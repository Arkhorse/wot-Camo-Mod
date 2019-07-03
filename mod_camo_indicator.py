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
from items.utils import getInvisibility, getClientInvisibility
from BattleFeedbackCommon import BATTLE_EVENT_TYPE
from gui.battle_control.controllers import feedback_events

from mod_constants_camo import MOD, CONFIG_FILES


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

# Mod Start
