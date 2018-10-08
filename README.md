#Instagram Clone
===================

- - - -
Author: [Dan Mungai](https://github.com/danalvin)
## Description
[Gallery](https://github.com/danalvin/Django-IP1) This web app is used to show pictures based on different location of shooting,categories and has photo descriptions. 

------------------------------------------------------------------------

## User 

1. View photos of interest
2. Like images and comment on them
3. Upload images
4. Login 
5. Sign up

## Features

+ [ ] Like images
+ [x] show Images
+ [x] Images have captions
+ [x] Sign up
+ [x] Login
+ [ ] search users



## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6.4

### Cloning the repository
```bash
git clone https://github.com/danalvin/Django-IP2 && cd IP2
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required
+ config==0.3.9
+ dj-database-url==0.5.0
+ Django==1.11
+ django-bootstrap3==10.0.1
+ django-bootstrap4==0.0.7
+ django-heroku==0.3.1
+ gunicorn==19.9.0
+ Pillow==5.2.0
+ psycopg2==2.7.5
+ python-decouple==3.1
+ pytz==2018.5
+ whitenoise==3.3.1


### Running Tests
```bash
python3.6 manage.py test
```

### Running the web app in development
```bash
python3.6 manage.py runserver
```
Open the app on your browser, by default on `127.0.0.1:8000`.

## Live Demo

The web app can be accessed from the following link


## Quickstart

```
usage: manage.py [-?] {server,test,shell,runserver} ...

positional arguments:
  {server,test,shell,runserver}
    server              Runs the Flask development server i.e. app.run()
    test                Run the unit tests.
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit
```

## Technology used

* [Python3.6](https://www.python.org/)
* [Django1.11](https://www.djangoproject.com/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/danalvin/Django-IP1]
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Dan Mungai][https://github.com/danalvin/Django-IP1]