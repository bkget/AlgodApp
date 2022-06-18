from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user

from .forms import SendForm, AssetForm, FilterForm

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/')
@login_required
def index():
    """Main page, displays balance"""
    balance = current_user.get_balance()
    return render_template('index.html', balance=balance)


@main_bp.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    """Provides a form to create and send a transaction"""
    form = SendForm()
    address = current_user.public_key
    if form.validate_on_submit():
        success = current_user.send(form.quantity.data, form.receiver.data, form.note.data)
        return render_template('success.html', success=success)

    # show the form, it wasn't submitted
    return render_template('send.html', form=form, address=address)

