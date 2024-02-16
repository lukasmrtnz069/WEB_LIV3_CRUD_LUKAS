from flask import (
    Blueprint, flash, render_template
)
from TurnFight.db import get_db

bp = Blueprint('charlist', __name__)  # Use a different name for the blueprint


@bp.route('/charlist')
def charlist():
    db = get_db()
    characters = db.execute(
        'SELECT p.char_name, p.char_class, p.char_level, p.char_hit_points, '
        'u.username as username, a.armor_name as armor, w.weapon_name as weapon, t.trinket_name as trinket '
        'FROM Personnage p '
        'JOIN user u ON p.player_id = u.id '
        'JOIN Armor a ON p.armor_id = a.armor_id '
        'JOIN Weapon w ON p.weapon_id = w.weapon_id '
        'JOIN Trinket t ON p.trinket_id = t.trinket_id'
    ).fetchall()
    return render_template('charpage/charlist.html', characters=characters)
