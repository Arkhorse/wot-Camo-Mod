# -*- coding: utf-8-sig -*-

# connect the game engine libraries available in the game client built-in python
import logging
import BigWorld
import BattleReplay
from debug_utils import LOG_CURRENT_EXCEPTION
from Avatar import PlayerAvatar
from skeletons.gui.app_loader import IAppLoader, GuiGlobalSpaceID
from gui.app_loader.settings import APP_NAME_SPACE
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.entities.View import View
from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID
# from items.utils import getInvisibility, getClientInvisibility
from BattleFeedbackCommon import BATTLE_EVENT_TYPE
from gui.battle_control.controllers import feedback_events

from mod_constants_camo import MOD, CONFIG_FILES
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

GENERATOR = {
    BATTLE_EVENT_TYPE.VISIBILITY_EVENTS     : ['UI_message_VISIBILITY_EVENTS_text', 'messageColorVISIBILITY_EVENTS']
}

# Mod Start

def onAppInitialized(self, event):
        if event.ns != APP_NAME_SPACE.SF_BATTLE:
            return
        _logger.info('AppLifeCycleEvent.INITIALIZED: SF_BATTLE')
        #self.initPanel()

def onAppDestroyed(self, event):
        if event.ns != APP_NAME_SPACE.SF_BATTLE:
            return
        _logger.info('AppLifeCycleEvent.DESTROYED: SF_BATTLE')
        self.finiPanel()

def format_recreate(self):
        self.format_str = {
            'camo'         : ''
        }
        
def textGenerator(self, event):
        text
        
def post_message(self, events):
    try:
        _logger.info('message started')
        g_sessionProvider = BigWorld.player().guiSessionProvider
        self.format_recreate()
        for data in events:
            feedbackEvent = feedback_events.PlayerFeedbackEvent.fromDict(data)
            eventID = feedbackEvent.getBattleEventType()
            if eventID in [BATTLE_EVENT_TYPE.VISIBILITY_EVENTS]:
                vehicleID = feedbackEvent.getTargetID()
                text
                inject.message(text)
    except:
        _logger.critical('Message Failed')
print '[LOAD_MOD]: [Camo Indicator by The Illusion]'