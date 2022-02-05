from aiohttp.client_exceptions import ClientConnectorCertificateError, ClientConnectorError, InvalidURL

from models import WebLog

current_ping = 0

async def save_log(**kwargs):
    return await WebLog.create(**kwargs)

async def on_request_start(session, trace_config_ctx, params):
    current_ping = 0 # reset on every request
    trace_config_ctx.start = asyncio.get_event_loop().time()

async def on_request_end(session, trace_config_ctx, params):
    current_ping = asyncio.get_event_loop().time() - trace_config_ctx.start
    print("Request took {}".format(elapsed))

trace_config = aiohttp.TraceConfig()
trace_config.on_request_start.append(on_request_start)
trace_config.on_request_end.append(on_request_end)

# Outputs
async def ping_url(url, session):
    resp = None
    try:
        resp = await session.get(url, trace_configs=[trace_config])
        
        # Return success response
        return {"message": {"status": resp.status, "reason": resp.reason}}
        
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
        # Save a web log
        await save_log(
        	site_addr=resp.url,
            ping_ms=current_ping,
            status=resp.status,
            reason=resp.reason
        )
        
    	# Close the response
        if resp:
    		resp.close()
