level_map: list[str] = [
    "HHHHHHHH                                                                                     GGGG                                                                                 TTT                                               ",
    "HHHHHHHH                                                                                     XXXX                                                                                 SSS                                               ",
    "HHHHHHHH                                                   HH                                XXXX                 G                                                   GGTTT       SSS    TTT                    SSSS     SSSS       ",
    "HHHHHHHH                                                   FF                                XXXX     GG      G   X                                                   XXSSS       SS     SSS                   S        S           ",
    "HHHHHHHH                                            H                  HHgGGGG                        XX      X                                                  G    X           SS       S                   S        S           ",
    "HHHHHHHH                                        H   F                  FFDXXXX      GG                                                                        G  X   GX           SST      S                   S   SS   S   SS      ",
    "HHHHHHHH                                        F                  HH  XXXXXXX      XX       GGGG                                                          G  X      XX  TT    TSSSSS    TTS                   S    S   S    S      ",
    "HHHHHHHH             H           HH     HH                         FF                        XXXX                          GGG                          G  X         XX  S     SSSSS     SSS                    SSSS     SSSS       ",
    "HHHHHHHH           HHHHH       FFFF     FF                    HHH                            XXXX                  GGG     XXX                       G  X            XX  S    TSSSSS     SSS                                        ",
    "HHHHHHHH P   HH    HHHHHH                                     FFF                            XXXX   GGG          GGXXX                            G  X               XX  S    SSSSSST      S                                        ",
    "HHHHHHHHHHH  HHH   HHHHHH                              HHH                                   XXXX   XXX    GG    XXXXX                         G  X                  XX  SSSSSSSSSSSS      S                                        ",
    "HHHHHHHHHHHHHHHH   HHHHHH    HHHHHHH           HHH     FFF                                   XXXX          XX                               G  X                     XX                  TTS                                        ",
    "FFFFFFFFFFFFFFFF   FFFFFF    FFFFFFF   FFF     FFF                                           XXXX                                        G  X                        XX                  SSS           TTTTTTTTTTTTTTTTTTTTTT       ",
    "XXXXXXXXXXXXXXXX   XXXXXX    XXXXXXX                                                         XXXX                                     GGGX                           XXXSSSSSSSSSSSSS    SSS           SSSSSSSSSSSSSSSSSSSSSS       ",
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
