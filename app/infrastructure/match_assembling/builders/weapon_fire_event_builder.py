from pandas import DataFrame

from app.infrastructure.match_assembling.builders.event_builder import EventBuilder
from app.infrastructure.match_assembling.mappers.weapon_mapper import convert_weapon_name
from app.domain.events.weapon_fire_event import WeaponFireEvent
from app.domain.enums.event_type import EventType

class WeaponFireEventBuilder(EventBuilder):

    EVENT_TYPE = EventType.WEAPON_FIRE

    def build_event(self, event_data: DataFrame) -> list[WeaponFireEvent]:
        events = list()
        for row in event_data.itertuples(index=False):
            events.append(WeaponFireEvent(
                tick=row.tick,
                user_id=row.user_steamid,

                weapon=convert_weapon_name(row.weapon),
                is_silenced=row.silenced,

                user_x=row.user_X,
                user_y=row.user_Y,
                user_z=row.user_Z,
                user_pitch=row.user_pitch,
                user_yaw=row.user_yaw
            ))
        return events
    