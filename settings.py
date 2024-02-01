level_map: list[str] = [
    "HHHHHHHH                                                                                     GGGG                                                                                 TTT                                      ",
    "HHHHHHHH                                                                                     XXXX                                                                                 SSS                                      ",
    "HHHHHHHH                                                   HH                                XXXX                 G                                                   GGTTT       SSS    TT                                      ",
    "HHHHHHHH                                                   FF                                XXXX     GG      G   X                                                   XXSSS       SS     SS                                           ",
    "HHHHHHHH                                            H                  HHgGGGG                        XX      X                                                  G    X           SS                                             ",
    "HHHHHHHH                                        H   F                  FFDXXXX      GG                                                                        G  X    X           SST                                                   ",
    "HHHHHHHH                                        F                  HH  XXXXXXX      XX       GGGG                                                          G  X       X  TT    TSSSSS    TT                                                 ",
    "HHHHHHHH             H           HH     HH                         FF                        XXXX                          GGG                          G  X          X  S     SSSSS     SS                                                  ",
    "HHHHHHHH           HHHHH       FFFF     FF                    HHH                            XXXX                  GGG     XXX                       G  X             X  S    TSSSSS                                             ",
    "HHHHHHHH P   HH    HHHHHH                                     FFF                            XXXX   GGG          GGXXX                            G  X                X  S    SSSSSST                                        ",
    "HHHHHHHHHHH  HHH   HHHHHH                              HHH                                   XXXX   XXX    GG    XXXXX                         G  X                   X  SSSSSSSSSSSS                                                ",
    "HHHHHHHHHHHHHHHH   HHHHHH    HHHHHHH           HHH     FFF                                   XXXX          XX                               G  X                      X                  TT                         ",
    "FFFFFFFFFFFFFFFF   FFFFFF    FFFFFFF   FFF     FFF                                           XXXX                                        G  X                         X                  SS                            ",
    "XXXXXXXXXXXXXXXX   XXXXXX    XXXXXXX                                                         XXXX                                     GGGX                            XXSSSSSSSSSSSSS                                                ",
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
