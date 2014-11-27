from flask import request, render_template, jsonify
from app import app

@app.route("/<name>", methods=["GET","POST"])
@app.route("/")
def intake(name=''):
    if name == "Eric":
        obj = jsonify({"name":"Eric Schles",
                        "job":"fightin' slavery",
                        "email":"eric.schles@syncano.com"})
        return render_template("index.html",obj=obj.get_data())
    elif name == "Lior":
        obj = jsonify({"name":"Lior Shahverdi",
                        "job":"nope",
                        "email":"like I'd tell you..."})
        return render_template("index.html",obj=obj.get_data())
    else:
        obj=''
        return render_template("index.html",obj=obj)

@app.route("/get",methods=["GET","POST"])
def get():
    name = request.form.get("name")
    id = request.form.get("id")
    if name == "Eric":
        return jsonify({"name":"Eric Schles",
                        "job":"fightin' slavery",
                        "email":"eric.schles@syncano.com"})
    if name == "Lior":
        return jsonify({"name":"Lior Shahverdi",
                        "job":"nope",
                        "email":"like I'd tell you..."})

