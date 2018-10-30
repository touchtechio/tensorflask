
setup an account and login to our region (oregon)
https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:sort=instanceId

create iam user with admin priveleges. generate the key/secret pair.  copy these into your ```~/.aws/credentials``` like so :

```
[default]
aws_access_key_id=THISSHOULDLOOKLIKEGARBAGE
aws_secret_access_key=ThisWillBeMoreGarbageAndLonger
```

install ansible for remote admin

[https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
)

install python modules for ansible and boto for managing credentials.  
```
pip install ansible boto3 botocore
```

create an inventory directory or update your local ansible hosts dynamically from ec2

your ```/etc/ansible/hosts``` should be created from the ansible provided ec2.py and made executeable. this will reachout to aws for a full inventory of your machines to run playbooks against. alternatively you can run your ansible commands with the ```-i inventory``` parameter like so ansible -i ec2.py -u ubuntu us-west-2b -m ping



run the following playbook to create 3 test instances with ***verbose*** logging:

```
ansible-playbook -u ubuntu -vvv -e "type=test" -e "count=3" provision-ec2.yml
```



###dev

provisioning a test instance

```ansible-playbook  -vvv -e "type=deep" -e "count=1" provision-ec2.yml```


configure instance settings in the type vars ./ec2_vars/test.yml

tune the task of privisioning: ./roles/provision-ec2/tasks/main.yml


### cheap: very inexpensive provision settings for a test instance

```
#file: ./ec2_vars/test.yml

key_name: <pem-file-path>
aws_region: us-west-2
vpc_id: vpc-e79efe9e
ami_id: ami-ba602bc2
instance_type: t2.micro
my_local_cidr_ip: 0.0.0.0/0
security_group: matt-aws-intel
keypair: <key-pair>
image: ami-ba602bc2
elastic_ip: <public-ip>
```




### launching ansible playbooks

```ansible-playbook -u ubuntu -e "type=deep" add-media.yml```


```ansible-playbook -u ubuntu -e "type=deep" add-efs.yml```


```
ansible-playbook -e "type=webserver" -u ubuntu -e "count=1" provision-ec2.yml
ansible-playbook -e "type=webserver" -u ubuntu add-python2.yml
ansible-playbook -e "type=webserver" -u ubuntu add-docker.yml
```




