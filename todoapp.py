from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    author = "beast mode beast mode"
    name = "apex predator"
    return render_template('index.html', author=author, name=name)


@app.route('/submit')
def hello_world():
    author = "/submit"
    name = "/submit"
    return render_template('index.html', author=author, name=name)


@app.route('/clear')
def hello_world():
    author = "/submit"
    name = "/submit"
    return render_template('index.html', author=author, name=name)


if __name__ == '__main__':
    app.run()


#export FLASK_APP=hello.py
# flask run
# https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/
# http: // opentechschool.github.io / python - flask / core / files - templates.html