"""A few dictionaries used to translate raw memory reads into displayable data"""


# This is the characters internal ID, converted to decimal
CHARACTERS = {
    0:	'Mario',
    1:	'Fox',
    2:	'Captain Falcon',
    3:	'Donkey Kong',
    4:	'Kirby',
    5:	'Bowser',
    6:	'Link',
    7:	'Sheik',
    8:	'Ness',
    9:	'Peach',
    10:	'Popo',
    11:	'Nana',
    12:	'Pikachu',
    13:	'Samus',
    14:	'Yoshi',
    15:	'Jigglypuff',
    16:	'Mewtwo',
    17:	'Luigi',
    18:	'Marth',
    19:	'Zelda',
    20:	'Young Link',
    21:	'Dr. Mario',
    22:	'Falco',
    23:	'Pichu',
    24:	'Mr. Game & Watch',
    25:	'Ganondorf',
    26:	'Roy',
    27:	'Master Hand',
    28:	'Crazy Hand',
    29:	'Wireframe Male',
    30:	'Wireframe Female',
    31:	'Giga Bowser',
    32:	'Sandbag'
}

# I'm not sure whether to use internal or external ID here, this is internal
STAGES = {
    2:    'Princess Peach\'s Castle',
    3:    'Rainbow Cruise',
    4:    'Kongo Jungle',
    5:    'Jungle Japes',
    6:    'Great Bay',
    7:    'Hyrule Temple',
    8:    'Brinstar',
    9:    'Brinstar Depths',
    10:   'Yoshi\'s Story',
    11:   'Yoshi\'s Island',
    12:   'Fountain of Dreams',
    13:   'Green Greens',
    14:   'Corneria',
    15:   'Venom',
    16:   'Pokemon Stadium',
    17:   'Poke Floats',
    18:   'Mute City',
    19:   'Big Blue',
    20:   'Onett',
    21:   'Fourside',
    22:   'Icicle Mountain',
    24:   'Mushroom Kingdom',
    25:   'Mushroom Kingdom II',
    27:   'Flat Zone',
    28:   'Dream Land',
    29:   'Yoshi\'s Island (64)',
    30:   'Kongo Jungle (64)',
    36:   'Battlefield',
    37:   'Final Destination'
}

