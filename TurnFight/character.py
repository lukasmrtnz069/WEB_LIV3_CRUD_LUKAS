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
                flash('Character created successfully!')

                characters = db.execute(
                    'SELECT p.char_id, p.char_name, p.char_class, p.char_level, p.char_hit_points, '
                    'u.username as username, a.armor_name as armor, w.weapon_name as weapon, t.trinket_name as trinket '
                    'FROM Personnage p '
                    'JOIN user u ON p.player_id = u.id '
                    'JOIN Armor a ON p.armor_id = a.armor_id '
                    'JOIN Weapon w ON p.weapon_id = w.weapon_id '
                    'JOIN Trinket t ON p.trinket_id = t.trinket_id'
                ).fetchall()
                return render_template('charpage/charlist.html', characters=characters)

            except db.IntegrityError:
                error = f"The {charname} armor is already registered in the database."

        flash(error)

    return render_template('charpage/character.html', players=players, armors=armors, weapons=weapons,
                           trinkets=trinkets)


@bp.route('/update_character', methods=['GET', 'POST'])
def update_character():
    db = get_db()
    armors = db.execute('SELECT armor_id, armor_name FROM Armor').fetchall()
    weapons = db.execute('SELECT weapon_id, weapon_name FROM Weapon').fetchall()
    trinkets = db.execute('SELECT trinket_id, trinket_name FROM Trinket').fetchall()

    if request.method == 'POST':
        # Handle form submission for updating character's equipment
        character_id = request.form['char_id']
        armor_id = request.form['armor_id']
        weapon_id = request.form['weapon_id']
        trinket_id = request.form['trinket_id']

        db.execute(
            "UPDATE Personnage SET armor_id = ?, weapon_id = ?, trinket_id = ? WHERE char_id = ?",
            (armor_id, weapon_id, trinket_id, character_id)
        )
        db.commit()

        flash('Character equipment updated successfully!')
        return redirect(url_for('character.character_creation'))  # Redirect to character list page after update

    # Render update character form page
    characters = db.execute(
        'SELECT p.char_id, p.char_name, p.char_class, p.char_level, p.char_hit_points, '
        'u.username as username, a.armor_name as armor, w.weapon_name as weapon, t.trinket_name as trinket '
        'FROM Personnage p '
        'JOIN user u ON p.player_id = u.id '
        'JOIN Armor a ON p.armor_id = a.armor_id '
        'JOIN Weapon w ON p.weapon_id = w.weapon_id '
        'JOIN Trinket t ON p.trinket_id = t.trinket_id'
    ).fetchall()
    return render_template('charpage/update_character.html', characters=characters, armors=armors, weapons=weapons,
                           trinkets=trinkets)


@bp.route('/delete_character/<int:char_id>', methods=['POST'])
def delete_character(character_id):
    db = get_db()
    db.execute('DELETE FROM Personnage WHERE char_id = ?', (character_id,))
    db.commit()
    flash('Character deleted successfully!')
    return redirect(url_for('character.character_creation'))
