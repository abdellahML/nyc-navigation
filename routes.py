from flask import Flask, request, render_template,flash,jsonify
from flask_bootstrap import Bootstrap
import os
import json
from ny_map_osmnx import NYMapOSMnx
from flask_wtf.csrf import CSRFProtect

from ny_map_osmnx import NYMapOSMnx

#csrf = CSRFProtect()

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'any secret string'
Bootstrap(app)
#csrf.init_app(app)

"""[Home route]

Returns:
    [View]: [login page]
"""

@app.route("/")
def home():
    return render_template("home.html",map=map)

@app.route('/get_post_json',methods=["GET", "POST"])
def get_post_json():

    osmnx = NYMapOSMnx()
    response = request.get_json(force=True)
    origin = tuple(response[0][0].values())
    destination = tuple(response[1][0].values())
    result = osmnx.safest_way(origin, destination, False)
    result = ','.join(map(str, result))
    return json.dumps( {"data": result})


if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))

        app.run(host='0.0.0.0', port=port, debug=True)

