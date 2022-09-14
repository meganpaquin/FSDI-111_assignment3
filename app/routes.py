from flask import (
    Flask,
    request,
    render_template
)

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/integers")
def integers():
    out = data_types.select_by_type(_type="int")
    return out

@app.get("/floats")
def floats():
    out = data_types.select_by_type(_type="float")
    return out

@app.get("/booleans")
def booleans():
    out = data_types.select_by_type(_type="bool")
    return out

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/strings")
def strings():
    return render_template("strings.html")

@app.get("/lists")
def lists():
    return render_template("lists.html")

@app.get("/reference")
def reference():
    return render_template("reference.html")

@app.get("/tuples")
def tuples():
    return render_template("tuples.html)")

@app.get("/integers")
def integers():
    return render_template("integers.html")

@app.get("/dictionaries")
def dictionaries():
    return render_template("dictionaries.html")