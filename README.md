# Flask Workshop

## About
A simple Flask application with routing and Jinja templates. Accompanying slides can be found [here](https://docs.google.com/presentation/d/1Ymkpu1PFn1XhtB4pIxzx-fhXnhv8OLi8lvx-xL6YhsE/edit?usp=sharing). Workshop held by the NYU Girls Who Code College Loop Chapter! To reach out with any general questions, please email nyugwc@gmail.com

## Setup
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
$ python3 -m venv env
$ source env/bin/activate
$ touch app.py .gitignore README.md requirements.txt
$ pip install Flask
$ python -m pip freeze > requirements.txt
```

### Open your project in your editor and create your basic app
```sh
$ export FLASK_APP=run.py      # Unix/Mac)
$ set FLASK_APP=run.py         # Windows
$ env:FLASK_APP = ".\run.py"  # Powershell
$ export FLASK_ENV=development
```

### Run the application
```sh
source env/bin/activate
flask run
```
Then navigate to the localhost the site is running on.

## Exiting the virtual environmment
```sh
deactivate
```

## Related resources
* [Flask Workshop Slides](https://docs.google.com/presentation/d/1Ymkpu1PFn1XhtB4pIxzx-fhXnhv8OLi8lvx-xL6YhsE/edit?usp=sharing)
* [Flask documentation](http://flask.pocoo.org/)
* [Jinja documentation](http://jinja.pocoo.org/)
* [Flask extensions](http://flask.pocoo.org/extensions/)
