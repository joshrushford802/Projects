from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/certifications-&-education")
def certifications_and_education():
    return render_template("certifications-&-education.html")

@app.route("/connect-with-me")
def connect_with_me():
    return render_template("connect-with-me.html")


if __name__ == '__main__':
    app.run()