from flask import Flask
from flask_cors import CORS
from flask_nameko import FlaskPooledClusterRpcProxy
from dotenv import load_dotenv
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path="{}/.env".format(BASEDIR))

app = Flask(__name__)

CORS(app)

CONFIG_METHOD = "main.config.{}".format(os.environ.get("APP_SETTINGS", "Develop"))

app.config.from_object(CONFIG_METHOD)


rpc = FlaskPooledClusterRpcProxy()