# list of in game action states by ID (using decimal ID)
# TODO: Create module to fix ID matching past 0x155
ACTIONSTATES = {
    0:	    'DeadDown',
    1:	    'DeadLeft',
    2:	    'DeadRight',
    3:	    'DeadUp',
    4:	    'DeadUpStar',
    5:	    'DeadUpStarIce',
    6:	    'DeadUpFall',
    7:	    'DeadUpFallHitCamera',
    8:	    'DeadUpFallHitCameraFlat',
    9:	    'DeadUpFallIce',
    10:	    'DeadUpFallHitCameraIce',
    11:	    'Sleep',
    12:	    'Rebirth',
    13:	    'RebirthWait',
    14:	    'Wait',
    15:	    'WalkSlow',
    16:	    'WalkMiddle',
    17:	    'WalkFast',
    18:	    'Turn',
    19:	    'TurnRun',
    20:	    'Dash',
    21:	    'Run',
    22:	    'RunDirect',
    23:	    'RunBrake',
    24:	    'KneeBend',
    25:	    'JumpF',
    26:	    'JumpB',
    27:	    'JumpAerialF',
    28:	    'JumpAerialB',
    29:	    'Fall',
    30:	    'FallF',
    31:	    'FallB',
    32:	    'FallAerial',
    33:	    'FallAerialF',
    34:	    'FallAerialB',
    35:	    'FallSpecial',
    36:	    'FallSpecialF',
    37:	    'FallSpecialB',
    38:	    'DamageFall',
    39:	    'Squat',
    40:	    'SquatWait',
    41:	    'SquatRv',
    42:	    'Landing',
    43:	    'LandingFallSpecial',
    44:	    'Attack11',
    45:	    'Attack12',
    46:	    'Attack13',
    47:	    'Attack100Start',
    48:	    'Attack100Loop',
    49:	    'Attack100End',
    50:	    'AttackDash',
    51:	    'AttackS3Hi',
    52:	    'AttackS3HiS',
    53:	    'AttackS3S',
    54:	    'AttackS3LwS',
    55:	    'AttackS3Lw',
    56:	    'AttackHi3',
    57:	    'AttackLw3',
    58:	    'AttackS4Hi',
    59:	    'AttackS4HiS',
    60:	    'AttackS4S',
    61:	    'AttackS4LwS',
    62:	    'AttackS4Lw',
    63:	    'AttackHi4',
    64:	    'AttackLw4',
    65:	    'AttackAirN',
    66:	    'AttackAirF',
    67:	    'AttackAirB',
    68:	    'AttackAirHi',
    69:	    'AttackAirLw',
    70:	    'LandingAirN',
    71:	    'LandingAirF',
    72:	    'LandingAirB',
    73:	    'LandingAirHi',
    74:	    'LandingAirLw',
    75:	    'DamageHi1',
    76:	    'DamageHi2',
    77:	    'DamageHi3',
    78:	    'DamageN1',
    79:	    'DamageN2',
    80:	    'DamageN3',
    81:	    'DamageLw1',
    82:	    'DamageLw2',
    83:	    'DamageLw3',
    84:	    'DamageAir1',
    85:	    'DamageAir2',
    86:	    'DamageAir3',
    87:	    'DamageFlyHi',
    88:	    'DamageFlyN',
    89:	    'DamageFlyLw',
    90:	    'DamageFlyTop',
    91:	    'DamageFlyRoll',
    92:	    'LightGet',
    93:	    'HeavyGet',
    94:	    'LightThrowF',
    95:	    'LightThrowB',
    96:	    'LightThrowHi',
    97:	    'LightThrowLw',
    98:	    'LightThrowDash',
    99:	    'LightThrowDrop',
    100:	'LightThrowAirF',
    101:	'LightThrowAirB',
    102:	'LightThrowAirHi',
    103:	'LightThrowAirLw',
    104:	'HeavyThrowF',
    105:	'HeavyThrowB',
    106:	'HeavyThrowHi',
    107:	'HeavyThrowLw',
    108:	'LightThrowF4',
    109:	'LightThrowB4',
    110:	'LightThrowHi4',
    111:	'LightThrowLw4',
    112:	'LightThrowAirF4',
    113:	'LightThrowAirB4',
    114:	'LightThrowAirHi4',
    115:	'LightThrowAirLw4',
    116:	'HeavyThrowF4',
    117:	'HeavyThrowB4',
    118:	'HeavyThrowHi4',
    119:	'HeavyThrowLw4',
    120:	'SwordSwing1',
    121:	'SwordSwing3',
    122:	'SwordSwing4',
    123:	'SwordSwingDash',
    124:	'BatSwing1',
    125:	'BatSwing3',
    126:	'BatSwing4',
    127:	'BatSwingDash',
    128:	'ParasolSwing1',
    129:	'ParasolSwing3',
    130:	'ParasolSwing4',
    131:	'ParasolSwingDash',
    132:	'HarisenSwing1',
    133:	'HarisenSwing3',
    134:	'HarisenSwing4',
    135:	'HarisenSwingDash',
    136:	'StarRodSwing1',
    137:	'StarRodSwing3',
    138:	'StarRodSwing4',
    139:	'StarRodSwingDash',
    140:	'LipStickSwing1',
    141:	'LipStickSwing3',
    142:	'LipStickSwing4',
    143:	'LipStickSwingDash',
    144:	'ItemParasolOpen',
    145:	'ItemParasolFall',
    146:	'ItemParasolFallSpecial',
    147:	'ItemParasolDamageFall',
    148:	'LGunShoot',
    149:	'LGunShootAir',
    150:	'LGunShootEmpty',
    151:	'LGunShootAirEmpty',
    152:	'FireFlowerShoot',
    153:	'FireFlowerShootAir',
    154:	'ItemScrew',
    155:	'ItemScrewAir',
    156:	'DamageScrew',
    157:	' DamageScrewAir',
    158:	'ItemScopeStart',
    159:	'ItemScopeRapid',
    160:	'ItemScopeFire',
    161:	'ItemScopeEnd',
    162:	'ItemScopeAirStart',
    163:	'ItemScopeAirRapid',
    164:	'ItemScopeAirFire',
    165:	'ItemScopeAirEnd',
    166:	'ItemScopeStartEmpty',
    167:	'ItemScopeRapidEmpty',
    168:	'ItemScopeFireEmpty',
    169:	'ItemScopeEndEmpty',
    170:	'ItemScopeAirStartEmpty',
    171:	'ItemScopeAirRapidEmpty',
    172:	'ItemScopeAirFireEmpty',
    173:	'ItemScopeAirEndEmpty',
    174:	'LiftWait',
    175:	'LiftWalk1',
    176:	'LiftWalk2',
    177:	'LiftTurn',
    178:	'GuardOn',
    179:	'Guard',
    180:	'GuardOff',
    181:	'GuardSetOff',
    182:	'GuardReflect',
    183:	'DownBoundU',
    184:	'DownWaitU',
    185:	'DownDamageU',
    186:	'DownStandU',
    187:	'DownAttackU',
    188:	'DownFowardU',
    189:	'DownBackU',
    190:	'DownSpotU',
    191:	'DownBoundD',
    192:	'DownWaitD',
    193:	'DownDamageD',
    194:	'DownStandD',
    195:	'DownAttackD',
    196:	'DownFowardD',
    197:	'DownBackD',
    198:	'DownSpotD',
    199:	'Passive',
    200:	'PassiveStandF',
    201:	'PassiveStandB',
    202:	'PassiveWall',
    203:	'PassiveWallJump',
    204:	'PassiveCeil',
    205:	'ShieldBreakFly',
    206:	'ShieldBreakFall',
    207:	'ShieldBreakDownU',
    208:	'ShieldBreakDownD',
    209:	'ShieldBreakStandU',
    210:	'ShieldBreakStandD',
    211:	'FuraFura',
    212:	'Catch',
    213:	'CatchPull',
    214:	'CatchDash',
    215:	'CatchDashPull',
    216:	'CatchWait',
    217:	'CatchAttack',
    218:	'CatchCut',
    219:	'ThrowF',
    220:	'ThrowB',
    221:	'ThrowHi',
    222:	'ThrowLw',
    223:	'CapturePulledHi',
    224:	'CaptureWaitHi',
    225:	'CaptureDamageHi',
    226:	'CapturePulledLw',
    227:	'CaptureWaitLw',
    228:	'CaptureDamageLw',
    229:	'CaptureCut',
    230:	'CaptureJump',
    231:	'CaptureNeck',
    232:	'CaptureFoot',
    233:	'EscapeF',
    234:	'EscapeB',
    235:	'Escape',
    236:	'EscapeAir',
    237:	'ReboundStop',
    238:	'Rebound',
    239:	'ThrownF',
    240:	'ThrownB',
    241:	'ThrownHi',
    242:	'ThrownLw',
    243:	'ThrownLwWomen',
    244:	'Pass',
    245:	'Ottotto',
    246:	'OttottoWait',
    247:	'FlyReflectWall',
    248:	'FlyReflectCeil',
    249:	'StopWall',
    250:	'StopCeil',
    251:	'MissFoot',
    252:	'CliffCatch',
    253:	'CliffWait',
    254:	'CliffClimbSlow',
    255:	'CliffClimbQuick',
    256:	'CliffAttackSlow',
    257:	'CliffAttackQuick',
    258:	'CliffEscapeSlow',
    259:	'CliffEscapeQuick',
    260:	'CliffJumpSlow1',
    261:	'CliffJumpSlow2',
    262:	'CliffJumpQuick1',
    263:	'CliffJumpQuick2',
    264:	'AppealR',
    265:	'AppealL',
    266:	'ShoulderedWait',
    267:	'ShoulderedWalkSlow',
    268:	'ShoulderedWalkMiddle',
    269:	'ShoulderedWalkFast',
    270:	'ShoulderedTurn',
    271:	'ThrownFF',
    272:	'ThrownFB',
    273:	'ThrownFHi',
    274:	'ThrownFLw',
    275:	'CaptureCaptain',
    276:	'CaptureYoshi',
    277:	'YoshiEgg',
    278:	'CaptureKoopa',
    279:	'CaptureDamageKoopa',
    280:	'CaptureWaitKoopa',
    281:	'ThrownKoopaF',
    282:	'ThrownKoopaB',
    283:	'CaptureKoopaAir',
    284:	'CaptureDamageKoopaAir',
    285:	'CaptureWaitKoopaAir',
    286:	'ThrownKoopaAirF',
    287:	'ThrownKoopaAirB',
    288:	'CaptureKirby',
    289:	'CaptureWaitKirby',
    290:	'ThrownKirbyStar',
    291:	'ThrownCopyStar',
    292:	'ThrownKirby',
    293:	'BarrelWait',
    294:	'Bury',
    295:	'BuryWait',
    296:	'BuryJump',
    297:	'DamageSong',
    298:	'DamageSongWait',
    299:	'DamageSongRv',
    300:	'DamageBind',
    301:	'CaptureMewtwo',
    302:	'CaptureMewtwoAir',
    303:	'ThrownMewtwo',
    304:	'ThrownMewtwoAir',
    305:	'WarpStarJump',
    306:	'WarpStarFall',
    307:	'HammerWait',
    308:	'HammerWalk',
    309:	'HammerTurn',
    310:	'HammerKneeBend',
    311:	'HammerFall',
    312:	'HammerJump',
    313:	'HammerLanding',
    314:	'KinokoGiantStart',
    315:	'KinokoGiantStartAir',
    316:	'KinokoGiantEnd',
    317:	'KinokoGiantEndAir',
    318:	'KinokoSmallStart',
    319:	'KinokoSmallStartAir',
    320:	'KinokoSmallEnd',
    321:	'KinokoSmallEndAir',
    322:	'Entry',
    323:	'EntryStart',
    324:	'EntryEnd',
    325:	'DamageIce',
    326:	'DamageIceJump',
    327:	'CaptureMasterhand',
    328:	'CapturedamageMasterhand',
    329:	'CapturewaitMasterhand',
    330:	'ThrownMasterhand',
    331:	'CaptureKirbyYoshi',
    332:	'KirbyYoshiEgg',
    333:	'CaptureLeadead',
    334:	'CaptureLikelike',
    335:	'DownReflect',
    336:	'CaptureCrazyhand',
    337:	'CapturedamageCrazyhand',
    338:	'CapturewaitCrazyhand',
    339:	'ThrownCrazyhand',
    340:	'BarrelCannonWait',
    341:	'Wait1',
    342:	'Wait2',
    343:	'Wait3',
    344:	'Wait4',
    345:	'WaitItem',
    346:	'SquatWait1',
    347:	'SquatWait2',
    348:	'SquatWaitItem',
    349:	'GuardDamage',
    350:	'EscapeN',
    351:	'AttackS4Hold',
    352:	'HeavyWalk1',
    353:	'HeavyWalk2',
    354:	'ItemHammerWait',
    355:	'ItemHammerMove',
    356:	'ItemBlind',
    357:	'DamageElec',
    358:	'FuraSleepStart',
    359:	'FuraSleepLoop',
    360:	'FuraSleepEnd',
    361:	'WallDamage',
    362:	'CliffWait1',
    363:	'CliffWait2',
    364:	'SlipDown',
    365:	'Slip',
    366:	'SlipTurn',
    367:	'SlipDash',
    368:	'SlipWait',
    369:	'SlipStand',
    370:	'SlipAttack',
    371:	'SlipEscapeF',
    372:	'SlipEscapeB',
    373:	'AppealS',
    374:	'Zitabata',
    375:	'CaptureKoopaHit',
    376:	'ThrownKoopaEndF',
    377:	'ThrownKoopaEndB',
    378:	'CaptureKoopaAirHit',
    379:	'ThrownKoopaAirEndF',
    380:	'ThrownKoopaAirEndB',
    381:	'ThrownKirbyDrinkSShot',
    382:	'ThrownKirbySpitSShot',
}

