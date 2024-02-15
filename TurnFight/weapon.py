from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from TurnFight.auth import login_required
from TurnFight.db import get_db

bp = Blueprint('weapon', __name__)


@bp.route('/weapon', methods=('GET', 'POST'))
def weapon_creation():
    if request.method == 'POST':
        weaponname = request.form['weapon_name']
        weapontype = request.form['weapon_type']
        weapondamage = request.form['weapon_damage']
        db = get_db()
        error = None

        if not weaponname:
            error = 'A weapon name is required.'
        elif not weapontype:
            error = 'A weapon type is required.'
        elif not weapondamage:
            error = 'A weapon damage is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO Weapon (weapon_name, weapon_type, weapon_damage) VALUES (?, ?, ?)",
                    (weaponname, weapontype, weapondamage),
                )
                db.commit()
            except db.IntegrityError:
                error = f"The {weaponname} armor is already registered in the database."

        flash(error)

    return render_template('charpage/weapon.html')
