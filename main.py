from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'throw3310@gmail.com'
app.config['MAIL_PASSWORD'] = 'kxpt rwsq fqzv mpja'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/send_email', methods=["POST"])
def send_email():
    fname = request.form['fname']
    lname = request.form['lname']
    city = request.form['city']
    email = request.form['email']
    height = request.form['height']
    weight = request.form['weight']
    gender = request.form['gender']
    FitnessGoals = request.form['fitness-goals']
    FitnessType = request.form['fitness-type']
    
    msg = Message(subject="trainer form",sender=email,recipients=['throw3310@gmail.com'])
    msg.body = "Name: " + fname + " " + lname + " " + "\n" + "City: " + city + "\n" + email + "\n" + "Height in inches: " + height + "\n" + "Weight in lbs: " + weight + "\n" + gender + "\n" + "Fitness Goals: " + FitnessGoals + "\n" + "Fitness Type: " + FitnessType
    mail.send(msg)
    return 'Email was sent successfully'



if __name__ == '__main__':
    app.run(debug=True)