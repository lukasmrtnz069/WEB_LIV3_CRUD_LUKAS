from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from TurnFight.auth import login_required
from TurnFight.db import get_db

bp = Blueprint('trinket', __name__)


@bp.route('/trinket', methods=('GET', 'POST'))
def trinket_creation():
    if request.method == 'POST':
        trinketname = request.form['trinket_name']
        trinketwear = request.form['trinket_wearable_by']
        trinketbonus = request.form['trinket_bonus']
        db = get_db()
        error = None

        if not trinketname:
            error = 'A trinket name is required.'
        elif not trinketwear:
            error = 'Choose which class can wear this.'
        elif not trinketbonus:
            error = 'A trinket bonus is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO Trinket (trinket_name, trinket_wearable_by, trinket_bonus) VALUES (?, ?, ?)",
                    (trinketname, trinketwear, trinketbonus),
                )
                db.commit()
            except db.IntegrityError:
                error = f"The {trinketname} armor is already registered in the database."

        flash(error)

    return render_template('charpage/trinket.html')
