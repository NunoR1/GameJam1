# Weapons
weapon_oldsword = {"name":"Old Sword", "attack":3, "gold_value":5, "type":"weapon", "magic_mod":1}
weapon_goodsword = {"name":"Sword", "attack":6, "gold_value":12, "type":"weapon", "magic_mod":1}
weapon_staff = {"name":"Staff", "attack":3, "gold_value":30, "type":"weapon", "magic_mod":2.5}
weapon_axe = {"name":"Axe", "attack":8, "gold_value":18, "type":"weapon", "magic_mod":0.8}
weapon_spear = {"name":"Spear", "attack":7, "gold_value":15, "type":"weapon", "magic_mod":1}
weapon_greatsword = {"name":"Greatsword", "attack":10, "gold_value":30, "type":"weapon", "magic_mod":0.5}
weapon_magicsword = {"name":"Magic Sword", "attack":7, "gold_value":30, "type":"weapon", "magic_mod":1.75}

weapons = {"Old Sword":weapon_oldsword, "Sword":weapon_goodsword, "Staff":weapon_staff, "Axe":weapon_axe, "Spear":weapon_spear, "Greatsword":weapon_greatsword, "Magic Sword":weapon_magicsword}

# Armor
armor_cloth = {"name":"Cloth Armor", "hp_buff": 5, "gold_value":5, "type":"armor"}
armor_leather = {"name":"Leather Armor", "hp_buff": 10, "gold_value":15, "type":"armor"}
armor_tabard = {"name":"Tabard", "hp_buff": 20, "gold_value":25, "type":"armor"}
armor_mail = {"name":"Mail Armor", "hp_buff": 35, "gold_value":40, "type":"armor"}

armors = {"Cloth Armor":armor_cloth, "Leather Armor":armor_leather, "Tabard":armor_tabard, "Mail Armor":armor_mail}

# Shields
shield_plank = {"name":"Plank Shield", "hp_buff": 5, "gold_value":7, "type":"shield"}
shield_round = {"name":"Round Shield", "hp_buff": 10, "gold_value":15, "type":"shield"}
shield_tower = {"name":"Tower Shield", "hp_buff": 20, "gold_value":25, "type":"shield"}

shields = {"Plank Shield":shield_plank, "Round Shield":shield_round, "Tower Shield":shield_tower}

# Spellbooks
spell_book = {"name":"Spellbook", "offense_spell_name":"Blast", "offense_spell_damage":6, "offense_spell_cost":3, "defense_spell_name":"Heal", "defense_spell_healing":4, "defense_spell_cost": 3, "gold_value":30, "type":"spellbook"}

books = {"Spellbook":spell_book}

Offhand = {"Plank Shield":shield_plank, "Round Shield":shield_round, "Tower Shield":shield_tower, "Spellbook":spell_book}

# Consumables

item_healpotion = {"name":"Healing Potion", "effect":"health_restore", "strength":10, "is_magic": False, "gold_value":8, "type":"consumable"}
item_manapotion = {"name":"Mana Potion", "effect":"mana_restore", "strength":10, "is_magic": False, "gold_value":8, "type":"consumable"}
item_lightningWand = {"name":"Wand of Lightnging", "effect":"damage", "strength":10, "is_magic": True, "gold_value":16, "type":"consumable"}
item_crossbow = {"name":"Crossbow", "effect":"damage", "strength":12, "is_magic": False, "gold_value":14, "type":"consumable"}

consumables = {"Healing Potion":item_healpotion, "Mana Potion":item_manapotion, "Lightning Wand":item_lightningWand, "Crossbow":item_crossbow}