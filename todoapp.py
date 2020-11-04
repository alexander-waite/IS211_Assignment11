from flask import Flask, render_template, request, redirect

app = Flask(__name__)
fakelist = [["x", "x", "x"], ["y", "y", "y"], ["z", "z", "z"]]


@app.route('/')
def hello_world():
    author = "beast mode beast mode"
    name = "apex predator"
    return render_template('index.html', author=author, name=name, fakelist=fakelist)


@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    fakelist.append([task, email, priority])
    return redirect('/')


"""
@app.route('/clear')
def hello_world():
    author = "/submit"
    name = "/submit"
    return render_template('index.html', author=author, name=name)
"""

if __name__ == '__main__':
    app.run(debug=True)

# export FLASK_APP=hello.py
# flask run
# https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/
# http: // opentechschool.github.io / python - flask / core / files - templates.html
