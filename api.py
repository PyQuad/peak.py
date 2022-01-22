from sanic import Sanic, json

app = Sanic("PeakAPI")

@app.get('/')
async def index(request):
    return json({'message': 'Peak API says hello!'})

@app.get('/ping')
async def ping(request):
    url = request.args.get("url")

    return json({'message': url})

if __name__ == "__main__":
    app.run()
