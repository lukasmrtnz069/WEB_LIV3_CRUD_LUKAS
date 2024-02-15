DROP TABLE IF EXISTS Armor;
DROP TABLE IF EXISTS Weapon;
DROP TABLE IF EXISTS Trinket;
DROP TABLE IF EXISTS Enemy;
DROP TABLE IF EXISTS Personnage;
DROP TABLE IF EXISTS Encounter;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


CREATE TABLE Armor (
    armor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    armor_name TEXT NOT NULL,
    armor_defense INTEGER NOT NULL
);

CREATE TABLE Weapon (
    weapon_id INTEGER PRIMARY KEY AUTOINCREMENT,
    weapon_name TEXT NOT NULL,
    weapon_type TEXT NOT NULL,
    weapon_damage INTEGER NOT NULL
);

CREATE TABLE Trinket (
    trinket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    trinket_name TEXT NOT NULL,
    trinket_wearable_by TEXT NOT NULL,
    trinket_bonus INTEGER NOT NULL
);

CREATE TABLE Enemy (
    enemy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enemy_name TEXT NOT NULL,
    enemy_class TEXT NOT NULL,
    enemy_level INTEGER NOT NULL,
    enemy_hit_points INTEGER NOT NULL,
    enemy_xp_given INTEGER NOT NULL,
    armor_id INTEGER NOT NULL,
    weapon_id INTEGER NOT NULL,
    trinket_id INTEGER NOT NULL,
    FOREIGN KEY (armor_id) REFERENCES Armor(armor_id),
    FOREIGN KEY (weapon_id) REFERENCES Weapon(weapon_id),
    FOREIGN KEY (trinket_id) REFERENCES Trinket(trinket_id)
);

CREATE TABLE Personnage (
    char_id INTEGER PRIMARY KEY AUTOINCREMENT,
    char_name TEXT NOT NULL,
    char_class TEXT NOT NULL,
    char_level INTEGER NOT NULL,
    char_hit_points INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    armor_id INTEGER NOT NULL,
    weapon_id INTEGER NOT NULL,
    trinket_id INTEGER NOT NULL,
    FOREIGN KEY (armor_id) REFERENCES Armor(armor_id),
    FOREIGN KEY (weapon_id) REFERENCES Weapon(weapon_id),
    FOREIGN KEY (trinket_id) REFERENCES Trinket(trinket_id),
    FOREIGN KEY (player_id) REFERENCES user (id)
);

CREATE TABLE Encounter (
    enc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enc_char_id INTEGER NOT NULL,
    enc_enemy_id INTEGER NOT NULL,
    FOREIGN KEY (enc_char_id) REFERENCES Personnage(char_id),
    FOREIGN KEY (enc_enemy_id)  REFERENCES Enemy(enemy_id)
);



