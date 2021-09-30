
class coin_info:
    COIN_DIMENSION: int = 75
    COIN_COLUMN: int = 5
    COIN_ROW: int = 6
    COIN_COLOR_NUMBER: int = 5
    COIN_NOT_CHOSEN: int = -1

class coin_separation:
    SEPARATION: float = 37.5
    CENTERS_SEPARATION: float = coin_info.COIN_DIMENSION + SEPARATION

class object_colors:
    GREEN = (45, 175, 128)
    BLUE = (45, 49, 175)
    RED = (175, 45, 75)
    GREY = (162, 162, 162)
    BLACK = (0,0,0)

class field_setup:
    INITIAL_COIN_SETUP = [0, 2, 4]
    INITIAL_EMPTYSPACE_SETUP = [(2,1), (2,3), (4,1), (4,3)]
    SET_COLORS = [(0,0), (0,2), (0,4)]
    EMPTY = [(0,1), (0,3)]

class samples:
    COLOR_SAMPLE = [object_colors.RED, object_colors.GREEN, object_colors.BLUE]
    COLOR_SAMPLE_REPEATS = [object_colors.RED, object_colors.RED, object_colors.RED, \
                            object_colors.RED, object_colors.RED, object_colors.GREEN, \
                            object_colors.GREEN, object_colors.GREEN, object_colors.GREEN, \
                            object_colors.GREEN, object_colors.BLUE, object_colors.BLUE, \
                            object_colors.BLUE, object_colors.BLUE, object_colors.BLUE]
    
class endgame:
    MISMATCH = 0
    MATCH = 1