from flask import Flask

"""
__name__ is a special variable in Python, which in this case is simply the name of the
Python file without its extension, i.e. "app").
"""
app = Flask(__name__)

"""
@ symbol wraps the hello_world() function in another function, app.route(), 
which is defined by Flask. The function is then called whenever requests matching
the specified URL path are received by the Flask server (/hello).
"""
@app.route('/hello') # @ symbol is a decorator
def hello_world():
    return 'Hello World!'