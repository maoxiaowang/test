# test

## Description
- test

## Pre-requisites
### OS
- Linux (>=CentOS 7.0)
### Python
- Python (>=3.5)

### Software Dependency
- Redis (>=3.2)
- RabbitMQ (>=3.6)

### Python Third-Party Library
- django (>=2.0)
- celery (>=4.1)
- pymysql (>=0.8, install as MySQLdb)
- django-channels (optional for now)
- daphne (optional for now)

## Software Configuration
### config RabbitMQ
$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_user_tags myuser mytag
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
### celery test process
$ celery -A ecloud worker -l info (-P eventlet)
add '-P eventlet' at the end of line if you are testing on WIN10

## Django Test Initialization
1. python3 makemigrations (first time or after make changes to any models)
2. python3 migrate
3. python3 runserver 0.0.0.0:8000
