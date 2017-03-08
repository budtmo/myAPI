MyAPI
======

[![Build Status](https://travis-ci.org/butomo1989/myAPI.svg?branch=master)](https://travis-ci.org/butomo1989/myAPI)
[![codecov](https://codecov.io/gh/butomo1989/myAPI/branch/master/graph/badge.svg)](https://codecov.io/gh/butomo1989/myAPI)


A Sample RESTful API written in Python and uses [Flask](http://flask.pocoo.org) and [Connexion](https://github.com/zalando/connexion) / [Swagger](http://swagger.io) as frameworks, [PostgreSQL](https://www.postgresql.org) as database, [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) as Object Relational Mapper and [Gunicorn](http://gunicorn.org) as WSGI HTTP Server.

Requirements
------------
1. [docker-compose](https://docs.docker.com/compose/install/) version 1.6.0+

Quick Start
-----------
1. Run application and its database with command:

	```bash
	local.sh run
	```

2. accees [app](http://127.0.0.1:8080/ui) through web browser.

	![][app]

Unit test
---------
```bash
local.sh test
```

Troubleshooting
---------------
```bash
local.sh debug
```

[app]: <img/app.png>
