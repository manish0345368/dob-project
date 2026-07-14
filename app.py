from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
app.secret_key = "manish123"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        name = request.form["name"]
        dob = datetime.strptime(request.form["dob"], "%Y-%m-%d").date()

        today = date.today()
        age = relativedelta(today, dob)

        total_days = (today - dob).days

        session["result"] = {
            "name": name,
            "dob": dob.strftime("%d/%m/%Y"),
            "today": today.strftime("%d/%m/%Y"),
            "years": age.years,
            "months": age.months,
            "days": age.days,
            "total_days": total_days,
            "hours": total_days * 24,
            "minutes": total_days * 24 * 60,
            "seconds": total_days * 24 * 60 * 60
        }

        return redirect(url_for("home"))

    result = session.pop("result", None)

    if result:
        return render_template("index.html", **result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)