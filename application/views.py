from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user

from .forms import SendForm, AssetForm, FilterForm

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


