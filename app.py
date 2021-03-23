#!/usr/bin/env python3
"""
Simple health check app for raspberry pi server
"""

import flask
from flask import jsonify

from checks.ExtFsMounted import ExtFsMountedHealthCheck
from checks.Temperature import TemperatureHealthCheck



health_checks = [
    ExtFsMountedHealthCheck("Stockpile", "/media/Stockpile/Data"),
    ExtFsMountedHealthCheck("Freezer", "/media/Stockpile/Data"),
    TemperatureHealthCheck()
]

app = flask.Flask(__name__)

@app.route("/health-check")
def health_check():
    healthy = True
    results = []
    for check in health_checks:
        name = check.name()
        try:
            result = check.run()
            healthy = result.healthy
            healthy &= healthy
            results.append({"name": name, "result": result.as_json(), "healthy": healthy})
        except Exception as e:
            results.append({"name": name, "error": str(e), "healthy": False})
            healthy = False

    return jsonify({
        "healthy" : healthy,
        "results" : results
    })


app.run(host="0.0.0.0", port="8069")
