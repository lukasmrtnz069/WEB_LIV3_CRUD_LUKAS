from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from TurnFight.db import get_db

bp = Blueprint('character', __name__)


@bp.route('/character', methods=('GET', 'POST'))
def character_creation():
    db = get_db()
    players = db.execute('SELECT id, username FROM user').fetchall()
    armors = db.execute('SELECT armor_id, armor_name FROM Armor').fetchall()
    weapons = db.execute('SELECT weapon_id, weapon_name FROM Weapon').fetchall()
    trinkets = db.execute('SELECT trinket_id, trinket_name FROM Trinket').fetchall()

    if request.method == 'POST':
        charname = request.form['char_name']
        charclass = request.form['char_class']
        charlevel = request.form['char_level']
        charhp = request.form['char_hit_points']
        userid = request.form['player_id']
        armorid = request.form['armor_id']
        weaponid = request.form['weapon_id']
        trinketid = request.form['trinket_id']
        db = get_db()
        error = None

        if not charname:
            error = 'A name is required.'
        elif not charclass:
            error = 'Choose your character''s class.'
        elif not charlevel:
            error = 'The character level is required'
        elif not charhp:
            error = 'The character hit points are required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO Personnage (char_name, char_class, char_level, char_hit_points, player_id, armor_id, "
                    "weapon_id, trinket_id "") VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (charname, charclass, charlevel, charhp, userid, armorid, weaponid, trinketid),
                )
                db.commit()
            except db.IntegrityError:
                error = f"The {charname} armor is already registered in the database."

        flash(error)

    return render_template('charpage/character.html', players=players, armors=armors, weapons=weapons, trinkets=trinkets)
