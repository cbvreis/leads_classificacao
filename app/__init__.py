from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


from .models import pipeline
from .routes import routes
from .views import pipeline
