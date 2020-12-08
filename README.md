# nba-api

> OpenAPI Flask app that serves data to measuredstudios.com

## Features

Its not just Flask but an ecosystem to properly create a RESTful API service... SO FILE app_refactored.py is that using:

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight WSGI web application framework in Python. It is designed to make getting started very quickly and very easily.
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/) is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) is a thin integration layer for Flask and marshmallow that adds additional features to marshmallow.
- [SQLAlchemy](https://www.sqlalchemy.org/library.html) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [Alembic](http://alembic.zzzcomputing.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask.
- [Tailwind](https://tailwindcss.com/) is a utility-first CSS framework for rapidly building custom user interfaces.


This project integrates other Flask libraries using: 

- [Blueprints](https://flask.palletsprojects.com/en/1.0.x/blueprints/) for scalability.
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system (passwords hashed with bcrypt).
- [flask_migrate](https://flask-migrate.readthedocs.io/en/latest/).
- [Flask-Script](https://flask-script.readthedocs.io/)
- [Flask-User](http://flask-user.readthedocs.io/en/v0.6/)

### Code characteristics

* Tested on Python 2.6, 2.7, 3.3, 3.4, 3.5 and 3.6
* Well organized directories with lots of comments
    * app
        * commands
        * models
        * static
        * templates
        * views
    * tests
* Includes test framework (`py.test`)
* Includes database migration framework (`alembic`)
* Sends error emails to admins for unhandled exceptions

## Installation

### 1. Get the code
    git clone 
    cd nba-api

### 2. Install requirements 
pip install -r requirements.txt

### Initializing the Database

    # Create DB tables and populate the roles and users tables
    python manage.py init_db

### Configuring SMTP

Edit the `local_settings.py` file.

Specifically set all the MAIL_... settings to match your SMTP settings

Note that Google's SMTP server requires the configuration of "less secure apps".
See https://support.google.com/accounts/answer/6010255?hl=en

### 3. Set the FLASK_APP environment variable
```powershell
PS ~/nba-api/> $env:FLASK_APP = 'app'
PS ~/nba-api/> $env:FLASK_ENV = 'development'
PS ~/nba-api/> python app.py
```

### 4. Run the application

#### Running the app (production)

To run the application in production mode, gunicorn3 is used (and included in requirements.txt.

    # Run the application in production mode
    ./runserver.sh

#### Running the automated tests

    # Start the Flask development web server
    py.test tests/

#### Using Server-side Sessions

Don't use server side session data! You should do everything you can to keep each request/response stateless. It'll be easier to maintain your code and easier to debug when something goes wrong.  

However, if you really need sessions, FlaskDash has Flask-Session built in (https://pythonhosted.org/Flask-Session/).  It is configured to use to the SQLAlchmey interface by default and the init_db command will set up a sessions table in your database.  You can change your configuration to use redis or MongoDB, as well.

Sessions are available in misc_views.py and can be added to any additional controllers you create.

This is how you might use it:

    # Session example
    session['key'] = 'value'
    val = session.get('key', 'not set')
    print(val)
    value    
    val = session.get('key2', 'not set')
    print(val)
    not set

### Trouble shooting

If you make changes in the Models and run into DB schema issues, delete the sqlite DB file `app.sqlite`.

## Example

/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/temp/2017-06-01/2017-06-30

## Data Powering the Web app

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Need to add Celery
- [ ] Add the mail blueprint
- [ ] https://github.com/cburmeister/flask-bones

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
