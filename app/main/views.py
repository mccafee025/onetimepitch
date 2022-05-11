from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from . import auth
from ..models import User, Pitch, Comment, Upvote, Downvote
from .. import db,photos
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile, CommentForm
@main.route('/')
def main_page():
    return redirect(url_for('auth.login'))
@main.route('/login')
def landing_page():
    title = 'Mathwiti | Login'
    return render_template('index.html', title = title)
