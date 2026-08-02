from app.domain.enums.body_part import BodyPart

unknown_locations = set()

head = ["head"]
chest = ["chest"]
stomach = ["stomach"]
right_arm = ["right_arm", "right hand"]
left_arm = ["left_arm", "left hand"]
left_leg = ["left_leg", "left foot"]
right_leg = ["right_leg", "right foot"]
generic = ["generic", "gear", "other", "unknown"]

LOCATION_MAP = {
    **{name: BodyPart.HEAD for name in head},
    **{name: BodyPart.CHEST for name in chest},
    **{name: BodyPart.STOMACH for name in stomach},
    **{name: BodyPart.RIGHT_ARM for name in right_arm},
    **{name: BodyPart.LEFT_ARM for name in left_arm},
    **{name: BodyPart.LEFT_LEG for name in left_leg},
    **{name: BodyPart.RIGHT_LEG for name in right_leg},
    **{name: BodyPart.BODY for name in generic},
}

def convert_hit_location(location: str) -> BodyPart:
    if location not in LOCATION_MAP:
        if type(location) == str and location:
            unknown_locations.add(location)
        return BodyPart.UNKNOWN
    return LOCATION_MAP[location]

def get_unknown_locations() -> set[str]:
    return unknown_locations