# table of stage dimensions via Kadano
# Name	<- bound | -> bound | upper bound | lower bound
# YS	-175.70    173.60	 168.00	   -91.00
# FD	-246.00    246.00    188.00	   -140.00
# FoD	-198.75    198.75	 202.50	   -146.25
# DL64	-255.00    255.00	 250.00	   -123.00
# BF	-224.00    224.00	 200.00	   -108.80
# PS	-230.00	   230.00    180.00	   -111.00
# --------------------------------------------
# Name  side plat	top plat    ledge l	    ledge r
# YS    23.45   	42.00   	-56.00  	56.00
# FD    0.00    	0.00	    -85.56  	85.56
# FoD   27.38   	42.75   	-63.35  	63.35
# DL64  30.24     	51.43   	-77.27  	77.27
# BF    27.20   	54.40   	-68.40  	68.40
# #PS   25.00       0.00    	-87.75  	87.75

STAGES = {
    'YS': {
        'blast-l': -175.70,
        'blast-r': 173.60,
        'blast-u': 168.00,
        'blast-d': -91.00,
        'sidePlat': 23.45,
        'topPlat': 42.00,
        'ledge-l': -56.00,
        'ledge-r': 56.00
    },

    'FD': {
        'blast-l': -246.00,
        'blast-r': 246.00,
        'blast-u': 188.00,
        'blast-d': -140.00,
        'sidePlat': 0.00,
        'topPlat': 0.00,
        'ledge-l': -85.56,
        'ledge-r': 85.56
    },

    'FoD': {
        'blast-l': -198.75,
        'blast-r': 198.75,
        'blast-u': 202.50,
        'blast-d': -146.25,
        'sidePlat': 27.38,
        'topPlat': 42.75,
        'ledge-l': -63.35,
        'ledge-r': 63.35
    },

    'DL64': {
        'blast-l': -255.00,
        'blast-r': 255.00,
        'blast-u': 250.00,
        'blast-d': -123.00,
        'sidePlat': 30.24,
        'topPlat': 51.43,
        'ledge-l': -77.27,
        'ledge-r': 77.27
    },

    'BF': {
        'blast-l': -224.00,
        'blast-r': 224.00,
        'blast-u': 200.00,
        'blast-d': -108.80,
        'sidePlat': 27.20,
        'topPlat': 54.40,
        'ledge-l': -68.40,
        'ledge-r': 68.40
    },

    'PS': {
        'blast-l': -230.00,
        'blast-r': 230.00,
        'blast-u': 180.00,
        'blast-d': -111.00,
        'sidePlat': 25.00,
        'topPlat': 0.00,
        'ledge-l': -87.75,
        'ledge-r': 87.75
    },
}
