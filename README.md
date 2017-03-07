MyAPI
======

A Sample RESTful API written in Python and uses [Flask](http://flask.pocoo.org) and [Connexion](https://github.com/zalando/connexion) / [Swagger](http://swagger.io) as frameworks, [PostgreSQL](https://www.postgresql.org) as database and [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) as Object Relational Mapper.

Requirements
------------
1. [docker-compose] version 1.6.0+

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
