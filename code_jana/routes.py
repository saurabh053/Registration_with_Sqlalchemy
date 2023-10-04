from code_jana import app
from flask import render_template, redirect, url_for, flash
from code_jana.forms import RegistrationForm, LoginForm


@app.route("/home")
def homepage():
    return render_template("homepage.html", title='Home')


@app.route("/about")
def about():
    return render_template("About.html", title='About')


@app.route("/account")
def account():
    return render_template("Account.html", title='Account')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully form {form.username.data}', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'saurabh@gmail.com' and form.password.data == '123456':
            flash(f'Login Successful for {form.email.data}', category='success')
            return redirect(url_for('account'))
        else:
            flash(f'Login unsuccessful for {form.email.data}', category='danger')
    return render_template('login.html', title='login', form=form)
