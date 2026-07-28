from app.domain.enums.weapons import Weapon

unknown_weapons = set()

knifes = ["knife", "knife_t"]

WEAPON_MAP = {
    "AK-47": Weapon.AK_47,
    "AWP": Weapon.AWP,
    "Bowie Knife": Weapon.BOWIE_KNIFE,
    "C4 Explosive": Weapon.C4_EXPLOSIVE,
    "CZ75-Auto": Weapon.CZ75_AUTO,
    "Desert Eagle": Weapon.DESERT_EAGLE,
    "Dual Berettas": Weapon.DUAL_BERETTAS,
    "FAMAS": Weapon.FAMAS,
    "Five-SeveN": Weapon.FIVE_SEVEN,
    "Flashbang": Weapon.FLASHBANG,
    "Galil AR": Weapon.GALIL_AR,
    "Glock-18": Weapon.GLOCK_18,
    "High Explosive Grenade": Weapon.HE_GRENADE,
    "Incendiary Grenade": Weapon.INCENDIARY_GRENADE,
    **{name: Weapon.KNIFE for name in knifes},
    "M4A1-S": Weapon.M4A1_S,
    "M4A4": Weapon.M4A4,
    "MAG-7": Weapon.MAG_7,
    "MP5-SD": Weapon.MP5_SD,
    "MP7": Weapon.MP7,
    "MP9": Weapon.MP9,
    "Molotov": Weapon.MOLOTOV,
    "Nova": Weapon.NOVA,
    "P250": Weapon.P250,
    "P90": Weapon.P90,
    "R8 Revolver": Weapon.R8_REVOLVER,
    "Sawed-Off": Weapon.SAWED_OFF,
    "SG 553": Weapon.SG_553,
    "Smoke Grenade": Weapon.SMOKE_GRENADE,
    "SSG 08": Weapon.SSG_08,
    "USP-S": Weapon.USP_S,
    "XM1014": Weapon.XM1014,
    "Zeus x27": Weapon.ZEUS_X27
}

def convert_weapon_name(name: str) -> Weapon:
    if name not in WEAPON_MAP:
        if type(name) == str:
            unknown_weapons.add(name)
        return Weapon.UNKNOWN
    return WEAPON_MAP[name]

def get_unknown_weapons() -> set[str]:
    return unknown_weapons
