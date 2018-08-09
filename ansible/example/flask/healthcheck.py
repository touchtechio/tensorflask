from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump

app = Flask(__name__)

# wrap the flask app and give a heathcheck url
health = HealthCheck(app, "/healthcheck")
envdump = EnvironmentDump(app, "/environment")

# add your own check function to the healthcheck
def redis_available():
    client = _redis_client()
    info = client.info()
    return True, "redis ok"

health.add_check(redis_available)

# add your own data to the environment dump
def application_data():
	return {"maintainer": "MattPinner",
	        "git_repo": "https://github.com/touchtechio/tensorflask"}

envdump.add_section("application", application_data)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


