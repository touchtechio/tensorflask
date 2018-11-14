from flask import render_template
import connexion
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'handlers': {
        'syslog': {
        'class': 'logging.handlers.SysLogHandler'
        }
    },
    'root': {
       'handlers': ['syslog']
    }
})

options = {'static_url_path': '/media/static'}

# Create the application instance
app = connexion.App(__name__, specification_dir='./', options=options)

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


application = app.app
application.static_url_path = '/media/static'


# remove old static map
url_map = application.url_map
try:
    for rule in url_map.iter_rules('static'):
        url_map._rules.remove(rule)
except ValueError:
    # no static view was created yet
    pass

# register new; the same view function is used
application.add_url_rule(
    application.static_url_path + '/<path:filename>',
    endpoint='static', view_func=application.send_static_file)


# Create a URL route in our application for "/"
@app.route('/media/')
def home():
    """
    This function just responds to the browser URL localhost:5000/media/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
