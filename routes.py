from flask import Flask
from flask import Flask, request, render_template
import os
from ny_map_osmnx.py import getSafest

app = Flask(__name__)

"""[Home route]

Returns:
    [View]: [login page]
"""


@app.route("/",methods=["GET", "POST"])
def home():
    return render_template("home.html")
def form():
    origin = request.form["origin"]
    print(origin)
    destination = request.form["destination"]
    print(destination)
    result = getSafest(origin,destination)
    return render_template("safest_path.html", safest_png= result)


if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
