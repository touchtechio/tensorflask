# tensorflask
These are example of hosting a TensorFlow models as Flask services for inference. 

I provide ansible configuration for provisioning services in aws. I'm working through configuring everything to work through ansible and docker containers for easy of deployment and modularity.

Features thus far are the installation of multiple hosts, the installation of docker dependencies, large file upload support, some tensorflow models, and basic flask site hosting

## Setup
1. You need Python 3.x with Flask and TensorFlow installed. You can [download ActivePython 3.5](https://www.activestate.com/activepython/downloads) which has all the required dependencies already pre-installed.
2. Clone to repository by clicking the clone button above.
3. Run `python app.py`.

## Usage

start in ansible/ansible-aws directory and run the playbooks from there

## License

Licensed under the Apache 2.0 license. See LICENSE file for details.
