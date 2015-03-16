from flask import Flask

app = Flask(__name__)
app.secret_key = '\x91;\xe6\x8cH\xe8a\x978*#\xb4\xc8X2T\xaf}F\xfa\xfbLV '
from app import views
