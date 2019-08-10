from flask import Flask, jsonify, make_response, request
import subprocess
import signal

app = Flask(__name__)

plugins = {
    'dashboard': False,
    '_dashboard_process': None
}


def get_dashboard_status():
    return int(plugins['dashboard'])


def turn_dashboard_on():
    plugins['dashboard'] = True
    plugins['_dashboard_process'] = subprocess.Popen(['python3', 'main.py'])


def turn_dashboard_off():
    plugins['dashboard'] = False
    if plugins['_dashboard_process']:
        plugins['_dashboard_process'].send_signal(signal.SIGINT)
        plugins['_dashboard_process'] = None


@app.route('/api/v1/dashboard/status', methods=['GET'])
def api_get_dashboard_status():
    return jsonify({'status': get_dashboard_status()})


@app.route('/api/v1/dashboard/status', methods=['POST'])
def api_update_dashboard_status():
    new_state = request.json['newState']
    if new_state == 'off':
        turn_dashboard_off()
    elif new_state == 'on':
        turn_dashboard_on()
    return jsonify({ 'status': get_dashboard_status() })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)