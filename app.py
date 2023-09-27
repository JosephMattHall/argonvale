from sanic import Sanic
from routes import auth, companion, protected
from database import setup_database, SessionLocal

app = Sanic("argonvale")

# Register blueprints for different routes
app.blueprint(auth.bp)
app.blueprint(companion.bp)
app.blueprint(protected.bp)

@app.listener("before_server_start")
async def setup_app(app, loop):
    await setup_database()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
