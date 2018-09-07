from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html", title='content.ai')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


