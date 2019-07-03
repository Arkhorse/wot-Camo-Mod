
import math

from constants import ARENA_PERIOD
# from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID
# from skeletons.gui.app_loader import GuiGlobalSpaceID

class MOD:
    ID = '${mod_id}'
    PACKAGE_ID = '${package_id}'
    NAME = '${name}'
    VERSION = '${version}'

CONFIG_FILES = [
    '${resource_dir}/config.json',
    '${config_file}'
]

LOG_FILE = '${log_file}'

ARENA_PERIOD_SYMBOL = {
    ARENA_PERIOD.IDLE:          'IDLE',
    ARENA_PERIOD.WAITING :      'WAITING',
    ARENA_PERIOD.PREBATTLE:     'PREBATTLE',
    ARENA_PERIOD.BATTLE:        'BATTLE',
    ARENA_PERIOD.AFTERBATTLE:   'AFTERBATTLE'
}

GUI_GLOBAL_SPACE_SYMBOL = {
    GuiGlobalSpaceID.UNDEFINED:         'UNDEFINED',
    GuiGlobalSpaceID.WAITING:           'WAITING',
    GuiGlobalSpaceID.INTRO_VIDEO:       'INTRO_VIDEO',
    GuiGlobalSpaceID.LOGIN:             'LOGIN',
    GuiGlobalSpaceID.LOBBY:             'LOBBY',
    GuiGlobalSpaceID.BATTLE_LOADING:    'BATTLE_LOADING',
    GuiGlobalSpaceID.BATTLE:            'BATTLE',