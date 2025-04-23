from flask import current_app as app
from flask import render_template, url_for, redirect, request, make_response

from .forms import ContactForm, SignupForm


@app.route('/')
def home():
    nav = [
        {'name': 'Sign Up', 'url': url_for('signup')},
        {'name': 'Contact Us', 'url': url_for('contact')}
    ]
    return render_template(
        'home.html',
        nav=nav,
        title='Jinja Demo Site',
        description='Something smart with Flask & Jinja',
    )


@app.route('/contact', methods=['GET'])
def contact():
    print('in contact')
    form = ContactForm()
    nav = [
        {'name': 'Home', 'url': url_for('home')},
        {'name': 'Sign Up', 'url': url_for('signup')},
    ]
    return render_template(
        'contact.html',
        form=form,
        template='form-template',
        nav=nav
    )


@app.route('/contact', methods=['POST'])
def contact_submit():
    print('in contacti_submit')
    form = ContactForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('success'))
    nav = [
        {'name': 'Home', 'url': url_for('home')},
        {'name': 'Sign Up', 'url': url_for('signup')},
    ]
    return render_template(
        'contact.html',
        form=form,
        template='form-template',
        nav=nav
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """User sign-up form for account creation."""
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    nav = [
        {'name': 'Home', 'url': url_for('home')},
        {'name': 'Contact Us', 'url': url_for('contact')}
    ]
    return render_template(
        "signup.html",
        form=form,
        template="form-template",
        title="Signup Form",
        nav=nav
    )


@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    nav = [
        {'name': 'Home', 'url': url_for('home')},
        {'name': 'Sign Up', 'url': url_for('signup')},
        {'name': 'Contact Us', 'url': url_for('contact')}
    ]
    return render_template(
        "success.html",
        template="success-template",
        nav=nav
    )


@app.before_request
def last_page_viewd():
    print('Sending out:', request.path)


@app.errorhandler(404)
def not_found(error):
    print(error.__dict__)
    return make_response(render_template("404.html"), 404)
