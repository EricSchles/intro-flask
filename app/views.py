from flask import request, render_template, jsonify

@app.route("/<name>", methods=["GET","POST"])
@app.route("/")
def intake(name=''):
    if name == "Eric":
        obj = jsonify({"name":"Eric Schles",
                        "job":"fightin' slavery",
                        "email":"eric.schles@syncano.com"})
    elif name == "Lior":
        obj = jsonify({"name":"Lior Shahverdi",
                        "job":"nope",
                        "email":"like I'd tell you..."})
    else:
        obj=''
    return render_template("index.html",obj=obj)

@app.route("/get",methods=["GET","POST"])
def get_input():
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

