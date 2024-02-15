from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from TurnFight.auth import login_required
from TurnFight.db import get_db

bp = Blueprint('armor', __name__)


@bp.route('/armor', methods=('GET', 'POST'))
def armor_creation():
    armor_records = []

    if request.method == 'POST':
        armorname = request.form['armor_name']
        armordefense = request.form['armor_defense']
        db = get_db()
        error = None

        if not armorname:
            error = 'An armor name is required.'
        elif not armordefense:
            error = 'A defense value is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO Armor (armor_name, armor_defense) VALUES (?, ?)",
                    (armorname, armordefense),
                )
                db.commit()
            except db.IntegrityError:
                error = f"The {armorname} armor is already registered in the database."

        flash(error)
        db = get_db()
        armor_records = db.execute('SELECT * FROM armor').fetchall()

    return render_template('charpage/armor.html', armor_records=armor_records)