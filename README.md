# Internal IP

This is a sample web service to manage a list of IP and IP ranges

## Getting Started

To develop this project you need python 2.7 and Docker

### Prerequisites

Check if your python version is > 2.7, also is recommended docker compose and virtualenv.

```
$ python -V
Python 2.7.15

$ docker version
Client: Docker Engine - Community
 Version:           18.09.1

$ docker-compose version
docker-compose version 1.23.2, build 1110ad01
docker-py version: 3.6.0
CPython version: 3.6.6
OpenSSL version: OpenSSL 1.1.0h  27 Mar 2018

$ virtualenv --version
16.2.0
```

### Install

To get a local version you need follow the steps:

```
$ git clone github.com/cirolini/internalip
$ cd zaz-ws-ip-internal
$ virtualenv venv
$ source venv/bin/activate
$ pip install -e .
```

## Initializing

Some things importantes:

- .env
- .flaskenv

The .env file have enviromment variables which will be load for the application.

The .flaskenv file have enviromment variables which will be used for flask when we use the command "flask run".

Before to init application it is required have a local Redis, for this follow the commands above.

```
# init Redis in background
$ docker run -d -p 6379:6379 redis

# checking
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
fb5eb1f0d477        redis               "docker-entrypoint.s…"   1 minute ago         Up 1 minute          0.0.0.0:6379->6379/tcp   redis_1
```

Now you need load the database.

```
$ flask init-db
Registering IP: 127.0.0.1.
Registering IP: ::1.
Registering IP: 129.168.0.0/16.
Initialized the database.
```
After this is just initializing the application.

```
$ flask run
 * Serving Flask app "internalIP" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 229-209-843
```

Everytime you modify any application file the web server will be restarted and you can test your modifications.

### Initializing with docker compose

For test the app with docker you can use docker compose. With docker-compose.yaml you init the app and  Redis.

```
# build containers
$ docker-compose build

# up redis in background
$ docker-compose up -d redis

# up application
$ docker-compose up app
```

The same for everytime you modify any application file the web server (uWSGI) will be restarted and you can test your modifications.

## Running the unit tests

The app is ready to execute unit tests with Pytest integrated with Flask. You need Redis up and a virtualenv with app to execute the tests.

```
$ pytest -v
========================================================================================= test session starts =========================================================================================
platform darwin -- Python 2.7.15, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Users/rafaelcirolini/ip-internal/venv/bin/python2.7
cachedir: .pytest_cache
rootdir: /Users/rafaelcirolini/ws-ip-internal, inifile:
collected 5 items

test/test_api.py::test_health PASSED                                                                                                                                                            [ 20%]
test/test_api.py::test_list_all_internal PASSED                                                                                                                                                 [ 40%]
test/test_api.py::test_add_ip PASSED                                                                                                                                                            [ 60%]
test/test_api.py::test_is_internal PASSED                                                                                                                                                       [ 80%]
test/test_api.py::test_remove_ip PASSED                                                                                                                                                         [100%]

====================================================================================== 5 passed in 0.50 seconds =======================================================================================
```

After this we can use the Coverage to measuring code coverage.

```
$ coverage run -m pytest

$ coverage report -m | grep internalIP
internalIP/__init__.py                                                                18      0   100%
internalIP/api.py                                                                     36      4    89%   26-27, 35-36
internalIP/db.py                                                                      15      1    93%   25
```

## Running the Pylint

Allways check Pylint.

```
(venv) Air-de-Rafael:ip-internal rafaelcirolini$ pylint internalip/*
No config file found, using default configuration
************* Module internalip.api
C: 12, 0: Argument name "f" doesn't conform to snake_case naming style (invalid-name)
W: 50,11: Catching too general exception Exception (broad-except)
W: 64,11: Catching too general exception Exception (broad-except)
C: 12, 0: Argument name "f" doesn't conform to snake_case naming style (invalid-name)
W: 50,11: Catching too general exception Exception (broad-except)
W: 64,11: Catching too general exception Exception (broad-except)

------------------------------------------------------------------
Your code has been rated at 8.99/10 (previous run: 8.70/10, +0.29)
```
