from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from pi_helper_functions import Motor, generate_stream

motor = Motor()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_piCAN():
    if request.method == 'GET':
        try:
            data = {'operation_type': 'off'}
            return jsonify(data), 200
        except:
            raise SystemExit(0) 

@app.route('/360_cw', methods=['GET'])
def piCAN_360_clockwise():
    if request.method == 'GET':
        try:
            motor.do_360_clockwise()
            data = {'operation_type': '360_clockwise'}
            return jsonify(data), 200
        except:
            raise SystemExit(0) 

@app.route('/360_ccw', methods=['GET'])
def piCAN_360_counter_clockwise():
    if request.method == 'GET':
        try:
            motor.do_360_counter_clockwise()
            data = {'operation_type': '360_counter_clockwise'}
            return jsonify(data), 200
        except:
            raise SystemExit(0) 

@app.route('/90_cw', methods=['GET'])
def piCAN_90_clockwise():
    if request.method == 'GET':
        try:
            motor.do_90_clockwise()
            data = {'operation_type': '90_clockwise'}
            return jsonify(data), 200
        except:
            raise SystemExit(0) 

@app.route('/90_ccw', methods=['GET'])
def piCAN_90_counter_clockwise():
    if request.method == 'GET':
        try:
            motor.do_90_counter_clockwise()
            data = {'operation_type': '90_counter_clockwise'}
            return jsonify(data), 200
        except:
            raise SystemExit(0)

@app.route('/pi_camera', methods=['GET'])
def piCAN_camera():
    if request.method == 'GET':
        try:
            return Response(generate_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')
        except:
            raise SystemExit(0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
