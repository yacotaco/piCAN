from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Response
from server_helper_functions import generate_stream
import IPs as ip
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def piCAN_welcome():
    if request.method == 'GET':
        return render_template("public/welcome.html")
    
    if request.method == 'POST':
        return redirect(url_for('main'))

@app.route('/main', methods=['POST'])
def piCAN_main():
    if request.method == 'POST':
        try:
            r = requests.get(ip.MAIN_PAGE)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/360_cw', methods=['POST'])
def piCAN_360_cw():
    if request.method == 'POST':
        try:
            r = requests.get(ip.do_360_cw)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/360_ccw', methods=['POST'])
def piCAN_360_ccw():
    if request.method == 'POST':
        try:
            r = requests.get(ip.do_360_ccw)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/90_cw', methods=['POST'])
def piCAN_90_cw():
    if request.method == 'POST':
        try:
            r = requests.get(ip.do_90_cw)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/90_ccw', methods=['POST'])
def piCAN_90_ccw():
    if request.method == 'POST':
        try:
            r = requests.get(ip.do_90_ccw)
            return render_template("public/index.html", status_code=r.status_code)
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

@app.route('/camera', methods=['GET'])
def piCAN_camera():
    if request.method == 'GET':
        try:
            r = requests.get(ip.camera)
            return Response(r, mimetype='multipart/x-mixed-replace; boundary=frame')
        except requests.exceptions.ConnectionError as e:
            return render_template("public/index.html", status_code=503)

if __name__ == '__main__':
    app.run()
