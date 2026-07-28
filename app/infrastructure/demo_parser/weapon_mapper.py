from app.domain.enums.weapons import Weapon

unknown_weapons = set()

ak47 = ["ak47", "weapon_ak47"]
awp = ["awp", "weapon_awp"]
bowie_knife = ["Bowie Knife"]
c4 = ["planted_c4"]
cz75_auto = ["CZ75-Auto"]
desert_eagle = ["deagle", "weapon_deagle"]
dual_berettas = ["weapon_elite"]
famas = ["famas", "weapon_famas"]
five_seven = ["fiveseven", "weapon_fiveseven"]
flashbang = ["flashbang", "weapon_flashbang"]
galil_ar = ["galilar", "weapon_galilar"]
glock_18 = ["glock", "weapon_glock"]
he_grenade = ["hegrenade", "weapon_hegrenade"]
incendiary_grenade = ["Incendiary Grenade", "weapon_incgrenade", "inferno"]
knifes = ["knife", "knife_t", "weapon_knife_t", "weapon_knife"]
m4a1_s = ["m4a1_silencer", "weapon_m4a1_silencer"]
m4a4 = ["m4a1", "weapon_m4a1"]
mag_7 = ["mag7", "weapon_mag7"]
mp5_sd = ["mp5sd", "weapon_mp5sd"]
mp7 = ["mp7", "weapon_mp7"]
mp9 = ["mp9"]
molotov = ["molotov", "weapon_molotov"]
nova = ["nova", "weapon_nova"]
p2000 = ["hkp2000"]
p250 = ["p250", "weapon_p250"]
p90 = ["p90", "weapon_p90"]
r8_revolver =["revolver", "weapon_revolver"]
sawed_off = ["sawedoff", "weapon_sawedoff"]
sg_553 = ["sg556", "weapon_sg556"]
smoke_grenade = ["Smoke Grenade", "weapon_smokegrenade"]
ssg_08 = ["ssg08", "weapon_ssg08"]
usp_s = ["usp_silencer", "weapon_usp_silencer"]
xm1014 = ["xm1014", "weapon_xm1014"]
zeus_x27 =["Zeus x27"]

WEAPON_MAP = {
    **{name: Weapon.AK_47 for name in ak47},
    **{name: Weapon.AWP for name in awp},
    **{name: Weapon.BOWIE_KNIFE for name in bowie_knife},
    **{name: Weapon.C4_EXPLOSIVE for name in c4},
    **{name: Weapon.CZ75_AUTO for name in cz75_auto},
    **{name: Weapon.DESERT_EAGLE for name in desert_eagle},
    **{name: Weapon.DUAL_BERETTAS for name in dual_berettas},
    **{name: Weapon.FAMAS for name in famas},
    **{name: Weapon.FIVE_SEVEN for name in five_seven},
    **{name: Weapon.FLASHBANG for name in flashbang},
    **{name: Weapon.GALIL_AR for name in galil_ar},
    **{name: Weapon.GLOCK_18 for name in glock_18},
    **{name: Weapon.HE_GRENADE for name in he_grenade},
    **{name: Weapon.INCENDIARY_GRENADE for name in incendiary_grenade},
    **{name: Weapon.KNIFE for name in knifes},
    **{name: Weapon.M4A1_S for name in m4a1_s},
    **{name: Weapon.M4A4 for name in m4a4},
    **{name: Weapon.MAG_7 for name in mag_7},
    **{name: Weapon.MP5_SD for name in mp5_sd},
    **{name: Weapon.MP7 for name in mp7},
    **{name: Weapon.MP9 for name in mp9},
    **{name: Weapon.MOLOTOV for name in molotov},
    **{name: Weapon.NOVA for name in nova},
    **{name: Weapon.P2000 for name in p2000},
    **{name: Weapon.P250 for name in p250},
    **{name: Weapon.P90 for name in p90},
    **{name: Weapon.R8_REVOLVER for name in r8_revolver},
    **{name: Weapon.SAWED_OFF for name in sawed_off},
    **{name: Weapon.SG_553 for name in sg_553},
    **{name: Weapon.SMOKE_GRENADE for name in smoke_grenade},
    **{name: Weapon.SSG_08 for name in ssg_08},
    **{name: Weapon.USP_S for name in usp_s},
    **{name: Weapon.XM1014 for name in xm1014},
    **{name: Weapon.ZEUS_X27 for name in zeus_x27}
}

def convert_weapon_name(name: str) -> Weapon:
    if name not in WEAPON_MAP:
        if type(name) == str and name:
            unknown_weapons.add(name)
        return Weapon.UNKNOWN
    return WEAPON_MAP[name]

def get_unknown_weapons() -> set[str]:
    return unknown_weapons
