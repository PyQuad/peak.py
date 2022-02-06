import aiohttp
import asyncio
from aiohttp.client_exceptions import ClientConnectorCertificateError, ClientConnectorError, InvalidURL

from models import WebLog

class Pinger:
    def __init__(self):
        self.current_ping = 0
    
    async def save_log(self, **kwargs):
        return await WebLog.create(**kwargs)

    async def on_request_start(self, session, trace_config_ctx, params):
        self.current_ping = 0  # reset on every request
        trace_config_ctx.start = asyncio.get_event_loop().time()

    async def on_request_end(self, session, trace_config_ctx, params):
        self.current_ping = (asyncio.get_event_loop().time() - trace_config_ctx.start) * 100
        print("Request took {}".format(self.current_ping))

    async def ping_url(self, url, session):
        resp = None
        try:
            resp = await session.get(url)
            #await resp.read() # reading the contents is critical to the actual response times

            # Return success response
            return {"message": {"status": resp.status, "reason": resp.reason, "ping": self.current_ping}}

        # Handling Errors
        except ClientConnectorCertificateError:
            return {"error": "SSLError"}
        except InvalidURL:
            return {"error": "InvalidURL"}
        except ClientConnectorError:
            return {"error": "ClientConnectorError"}
        except TypeError:
            return {"error": "NoInput"}
        finally:
            if resp:
                # Save a web log
                await self.save_log(
                    site_addr=resp.url,
                    ping_ms=self.current_ping,
                    status=resp.status,
                    reason=resp.reason
                )

                # Close the response
                resp.close()
