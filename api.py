from sanic import Sanic, json

app = Sanic("PeakAPI")

@app.route('/')
async def test(request):
    return json({'hello': 'peak'})

if __name__ == "__main__":
    app.run()
