from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/login')
def login():
    return render_template('login.html')

@application.route('/admin')
def admin():
    return render_template('admin.html')

@application.route('/admin/login')
def admin_login():
    return render_template('admin_login.html')

@application.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@application.route('/profile')
def profile():
    return render_template('profile.html')

@application.route('/settings')
def settings():
    return render_template('settings.html')

@application.route('/user/profile')
def user_profile():
    return render_template('user_profile.html')

@application.route('/signup')
def signup():
    return render_template('signup.html')

@application.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

@application.route('/reset-password')
def reset_password():
    return render_template('reset_password.html')

@application.route('/admin/settings')
def admin_settings():
    return render_template('admin_settings.html')

@application.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@application.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html')

@application.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/secret')
def secret():
    return render_template('secret.html')
