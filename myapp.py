
from flask import *
from DBM import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/reg")
def register():
    return render_template("signup.html")

@app.route("/log")
def login():
    return render_template("login.html")

@app.route("/recipe")
def recipe():
    return render_template("recipe.html")

@app.route('/addUser',methods=['POST'])
def newuser():
    name=request.form['name']
    passw=request.form['passw']

    t=(name,passw)
    addUser(t)
    return redirect("about") #need to redirect somewhere else this is only for demo

@app.route("/validUser",methods=['POST'])
def auth():
    name=request.form['name']
    passw=request.form['passw']
    t=(name,passw)
    authen=validUser()
    if (t in authen):
        return render_template("about.html") #need to redirect somewhere else this is only for demo
    return redirect("log")

@app.route("/recipelist")
def recipelist():
    data=allData()
    return render_template("recipelist.html",elist=data)

@app.route("/addrecipe",methods=['POST'])
def add_recipe():
    title=request.form['title']
    recipe=request.form['recipe']
    t=(title,recipe)
    addrecipe(t)
    return redirect("recipelist")

@app.route("/delete")
def dele():
    title=request.args.get("title")
    delData(title)
    return redirect("recipelist")

@app.route("/edit")
def edit_recipe():
    title=request.args.get("title")
    data=selectrecipe(title)
    return render_template("updaterecipe.html",row=data)

@app.route("/updaterecipe",methods=['POST'])
def update_recipe():
    title=request.form['title']
    recipe=request.form['recipe']
    t=(recipe,title)
    updaterecipe(t)
    return redirect("recipelist")

@app.route("/about")
def aboutrecipe():
    return render_template("about.html")



if(__name__=="__main__"):
    app.run(debug=True)