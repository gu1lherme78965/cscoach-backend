from pandas import DataFrame

from app.infrastructure.match_assembling.builders.event_builder import EventBuilder
from app.infrastructure.match_assembling.mappers.weapon_mapper import convert_weapon_name
from app.infrastructure.match_assembling.mappers.hit_location_mapper import convert_hit_location
from app.domain.events.player_death_event import PlayerDeathEvent
from app.domain.enums.event_type import EventType

class PlayerDeathEventBuilder(EventBuilder):
    
    EVENT_TYPE = EventType.PLAYER_DEATH

    def build_event(self, event_data: DataFrame) -> list[PlayerDeathEvent]:
        events = list()
        for row in event_data.itertuples(index=False):
            events.append(PlayerDeathEvent(
                tick=row.tick,
                attacker_id=row.attacker_steamid,
                victim_id=row.user_steamid,
                assister_id=row.assister_steamid,

                weapon=convert_weapon_name(row.weapon),
                hit_location=convert_hit_location(row.hitgroup),

                distance=row.distance,
                dmg_health=row.dmg_health,
                dmg_armor=row.dmg_armor,

                attacker_in_air=row.attackerinair,
                attacker_is_blind=row.attackerblind,
                is_blind_assist=row.assistedflash,
                is_noscope=row.noscope,
                is_penetrated=row.penetrated,
                is_through_smoke=row.thrusmoke
            ))
        return events
    