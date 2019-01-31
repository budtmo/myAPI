MyAPI
======

[![Build Status](https://travis-ci.org/budtmo/myAPI.svg?branch=master)](https://travis-ci.org/budtmo/myAPI)
[![codecov](https://codecov.io/gh/budtmo/myAPI/branch/master/graph/badge.svg)](https://codecov.io/gh/budtmo/myAPI)


A Sample RESTful API written in Python and uses [Flask](http://flask.pocoo.org) and [Connexion](https://github.com/zalando/connexion) / [Swagger](http://swagger.io) as frameworks, [PostgreSQL](https://www.postgresql.org) as database, [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) as Object Relational Mapper, [Gunicorn](http://gunicorn.org) as WSGI HTTP Server and [Nginx](https://nginx.org/en/) as Proxy Server.

Requirements
------------
1. [docker-compose](https://docs.docker.com/compose/install/) version 1.6.0+

Quick Start
-----------
1. Run application and its database with command:

	```bash
	local.sh run
	```

2. accees [app](http://127.0.0.1/ui) through web browser.

	![][app]

Unit test
---------
```bash
local.sh test
```

Troubleshooting
---------------
All logs inside container are stored under folder **/var/log/supervisor**. you can print out log file by using **docker exec**. Example:

```bash
docker exec -it api tail -f /var/log/supervisor/gunicorn.stdout.log
```

[app]: <img/app.png>
