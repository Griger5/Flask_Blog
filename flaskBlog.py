from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "bdfba6c8dadf2cc4b42f5a78a5831a95"

kretList = [
    {
        "author":"Molerasmus",
        "title":"Mole Wisdom",
        "content":"There's nothing noble in being superior to your fellow moles, true nobility lies in being superior to your former self",
        "date":"27 lutego 1210"
    },
    {
        "author":"Author 2",
        "title":"Title 2",
        "content":"lorem ipsum",
        "date":"1 września 1970"
    },
    {
        "author":"Author 3",
        "title":"Title 3",
        "content":"content content",
        "date":"9 września 1999"
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Rejestracja", form=form)
#@app.route("/login")
#def login():
 #   form = LoginForm()
  #  return render_template("login.html", title="Zaloguj się", form=form)

@app.route("/kret")
def kret():
    return render_template("kret.html", title="Krecie Sprawy", kretList=kretList)

@app.route("/kret/post1")
def post1():
    return render_template("post.html", title="Post1", post=kretList[0])
@app.route("/kret/post2")
def post2():
    return render_template("post.html", title="Post2", post=kretList[1])

if __name__ == "__main__":
    app.run()