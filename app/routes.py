from flask import (
    Flask,
    request,
    render_template)

app = Flask(__name__)

# We created a module called database by adding the __init__.py file into that folder. You can import it like flask or other modules
from app.database import data_types

RESPONSE = {
    "Status": "ok"
}

@app.get("/")
def home():
    response = dict(RESPONSE)
    response["data_types"] = data_types.scan()
    scan_data = response.get("data_types")
    return render_template('index.html', data_types=scan_data)

@app.get("/data_types")
def index():
    response = dict(RESPONSE)
    response["data_types"] = data_types.scan()
    scan_data = response.get("data_types")
    return render_template('index.html', data_types=scan_data)

@app.get("/data_types/about")
def about():
    return render_template("about.html")

@app.get("/data_types/Integers")
def Integers():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Integers")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])

@app.get("/data_types/Floats")
def Floats():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Floats")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])

@app.get("/data_types/Booleans")
def Booleans():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Booleans")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])

@app.get("/data_types/Strings")
def Strings():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Strings")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])

@app.get("/data_types/Lists")
def Lists():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Lists")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])

@app.get("/data_types/Tuples")
def Tuples():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Tuples")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])

@app.get("/data_types/Dictionaries")
def Dictionaries():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Dictionaries")
    scan_data = response.get("data_type")
    return render_template('data_type.html', data_type=scan_data[0])


@app.get("/data_types/reference")
def reference():
    return render_template("reference.html")



# Add, delete, change the database
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