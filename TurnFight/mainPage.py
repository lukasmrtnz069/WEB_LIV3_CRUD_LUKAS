from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from TurnFight.auth import login_required
from TurnFight.db import get_db

bp = Blueprint('mainPage', __name__)


@bp.route('/')
def index():
    # Render the main page template
    return render_template('mainP/index.html')
