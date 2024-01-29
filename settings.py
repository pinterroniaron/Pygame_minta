level_map: list[str] = [
    "HHHHHHHH                              HHHHHHHHHHHHHHHHHWWWWG                                                           GXXGGGGGGGGGGGGGG         ",
    "HHHHHHHH                              HHHHHHHHHHHHHHHHHBBBBX                                                           XXXXXXXXXXXXXXXXX           ",
    "HHHHHHHH                              FFFFFFFFFFFFFFFFFDXXXX                                                           XXXXXXXXXXXXXXXXX             ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX                                            GGGGGG       GGXXXXXXXXXXXXXXXXX                ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX                                          GGXXXXXXGGG                                      ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX                   G                     GXXXXXXXXXXX                                      ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX            GGGG                        GXXXXXXXXXXXX    GGGGGGGGGGGGGGGGGGGTTTTTT                ",
    "HHHHHHHH             H           HH                                                               GGXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS                ",
    "HHHHHHHH           HHHHHH      HHHH                             GGGG                         GGGGGX     XXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS                ",
    "HHHHHHHHP     HH   HHH                HHHHHHHHHHHHHHHHHgGGGGGGGGXXXX                   GGGGGGXXXXXXWWWWWXXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS                ",
    "HHHHHHHHHHH  HHH   HHH                HHHHHHHHHHHHHHHHHMXXXXXXXXXXXX         GGGGG     XXXXXXXXXXXXXBBBBXXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS                ",
    "HHHHHHHHHHHHHHHH   HHHHHH    HHHHHHH  HHHHHHHHHHHHHHHHHMXXXXXXXXXXXX         XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS                ",
    "FFFFFFFFFFFFFFFF   FFFFFF    FFFFFFF  FFFFFFFFFFFFFFFFFDXXXXXXXXXXXX         XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS               ",
    "XXXXXXXXXXXXXXXX   XXXXXX    XXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXSSSSSS              ",
]

#T = sand_top
#S = sand
#G = grass
#X = dirt
#P = player
#H = snow
#F = snow_dirt
#M = melting_snow
#W = water
#B = water_bottom
#D = melting_dirt
#g = melting grass

tile_size = 64
width, height = 1900, len(level_map) * tile_size
