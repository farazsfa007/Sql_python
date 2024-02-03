from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/welcome')
def test():
    return "<h2>Welcome To abc Corporation</h2>"

@app.route('/')

def Msg():
    return """
<p>Company Name: ABC Corporation</p>
<p>Location: India</p>
<p>Contact Detail: 999-999-9999</p>
"""


@app.route('/hello')
def test2():
    data = request.args.get('x')
    # return '''<h1>this is the first flask app</h1>'''
    return "thie ie m4 {} ".format(data)

if __name__== "__main__":
    app.run(debug=True)