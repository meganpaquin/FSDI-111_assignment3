from flask import (
    Flask,
    request,
    render_template
)

app = Flask(__name__)

# We created a module called database by adding the __init__.py file into that folder. You can import it like flask or other modules
from app.database import data_types

@app.get("/data_types")
def index():
    out = data_types.scan()
    return out



@app.get("/data_types/integers")
def integers():
    out = data_types.select_by_type(name="Integers")
    return out

@app.get("/data_types/floats")
def floats():
    out = data_types.select_by_type(name="Float")
    return out

@app.get("/data_types/booleans")
def booleans():
    out = data_types.select_by_type(name="Booleans")
    return out

@app.get("/data_types/about")
def about():
    return render_template("about.html")

@app.get("/data_types/strings")
def strings():
    return render_template("strings.html")

@app.get("/data_types/lists")
def lists():
    return render_template("lists.html")

@app.get("/data_types/reference")
def reference():
    return render_template("reference.html")

@app.get("/data_types/tuples")
def tuples():
    return render_template("tuples.html)")

@app.get("/data_types/dictionaries")
def dictionaries():
    return render_template("dictionaries.html")

@app.post("/data_types")
def create_data_type():
    data_body = request.json
    data_types.create(data_body)
    return "", 204

@app.put("/data_types/<int:key>")
def update_data(key):
    data_body = request.json
    data_types.update(data_body, key)
    return "", 204

@app.delete("/data_types/<int:key>")
def delete_data(key):
    data_body = request.json
    data_types.delete(data_body, key)
    return "", 204