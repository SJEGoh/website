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
        purpose = request.form.get("purpose")
        message = request.form.get("user_message")
        print(name, email, purpose, message)
    return render_template('contact.html')

@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/projects', methods = ['GET', 'POST'])
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/interests')
def interests():
    return render_template('interests.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')


