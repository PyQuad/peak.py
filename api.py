"""------------Importing Dependencies Start-----------"""
import logging

# Imported Sanic, Asynchronous web frameworks
from sanic import Sanic, json
# Imported AIOHttp, Asynchronous HTTP Client
from aiohttp import ClientSession

from tortoise.contrib.sanic import register_tortoise
from models import WebLogs

logging.basicConfig(level=logging.DEBUG)

# Imported ping to play with websites
from ping import ping_url

"""-----------Importing Dependencies End---------------"""

"""-------------Sanic App Start----------"""
# Created Sanic Application
app = Sanic("PeakAPI")


# Created a client session
@app.listener('before_server_start')
async def init(app, loop):
    app.ctx.aiohttp_session = ClientSession(loop=loop)


# Listener to close session
@app.listener('after_server_stop')
def finish(app, loop):
    loop.run_until_complete(app.ctx.aiohttp_session.close())
    loop.close()


# Main/Home Path
@app.get('/')
async def index(request):
    return json({'message': 'Peak API says hello!'})


# Created /ping path to get url
@app.get('/ping')
# Creating /url parameter
async def ping(request):
    url = request.args.get("url")
    result = await ping_url(url, app.ctx.aiohttp_session)
    return json(result)

"""-----------Sanic App End-----------"""

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True
)

# Let's run
if __name__ == "__main__":
    app.run()
