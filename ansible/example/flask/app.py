from flask import Flask
from flask import render_template
from flask_basicauth import BasicAuth
import os


## host all static files here
app = Flask(__name__, static_url_path='/static')

## get passwords passed in as env var on env creation or execution
try:
    os.environ["USERNAME"]
    os.environ["PASSWORD"]
except KeyError:
    print("Please set the environment variable USERNAME/PASSWORD")
    sys.exit(1)

app.config['BASIC_AUTH_USERNAME'] = os.environ["USERNAME"]
app.config['BASIC_AUTH_PASSWORD'] = os.environ["PASSWORD"]

# simple auth doesn't protect us from snooping passwords
#app.config['BASIC_AUTH_USERNAME'] = 'eddywasabadman'
#app.config['BASIC_AUTH_PASSWORD'] = 'bowlofricefordinner'


## protect a portion of the site behind basic http-auth
basic_auth = BasicAuth(app)


## splach screen
@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html', title='content.ai')


## protected portion
@app.route('/internal')
@basic_auth.required
def secret_view():
    return render_template('internal.html', title='content.ai')


## start app and accept connections from anywhere
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


