from flask import Flask
from config import config
from routes import init_routes
import os

app = Flask(__name__)

env = os.getenv("FLASK_ENV", "development")
app.config.from_object(config[env])

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

init_routes(app)

if __name__ == "__main__":
    app.run(debug=(env == "development"))
