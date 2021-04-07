from flask import Flask, render_template, url_for, request, redirect
import json
import csv
app = Flask(__name__)


contact_info = {
    "email": "rbo224@nyu.edu",
    "linkedin": "https://www.linkedin.com/in/rachelombok",
    "github": "https://github.com/rachelombok",
    "twitter": "https://twitter.com/rachelombok"
}

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', contact=contact_info,)

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/portfolio")
def portfolio():
    projects = []
    with open('./projects.json') as proj_info:
        data = json.load(proj_info)
        for i in range(len(data['obj'])):
            projects.append(data['obj'][i])
    
    return render_template('items.html', items=projects)

@app.route("/projects/<string:title>")
def projects_view(title):
    project = {"description": "yep", "title": "title"}
    
    with open('./projects.json') as proj_info:
        data = json.load(proj_info)
        for i in range(len(data['obj'])):
            if title == data['obj'][i]['title']:
                projects = data['obj'][i]
    return render_template("project.html",
                           title=project['title'],
                           project=projects
                          )


if __name__ == '__main__':
  app.run(debug=True)
