from app.domain.enums.maps import Map

unknown_maps = set()

mirage = ["de_mirage"]

MAP_MAP = {
    **{name: Map.MIRAGE for name in mirage}
}

def convert_map_name(name: str) -> Map:
    if name not in MAP_MAP:
        if type(name) == str and name:
            unknown_maps.add(name)
        return Map.UNKNOWN
    return MAP_MAP[name]

def get_unknown_maps() -> set[str]:
    return unknown_maps
