import aiohttp
import asyncio
from aiohttp.client_exceptions import ClientConnectorCertificateError, ClientConnectorError, InvalidURL

from models import WebLog

current_ping = 0


async def save_log(**kwargs):
    return await WebLog.create(**kwargs)


async def on_request_start(session, trace_config_ctx, params):
    current_ping = 0  # reset on every request
    trace_config_ctx.start = asyncio.get_event_loop().time()


async def on_request_end(session, trace_config_ctx, params):
    current_ping = asyncio.get_event_loop().time() - trace_config_ctx.start
    print("Request took {}".format(current_ping))





# Outputs
async def ping_url(url, session):
    resp = None
    try:
        resp = await session.get("https://saharaa.in")
        #rp = await resp.read()
        #print(rp)

        # Return success response
        return {"message": {"status": resp.status, "reason": resp.reason}}

    # Handling Errors
    except ClientConnectorCertificateError:
        return {"error": "SSLError"}
    except InvalidURL:
        return {"error": "InvalidURL"}
    except ClientConnectorError:
        return {"error": "ClientConnectorError"}
    except TypeError as e:
        print(e)
        return {"error": "NoInput"}
    finally:
        if resp:
            # Save a web log
            await save_log(
                site_addr=resp.url,
                ping_ms=current_ping,
                status=resp.status,
                reason=resp.reason
            )

            # Close the response
            resp.close()
