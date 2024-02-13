from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from TurnFight.auth import login_required
from TurnFight.db import get_db

bp = Blueprint('armor', __name__)