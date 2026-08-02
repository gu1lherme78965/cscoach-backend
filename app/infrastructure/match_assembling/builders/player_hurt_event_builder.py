from pandas import DataFrame

from app.infrastructure.match_assembling.builders.event_builder import EventBuilder
from app.infrastructure.match_assembling.mappers.weapon_mapper import convert_weapon_name
from app.infrastructure.match_assembling.mappers.hit_location_mapper import convert_hit_location
from app.domain.events.player_hurt_event import PlayerHurtEvent
from app.domain.enums.event_type import EventType

class PlayerHurtEventBuilder(EventBuilder):
    EVENT_TYPE = EventType.PLAYER_HURT

    def build_event(self, event_data: DataFrame) -> list[PlayerHurtEvent]:
        events = list()
        for row in event_data.itertuples(index=False):
            events.append(PlayerHurtEvent(
                tick=row.tick,
                attacker_id=row.attacker_steamid,
                victim_id=row.user_steamid,
                weapon=convert_weapon_name(row.weapon),
                hit_location=convert_hit_location(row.hitgroup),
                dmg_health=row.dmg_health,
                dmg_armor=row.dmg_armor,
                remaining_health=row.health,
                remaining_armor=row.armor
            ))
        return events
    