from sanic import Sanic, json
from aiohttp import ClientSession

from ping import ping_url

app = Sanic("PeakAPI")

@app.listener('before_server_start')
async def init(app, loop):
    app.ctx.aiohttp_session = ClientSession(loop=loop)

@app.listener('after_server_stop')
def finish(app, loop):
    loop.run_until_complete(app.ctx.aiohttp_session.close())
    loop.close()

@app.get('/')
async def index(request):
    return json({'message': 'Peak API says hello!'})

@app.get('/ping')
async def ping(request):
    url = request.args.get("url")

    result = await ping_url(url, app.ctx.aiohttp_session)

    return json(result)

if __name__ == "__main__":
    app.run()
