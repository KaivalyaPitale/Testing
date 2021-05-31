# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        Medu = int(request.form['Medu'])
        Fedu = int(request.form['Fedu'])
        traveltime = int(request.form['traveltime'])
        studytime = int(request.form['studytime'])
        failures = int(request.form['failures'])
        health = int(request.form['health'])
        absences = int(request.form['absences'])
        G1 = int(request.form['G1'])
        G2 = int(request.form['G2'])
        sex_M = int(request.form['sex'])
        address_U = int(request.form['address'])
        famsize_LE3 = int(request.form['famsize'])
        reason = int(request.form['reason'])
        schoolsup_yes = int(request.form['schoolsup'])
        paid_yes = int(request.form['paid'])
        activities_yes = int(request.form['activities'])
        higher_yes = int(request.form['higher'])
        internet_yes = int(request.form['internet'])

        if reason == 4:
            reason_course = 0
            reason_home = 0
            reason_reputation = 1
        elif reason == 3:
            reason_course = 1
            reason_home = 0
            reason_reputation = 0
        elif reason == 2:
            reason_course = 0
            reason_home = 1
            reason_reputation = 0
        else:
            reason_course = 0
            reason_home = 0
            reason_reputation = 0

        prediction = model.predict([[
            age, Medu, Fedu, traveltime, studytime, failures, health, absences, G1, G2, sex_M,
            address_U, famsize_LE3, reason_course, reason_home, reason_reputation, schoolsup_yes, paid_yes,
            activities_yes, higher_yes, internet_yes
        ]])

        return render_template("prediction.html", prediction_text="Student will get an expected grade of {}".format(prediction))

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
