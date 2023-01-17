<<<<<<< HEAD
from flask import Blueprint, render_template, request, flash
=======
from flask import Blueprint, render_template, request
>>>>>>> main

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)

    return render_template("login.html", text="Testing", boolean=True)

@auth.route('/logout')
def logout():
    return '<p>Logout<p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
<<<<<<< HEAD

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least  6 characters.', category='error')
        else:
            flash('Account created!', category='success')
            pass
=======
    if len(email) < 4:
        pass
    elif len(firstName) < 2:
        pass
    elif password1 != password2:
        pass
    elif len(password1) < 7:
        pass
    else:
        # add user to database
        pass
>>>>>>> main

    return render_template("sign_up.html")