"""------------Importing Dependencies Start-----------"""
import logging

# Imported Sanic, Asynchronous web frameworks
import aiohttp
from sanic import Sanic, json

# Imported AIOHttp, Asynchronous HTTP Client
from aiohttp import ClientSession

from tortoise.contrib.sanic import register_tortoise

from tortoise_config import TORTOISE_ORM
from models import WebLog

# Imported ping to play with websites
from ping import Pinger

# Setup logging
logging.basicConfig(level=logging.DEBUG)

"-----------Importing Dependencies End---------------" ""

"""-------------Sanic App Start----------"""
# Created Sanic Application
app = Sanic("PeakAPI")


# Created a client session
@app.listener("before_server_start")
async def init(app, loop):
    # Bind the pinger class
    app.ctx.pinger = Pinger()

    # Bind the trace config
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(app.ctx.pinger.on_request_start)
    trace_config.on_request_end.append(app.ctx.pinger.on_request_end)
    app.ctx.aiohttp_session = ClientSession(loop=loop, trace_configs=[trace_config])

# Listener to close session
@app.listener("after_server_stop")
def finish(app, loop):
    # Close aiohttp loop on server stop
    loop.run_until_complete(app.ctx.aiohttp_session.close())
    loop.close()


# Main/Home Path
@app.get("/")
async def index(request):
    return json({"message": "Peak API says hello!"})


# Created /ping path to get url
@app.get("/ping")
# Creating /url parameter
async def ping(request):
    url = request.args.get("url")
    result = await app.ctx.pinger.ping_url(url, app.ctx.aiohttp_session)
    return json(result)


"""-----------Sanic App End-----------"""

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)

# Let's run
if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8000)),
        workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
        debug=bool(os.environ.get('DEBUG', ''))
    )
