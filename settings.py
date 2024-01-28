level_map: list[str] = [
    "HHHHHHHH                              HHHHHHHHHHHHHHHHHWWWWG                                                           GXXGGGGGGGGGGGGGG         ",
    "HHHHHHHH                              HHHHHHHHHHHHHHHHHBBBBX                                                           GXXXXXXXXXXXXXXXX           ",
    "HHHHHHHH                              FFFFFFFFFFFFFFFFFDXXXX                                                           GGXXXXXXXXXXXXXXX             ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX                                            GGGGGG       GGXXXXXXXXXXXXXXXXX                ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX                                          GGXXXXXXGGG                          ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX                   G                     GXXXXXXXXXXX                          ",
    "HHHHHHHH                              XXXXXXXXXXXXXXXXXXXXXX            GGGG                        GXXXXXXXXXXXX    GGGGGGGGGGGGGGGGGGG              ",
    "HHHHHHHH             H           HH                                                               GGXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXX              ",
    "HHHHHHHH           HHHHHH      HHHH                             GGGG                         GGGGGX     XXXXXXXXX    XXXXXXXXXXXXXXXXXXX              ",
    "HHHHHHHHP     HH   HHH                HHHHHHHHHHHHHHHHHgGGGGGGGGXXXX                   GGGGGGXXXXXXWWWWWXXXXXXXXX    XXXXXXXXXXXXXXXXXXX              ",
    "HHHHHHHHHHH  HHH   HHH                HHHHHHHHHHHHHHHHHMXXXXXXXXXXXX         GGGGG     XXXXXXXXXXXXXBBBBXXXXXXXXX    XXXXXXXXXXXXXXXXXXX              ",
    "HHHHHHHHHHHHHHHH   HHHHHH    HHHHHHH  HHHHHHHHHHHHHHHHHMXXXXXXXXXXXX         XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXX              ",
    "FFFFFFFFFFFFFFFF   FFFFFF    FFFFFFF  FFFFFFFFFFFFFFFFFDXXXXXXXXXXXX         XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXX             ",
    "XXXXXXXXXXXXXXXX   XXXXXX    XXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXX              ",
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
