from flask import Flask, render_template, redirect, request

from helpers import getWeatherForecast

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/forecast")
def forecast():
    if not request.args.get("latitude") or not request.args.get("longitude"):
        return redirect("/")

    forecast = getWeatherForecast(request.args.get("latitude"), request.args.get("longitude"))

    if not forecast:
        return redirect("/")

    return render_template("index.html", forecast=forecast)
