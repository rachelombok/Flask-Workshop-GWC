# NYU Girls Who Code Flask Workshop

## About
A simple Flask application with routing and Jinja templates. Accompanying slides can be found [here](https://docs.google.com/presentation/d/1Ymkpu1PFn1XhtB4pIxzx-fhXnhv8OLi8lvx-xL6YhsE/edit?usp=sharing). Workshop held by the NYU Girls Who Code College Loop Chapter! To reach out with any general questions, please email nyugwc@gmail.com

## Setup
*If you want to start this project from scratch ...*
### Install Python
Make sure you have Python downloaded on your device, download it [here](https://www.python.org). It should be Python version 2.7 or newer.

### Install Pip
If you do not have pip already installed on your computer, follow [this tutorial](https://pip.pypa.io/en/stable/installing/) to install pip. (pip3 should work aswell)

### Install your Virtual Environment & Flask
```sh
pip install virtualenv   
```

### Create your project directory
```sh
$ mkdir flask-project
$ cd flask-project 

$ python3 -m venv env       # for python3, MacOS, Linux
$ python -m virtualenv env  # for python2, MacOS, Linux
$ py -3 -m venv env         # for python3, Windows
$ py -2 -m virtualenv env   # for python2, Windows

$ source env/bin/activate   # activate env on MacOS, Linux
$ env\Scripts\activate      # activate env on Windows

$ touch app.py .gitignore README.md requirements.txt
$ pip install Flask
$ python -m pip freeze > requirements.txt
```

### Open your project in your editor and create your basic app
In your main.py:
```sh
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'
```

### Set up app in Terminal:
```sh
$ export FLASK_APP=run.py      # Unix/Mac)
$ set FLASK_APP=run.py         # Windows
$ env:FLASK_APP = ".\run.py"   # Powershell

$ export FLASK_ENV=development
```

### Run the application
```sh
flask run
```
Then navigate to the localhost the site is running on.

## Exiting the virtual environmment
```sh
deactivate
```

*If you prefer to use this repository... *
### Clone this repository
```sh
$ git clone https://github.com/rachelombok/Flask-Workshop-GWC.git
$ cd flask-workshop-gwc
$ pip install -r requirements.txt
```
*... and follow the previous steps for setting up the environment, and running.

Use this file for your [.gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)

## Related resources
* [Flask Workshop Slides](https://docs.google.com/presentation/d/1Ymkpu1PFn1XhtB4pIxzx-fhXnhv8OLi8lvx-xL6YhsE/edit?usp=sharing)
* [Flask documentation](http://flask.pocoo.org/)
* [Jinja documentation](http://jinja.pocoo.org/)
* [Flask extensions](http://flask.pocoo.org/extensions/)

## Extra 
* [Bootstrap CDN](https://getbootstrap.com)
* [Font Awesome CDN](https://fontawesome.com/how-to-use/customizing-wordpress/snippets/setup-cdn-webfont)

