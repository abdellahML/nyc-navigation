from flask import Flask
from flask import Flask, request, render_template,flash
from flask_bootstrap import Bootstrap
import os
from ny_map_osmnx import NYMapOSMnx
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
Bootstrap(app)
csrf.init_app(app)

"""[Home route]

Returns:
    [View]: [login page]
"""

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test",methods=["POST"])
def test():
    origin = request.form["origin"]
    print(origin)
    destination = request.form["destination"]
    print(destination)
    NYMapOSMnx()
    coordinate = NYMapOSMnx.isPresent(origin,destination)
    #result = getSafest(origin,destination)
    if coordinate != True:
        flash(u'Look like you have entered a wrong origin or destination', 'error')
        return render_template("home.html",message = 'PLOPpeR de PLOP')
    else:
        return render_template("safest_path.html")


if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
