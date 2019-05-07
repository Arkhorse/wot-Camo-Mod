# -*- coding: utf-8-sig -*-

# connect the game engine libraries available in the game client built-in python
import logging
import BigWorld
import Vehicle
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import SystemMessages
from Account import Account

# noinspection PyUnresolvedReferences
from gui.mods.mod_mods_gui import g_gui, inject

_logger = logging.getLogger(camoIndicator)

g_indicatorManager = None

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


class Config(object):
    def __init__(self):
        self.ids = 'Test Mod'
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
            'UI_description'                       : 'Test',
            'UI_setting_test_text'           : 'This is test text',
            'UI_setting_test_tooltip'        : '{HEADER}<font color="#FFD700">Info:</font>{/HEADER}{BODY}Test Header:\n<font color="#FFD700">test\ntest2</font>{/BODY}'
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
                    'value'  : self.data['Test Mod'],
                    'tooltip': self.i18n['UI_setting_test_tooltip'],
                    'varName': 'test'
                }]
            }
            
    def apply(self, settings):
        self.data = g_gui.update_data(self.ids, settings, 'spoter')
        g_gui.update(self.ids, self.template)

def hello(self):
    parent(self)
    try:
        SystemMessages.pushMessage('Hello WoT!', type=SystemMessages.SM_TYPE.Warning)
    except:
        LOG_CURRENT_EXCEPTION()
        _logger.warning('fail to talk')
    Account.onBecomePlayer = parent
parent = Account.onBecomePlayer
Account.onBecomePlayer = hello