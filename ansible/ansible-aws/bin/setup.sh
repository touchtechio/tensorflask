#!/bin/bash

ansible-playbook -e "type=webserver" -u ubuntu -e "count=1" provision-ec2.yml
ansible-playbook -e "type=webserver" -u ubuntu add-python2.yml
ansible-playbook -e "type=webserver" -u ubuntu add-docker.yml
ansible-playbook -e "type=webserver" -u ubuntu add-nginx.yml
