from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')
        
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        purpose = request.form.get("purpose_of_contact")
        message = request.form.get("user_message")
        print(name, email, purpose, message)
    return render_template('contact.html')


