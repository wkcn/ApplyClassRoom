#!flask/bin/python
from app import app
app.run(host="0.0.0.0", port=int("80"), debug=True)
#app.run(debug = True)
