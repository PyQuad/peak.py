from sanic import Sanic, json

app = Sanic("PeakAPI")

@app.get('/')
async def index(request):
    return json({'message': 'Peak API says hello!'})

if __name__ == "__main__":
    app.run()
