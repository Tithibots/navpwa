import os

MODULEDIR = os.path.dirname(__file__)
SESSIONDIR = os.path.join(MODULEDIR, 'sessions')

DEFAULT_WAIT = 89

class SELECTORS(object):
    MAIN_SEARCH_BAR = '._3FRCZ'
    MAIN_SEARCH_BAR_DONE = '.MfAhJ'
    MAIN_SEARCH_BAR_SEARCH_ICON = '._3e4VU'
    MAIN_SEARCH_BAR_BACK_ARROW = '._3e4VU'
    MESSAGE_INPUT_BOX = '#main footer ._3FRCZ'
    TURN_ON_DESKTOP_NOTIFICATIONS = '.zKq5Y'
    CLOSE_INFO = '[data-testid="x-alt"]'
    MAIN_MENU_OPTIONS__MENU_ICON = '[data-testid=menu]'
    MAIN_MENU_OPTIONS__NEW_GROUP = '[title="New group"]'
    CREATE_NEW_GROUP__TYPE_CONTACTS_INPUT_BOX = '._17ePo'
    CREATE_NEW_GROUP__RESULT_CONTACT = '._210SC'
    CREATE_NEW_GROUP__OK_CONTACTS_TYPE = '[data-testid="arrow-forward"]'
    CREATE_NEW_GROUP__TYPE_GROUP_NAME = '._3FRCZ'
    CREATE_NEW_GROUP__OK_GROUP_NAME_TYPE = '._3y5oW'
    CREATE_NEW_GROUP__ENCRYPTED_LOCK_SIGN = '._2VO5X'
    CHATROOM__NAME_AND_INFO = '._33QME'
    CHATROOM__NAME = '.DP7CM'
    CHATROOM__INFO = '._3-cMa._3Whw5'
    CHATROOM__CLOSE_INFO = '[data-testid="x"]'
    GROUPS__MEMBERS_SEARCH_ICON = '._3lS1C'
    GROUPS__SEARCH_CONTACTS_INPUT_BOX = '._9a59P ._3FRCZ'
    GROUPS__CONTACTS_SEARCH_NAME = '._3ko75'
    GROUPS__CLOSE_CONTACTS_SEARCH = '._2HE5l .t4a8o'
    GROUPS__ADMIN_ICON = '.LwCwJ'
    GROUPS__MAKE_ADMIN = '.Ut_N0'
    GROUPS__REMOVE = '.Ut_N0[title="Remove"]'
    GROUPS__EXIT_FROM_GROUP = '._3wAoe._3DSZk[title="Exit group"]'
    GROUPS__EXIT_DIALOG_BOX = '._9a59P'
    GROUPS__EXIT_BUTTON_EXIT_DIALOG_BOX = '.S7_rT.FV2Qy'
    GROUPS__NO_LONGER_A_PARTICIPANT = '._3ge3i'
    GROUPS__GROUP_NAME_IN_CHATS = '._3CneP > ._3ko75._5h6Y_._3Whw5'

class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'