# -*- coding: utf-8 -*-

from LoadConf import LoadConf
from mysql_python_factory import MysqlPythonFacotry

class Biz_Base(object):

    def __init__(self, db):
        self.db = db
