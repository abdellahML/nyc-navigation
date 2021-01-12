from flask import Flask
from flask import Flask, request, render_template,flash
from flask_bootstrap import Bootstrap
import os
import json
from ny_map_osmnx import NYMapOSMnx
from flask_wtf.csrf import CSRFProtect

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
    
    response = request.get_json(force=True)
    osmnx = NYMapOSMnx
    print(response['origin'])
    result = osmnx.safest_way(response['origin'],response['destination'],False)
    return render_template("home.html",data = response)
    #coordinate = isPresent(origin,destination)
    #result = safest_way(origin,destination)
    # if coordinate != True:
    #     flash(u'Look like you have entered a wrong origin or destination', 'error')
    #     return render_template("home.html",message = '')
    # else:
    #     return render_template("safest_path.html",result = result)


if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port,debug = True)
