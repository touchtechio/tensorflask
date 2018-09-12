from flask import Flask
from flask import render_template
from flask_basicauth import BasicAuth


app = Flask(__name__, static_url_path='/static')


app.config['BASIC_AUTH_USERNAME'] = 'eddy'
app.config['BASIC_AUTH_PASSWORD'] = 'bowl'

basic_auth = BasicAuth(app)


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html', title='content.ai')


@app.route('/internal')
@basic_auth.required
def secret_view():
    return render_template('internal.html', title='content.ai')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


