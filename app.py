from flask import Flask, render_template, request, redirect, url_for
# from flask import Flask, render_template, request
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        dob = datetime.strptime(request.form["dob"], "%Y-%m-%d").date()

        today = date.today()

        age = relativedelta(today, dob)

        years = age.years
        months = age.months
        days = age.days

        total_days = (today - dob).days
        hours = total_days * 24
        minutes = hours * 60
        seconds = minutes * 60

        return render_template(
            "index.html",
            name=name,
            dob=dob,
            today=today,
            years=years,
            months=months,
            days=days,
            total_days=total_days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)