from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
app.secret_key = "manish123"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dob", methods=["GET", "POST"])
def dob():
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

        return redirect(url_for("dob"))

    result = session.pop("result", None)

    if result:
        return render_template("index.html", **result)

    return render_template("index.html")

@app.route("/salary", methods=["GET", "POST"])
def salary():

    if request.method == "POST":

        employee = request.form["employee"]
        basic_salary = float(request.form["basic_salary"])
        bonus = float(request.form["bonus"])
        tax = float(request.form["tax"])

        gross_salary = basic_salary + bonus
        tax_amount = gross_salary * (tax / 100)
        net_salary = gross_salary - tax_amount

        return render_template(
            "salary.html",
            employee=employee,
            basic_salary=basic_salary,
            bonus=bonus,
            tax=tax,
            gross_salary=gross_salary,
            tax_amount=tax_amount,
            net_salary=net_salary
        )

    return render_template("salary.html")
@app.route("/student", methods=["GET", "POST"])
def student():

    if request.method == "POST":

        student = request.form["student"]
        marks = float(request.form["marks"])
        total = float(request.form["total"])

        percentage = (marks / total) * 100

        return render_template(
            "student.html",
            student=student,
            marks=marks,
            total=total,
            percentage=percentage
        )

    return render_template("student.html")
@app.route("/discount", methods=["GET", "POST"])
def discount():

    if request.method == "POST":

        item = request.form["item"]
        price = float(request.form["price"])
        discount = float(request.form["discount"])

        discount_amount = price * discount / 100
        final_price = price - discount_amount

        return render_template(
            "discount.html",
            item=item,
            price=price,
            discount=discount,
            final_price=final_price
        )

    return render_template("discount.html")
@app.route("/average", methods=["GET", "POST"])
def average():

    if request.method == "POST":

        numbers = request.form["numbers"]

        num_list = [float(x) for x in numbers.split(",")]

        total = sum(num_list)
        count = len(num_list)
        average = total / count

        return render_template(
            "average.html",
            total=total,
            count=count,
            average=average
        )

    return render_template("average.html")

@app.route("/gst", methods=["GET", "POST"])
def gst():

    if request.method == "POST":

        amount = float(request.form["amount"])
        gst = float(request.form["gst"])

        gst_amount = amount * gst / 100
        final_amount = amount + gst_amount

        return render_template(
            "gst.html",
            amount=amount,
            gst_amount=gst_amount,
            final_amount=final_amount
        )

    return render_template("gst.html")

@app.route("/emi", methods=["GET", "POST"])
def emi():

    if request.method == "POST":

        loan = float(request.form["loan"])
        rate = float(request.form["rate"])
        years = int(request.form["years"])

        monthly_rate = rate / (12 * 100)
        months = years * 12

        emi = (loan * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

        total_payment = emi * months
        total_interest = total_payment - loan

        return render_template(
            "emi.html",
            emi=round(emi, 2),
            total_payment=round(total_payment, 2),
            total_interest=round(total_interest, 2)
        )

    return render_template("emi.html")
if __name__ == "__main__":
    app.run(debug=True)
