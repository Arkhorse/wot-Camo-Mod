# -*- coding: utf-8-sig -*-

# connect the game engine libraries available in the game client built-in python
import datetime
import math
import Math
import BigWorld
import Vehicle
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import SystemMessages
from Account import Account
from Avatar import PlayerAvatar
from skeletons.gui.app_loader import IAppLoader, GuiGlobalSpaceID
from gui.app_loader.settings import APP_NAME_SPACE

# noinspection PyUnresolvedReferences
from gui.mods.mod_mods_gui import g_gui, inject

COLORS = ['#FE0E00', '#FE7903', '#F8F400', '#60FF00', '#02C9B3', '#D042F3']
MENU = ['UI_color_blue', 'UI_color_brown', 'UI_color_chocolate', 'UI_color_cornflower_blue', 'UI_color_cream', 'UI_color_cyan', 'UI_color_emerald', 'UI_color_gold', 'UI_color_green', 'UI_color_green_yellow', 'UI_color_hot_pink', 'UI_color_lime',
        'UI_color_orange', 'UI_color_pink', 'UI_color_purple', 'UI_color_red', 'UI_color_wg_blur', 'UI_color_wg_enemy', 'UI_color_wg_friend', 'UI_color_wg_squad', 'UI_color_yellow', 'UI_color_nice_red', 'UI_color_very_bad', 'UI_color_bad', 'UI_color_normal', 'UI_color_good', 'UI_color_very_good', 'UI_color_unique']

# In Garage Settings
class Config(object):
    def __init__(self):
        self.ids = 'Camo Indicator'
        self.version = 'v0.01 (2019-05-06)'
        self.version_id = 001
        self.author = 'by the illusion'
        self.data = {
            'version'           : self.version_id,
            'enabled'           : True,
            'testOption'        : 'testOption'
            }
        self.i18n = {
            'version'                              : self.version_id,
            'UI_description'                       : 'Camo Indicator',
            'UI_setting_show_text'           : 'This is test text',
            'UI_setting_test_tooltip'        : '{HEADER}<font color="#FFD700">Info:</font>{/HEADER}{BODY}Test Header:\n<font color="#FFD700">test\ntest2</font>{/BODY}',
            'UI_color_blue'                        : 'Blue',
            'UI_color_brown'                       : 'Brown',
            'UI_color_chocolate'                   : 'Chocolate',
            'UI_color_cornflower_blue'             : 'Cornflower Blue',
            'UI_color_cream'                       : 'Cream',
            'UI_color_cyan'                        : 'Cyan',
            'UI_color_emerald'                     : 'Emerald',
            'UI_color_gold'                        : 'Gold',
            'UI_color_green'                       : 'Green',
            'UI_color_green_yellow'                : 'Green Yellow',
            'UI_color_hot_pink'                    : 'Hot Pink',
            'UI_color_lime'                        : 'Lime',
            'UI_color_orange'                      : 'Orange',
            'UI_color_pink'                        : 'Pink',
            'UI_color_purple'                      : 'Purple',
            'UI_color_red'                         : 'Red',
            'UI_color_wg_blur'                     : 'WG Blur',
            'UI_color_wg_enemy'                    : 'WG Enemy',
            'UI_color_wg_friend'                   : 'WG Friend',
            'UI_color_wg_squad'                    : 'WG Squad',
            'UI_color_yellow'                      : 'Yellow',
            'UI_color_nice_red'                    : 'Nice Red',
            'UI_color_very_bad'                    : 'Very bad rating',
            'UI_color_bad'                         : 'Bad rating',
            'UI_color_normal'                      : 'Normal rating',
            'UI_color_good'                        : 'Good rating',
            'UI_color_very_good'                   : 'Very good rating',
            'UI_color_unique'                      : 'Unique rating'
            }
        self.data, self.i18n = g_gui.register_data(self.ids, self.data, self.i18n, 'spoter')
        g_gui.register(self.ids, self.template, self.data, self.apply)
        print '[LOAD_MOD]:  [%s %s, %s]' % (self.ids, self.version, self.author)
        
    def template(self):
        return {
            'modDisplayName' : self.i18n['UI_description'],
            'settingsVersion': self.version_id,
            'enabled'        : self.data['enabled'],
            'column1'        : [
                {
                    'type'   : 'CheckBox',
                    'text'   : self.i18n['UI_setting_test_text'],
                    'value'  : self.data['Camo Indicator'],
                    'tooltip': self.i18n['UI_setting_test_tooltip'],
                    'varName': 'test'
                }]
            }
            
    def apply(self, settings):
        self.data = g_gui.update_data(self.ids, settings, 'spoter')
        g_gui.update(self.ids, self.template)
# Mod Start
def hello(self):
    parent(self)
    SystemMessages.pushMessage('Camo Indicator Loaded', type=SystemMessages.SM_TYPE.Warning)
    Account.onBecomePlayer = parent
parent = Account.onBecomePlayer
Account.onBecomePlayer = hello