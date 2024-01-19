from flask import Flask, jsonify, request
from monit import get_report, get_all_reports, get_avg_of_report, get_rapports_younger_than, get_last_rapport

app = Flask(__name__)

@app.route("/reports", methods=["GET"])
def reports():
    return jsonify(get_all_reports()),200

@app.route("/reports/<id>", methods=["GET"])
def report(id):
    return jsonify(get_report(id)), 200

@app.route("/reports/avg/<hours>", methods=["GET"])
def avg(hours):
    return jsonify(get_avg_of_report(int(hours))), 200

@app.route("/reports/last", methods=["GET"])
def last():
    return jsonify(get_last_rapport()), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)