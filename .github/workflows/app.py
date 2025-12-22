from flask import flask

app = flask(__name__)
@app.route(/)
def home () :
    return 'Hallo word'

@app.route('/about')
def about(): 
    return 'About'

if __name__"__name__" :
    app.run()
    