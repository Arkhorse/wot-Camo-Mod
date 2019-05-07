# -*- coding: utf-8-sig -*-

# connect the game engine libraries available in the game client built-in python
import logging
import BigWorld
from mod_constants_camo import MOD, CONFIG_FILES
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import SystemMessages
from Account import Account
from Avatar import PlayerAvatar
from skeletons.gui.app_loader import IAppLoader, GuiGlobalSpaceID
from gui.app_loader.settings import APP_NAME_SPACE
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.entities.View import View
from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID
# from items.utils import getInvisibility, getClientInvisibility
from BattleFeedbackCommon import BATTLE_EVENT_TYPE
from gui.battle_control.controllers import feedback_events

# noinspection PyUnresolvedReferences
# from gui.mods.mod_mods_gui import g_gui, inject

_logger = logging.getLogger(MOD.NAME)

def getLogLevel(name):
    logLevel = {
        'CRITICAL':     logging.CRITICAL,
        'ERROR':        logging.ERROR,
        'WARNING':      logging.WARNING,
        'INFO':         logging.INFO,
        'DEBUG':        logging.DEBUG,
        'NOTSET':       logging.NOTSET
    }
    return logLevel.get(name, logging.INFO)
_logger.info('Staring Camo Indicator')
COLORS = ['#FE0E00', '#FE7903', '#F8F400', '#60FF00', '#02C9B3', '#D042F3']
MENU = ['UI_color_blue', 'UI_color_brown', 'UI_color_chocolate', 'UI_color_cornflower_blue', 'UI_color_cream', 'UI_color_cyan', 'UI_color_emerald', 'UI_color_gold', 'UI_color_green', 'UI_color_green_yellow', 'UI_color_hot_pink', 'UI_color_lime',
        'UI_color_orange', 'UI_color_pink', 'UI_color_purple', 'UI_color_red', 'UI_color_wg_blur', 'UI_color_wg_enemy', 'UI_color_wg_friend', 'UI_color_wg_squad', 'UI_color_yellow', 'UI_color_nice_red', 'UI_color_very_bad', 'UI_color_bad', 'UI_color_normal', 'UI_color_good', 'UI_color_very_good', 'UI_color_unique']

GENERATOR = {
    BATTLE_EVENT_TYPE.VISIBILITY_EVENTS     : ['UI_message_VISIBILITY_EVENTS_text', 'messageColorVISIBILITY_EVENTS']
}

# Mod Start
def modStart(self):
    parent(self)
    SystemMessages.pushMessage('Camo Indicator Loaded', type=SystemMessages.SM_TYPE.Warning)
    Account.onBecomePlayer = parent
parent = Account.onBecomePlayer
Account.onBecomePlayer = modStart

def format_recreate(self):
        self.format_str = {
            'camo'         : ''
        }
        
def textGenerator(self, event):
        text, color = GENERATOR[event]
        return config.i18n[text].format(**self.format_str), COLOR[config.data[color]]
        
def post_message(self, events):
        g_sessionProvider = BigWorld.player().guiSessionProvider
        self.format_recreate()
        for data in events:
            feedbackEvent = feedback_events.PlayerFeedbackEvent.fromDict(data)
            eventID = feedbackEvent.getBattleEventType()
            if eventID in [BATTLE_EVENT_TYPE.VISIBILITY_EVENTS]:
                vehicleID = feedbackEvent.getTargetID()
                text, colour = self.textGenerator(eventID)
                inject.message(text, color)
                
print '[LOAD_MOD]: [Camo Indicator by The Illusion]'