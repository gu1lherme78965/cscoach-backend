### Player
- Steamid
- Name
- Team Number

### Utility
- Grenade Type
- Grenade Entity id
- x
- y
- z
- tick
- steamid
- name

### Game events
- [Other Death](#other-death)
- [Bomb Pickup](#bomb-pickup)
- smokegrenade detonate
- bomb dropped
- weapon fire
- bomb planted
- cs win panel match
- player disconnect
- hegrenade detonate
- item equip
- announce phase end
- round officially ended
- player team
- round poststart
- bomb exploded
- server cvar
- smokegrenade expired
- hltv versioninfo
- begin new match
- player spawn
- cs round start beep
- round freeze end
- weapon reload
- inferno startburn
- rank update
- buytime ended
- item pickup
- bullet damage
- bomb beginplant
- round announce match point
- player footstep
- player bullet hit
- round prestart
- round announce last round half
- cs pre restart
- round annouce match start
- cs round final beep
- fire bullets
- player blind
- player hurt
- player death
- bomb begindefuse
- chat message
- inferno expire
- weapon zoom
- flashbang detonate

#### Other Death
*nothing*

#### Bomb Pickup
- tick
- user_name
- user_steamid

#### Smokegrenade Detonate~
- entityid
- tick
- user_name
- user_steamid
- x
- y
- z

#### Bomb Dropped
- entindex
- tick
- user_name
- user_steamid

#### Weapon Fire
- silenced
- tick
- user_name
- user_steamid
- weapon

#### Bomb Planted
- c4
- site
- tick
- user_name
- user_steamid

#### Cs Win Panel Match
- tick

#### player disconnect
- PlayerID
- ever_fully_connected
- name
- networkid
- reason
- tick
- user_name
- user_steamid
- xuid

#### hegrenade detonate
- entityid
- tick
- user_name
- user_steamid
- x
- y
- z

#### item equip
- canzoom
- defindex
- hassilencer
- hastracers
- ispainted
- issilenced
- item
- tick
- user_name
- user_steamid
- weptype

#### announce phase end
- tick

#### round officially ended
- tick

#### player team
- diconnect
- isbot
- oldteam
- silent
- team
- tick
- user_name
- user_steamid

#### round poststart
- tick

#### bomb exploded
- c4
- site
- tick
- user_name
- user_steamid

#### server cvar
- name
- tick
- value

#### smokegrenade expired
*nothing*

#### hltv versioninfo
- tick
- version

#### begin new match
- tick

#### player spawn
- tick
- user_name
- user_steamid

#### cs round start beep
- tick

#### round freeze end
- tick

#### weapon reload
- tick
- user_name
- user_steamid

#### inferno startburn
- entityid
- tick
- user_name
- user_steamid
- x
- y
- z

#### rank update
- num_wins
- rank_change
- rank_new
- rank_old
- rank_type_id
- tick
- user_name
- user_steamid

#### buytime ended
- tick

#### item pickup
- defindex
- item
- silent
- tick
- user_name
- user_steamid

#### bullet damage
- aim_punch_x
- aim_punch_y
- aim_punch_z
- attack_tick_count
- attack_tick_frac
- attacker_name
- attacker_steamid
- damage_dir_x
- damage_dir_y
- damage_dir_z
- distance
- in_air
- inaccuracy_air
- inaccuracy_move
- inaccuracy_total
- no_scope
- num_penetrations
- recoil_index
- render_tick_count
- render_tick_frac
- shoot_ang_x
- shoot_ang_y
- shoot_ang_z
- tick
- type
- victim_name
- victim_steamid

#### bomb beginplant
- site
- tick
- user_name
- user_steamid

#### round announce match point
- tick

#### player footstep
- tick
- user_name
- user_steamid

#### player bullet hit
- attacker_slot
- damage
- hit_group
- is_kill
- penetration_count
- round
- tick
- victim_pos_x
- victim_pos_y
- victim_pos_z
- victim_slot

#### round prestart
- tick

#### round announce last round half
- tick

#### cs pre restart
- tick

#### round annouce match start
- tick

#### cs round final beep
- tick

#### fire bullets
- angles_x
- angles_y
- angles_z
- attack_type
- ent_origin_x
- ent_origin_y
- ent_origin_z
- innaccuracy
- item_def_index
- mode
- num_bullets_remaining
- origin_x
- origin_y
- origin_z
- player
- player_inair
- player_scoped
- recoil_index
- round
- seed
- sound_dsp_effect
- sound_type
- spread
- tick
- user_name
- user_steamid
- weapon_id

#### player blind
- attacker_name
- attacker_steamid
- blind_duration
- entityid
- tick
- user_name
- user_steamid

#### player hurt
- armor
- attacker_name
- attacker_steamid
- dmg_armor
- dmg_health
- health
- hitgroup
- tick
- user_name
- user_steamid
- weapon

#### player death
- assistedflash
- assister_name
- assister_steamid
- attacker_name
- attacker_steamid
- attacekrblind
- attackerinair
- distance
- dmg_armor
- dmg_health
- dominated
- headshot
- hitgroup
- noreplay
- noscope
- penetrated
- revenge
- thrusmoke
- tick
- user_name
- user_steamid
- weapon
- weapon_fauxitemid
- weapon_itemid
- weapon_originamowner_xuid
- wipe

#### bomb begindefuse
- haskit
- tick
- user_name
- user_steamid

#### chat message
- chat_message
- tick
- user_name
- user_steamid

#### inferno expire
- entityid
- tick
- user_name
- user_steamid
- x
- y
- z

#### weapon zoom
- tick
- user_name
- user_steamid

#### flashbang detonate
- entityid
- tick
- user_name
- user_steamid
- x
- y
- z