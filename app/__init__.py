from flask import Flask

app = Flask(__name__)

from app import routes
# The bottom import is a workaround to circular imports, a common problem with Flask applications.
