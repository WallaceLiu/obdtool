﻿# -*- coding: utf-8 -*-

from CmdBase import CmdBase
from Msg_Src import Msg_Src
from Msg_Dest import Msg_Dest
from ErrorCommandFormat import ErrorCommandFormat


class CmdSend(CmdBase):
    """
        send command.

        Command Format :
        send <v1>
        send <v1><[-|,]><v2>
    """
    __msg_src = None
    __msg_dest = None
    __mode = None

    def __init__(self, params, srcDb, destMode, destDb, s):
        self.id = ""
        self.name = "send command"
        self.params = params  
        self.cmd = "SEND"

        self.__mode = destMode

        self.__msg_src = Msg_Src(srcDb)
        self.__msg_dest = Msg_Dest(destDb)

        self.frm = None
        self.to = None

        self.__s = s

        self.validate()

    def validate(self):
        CmdBase.validate(self)

        if len(self.params) < 2:
            raise ErrorCommandFormat("Command Params Error.")
        else :
            frmtos = str.split(self.params[1].replace('-',','),',')

            if len(frmtos) == 1:
                self.frm = frmtos[0]
                self.to = None
            elif len(frmtos) == 2:
                self.frm = frmtos[0]
                self.to = frmtos[1]
            else:
                raise ErrorCommandFormat("Command Params Error.")

    def execute(self):

        try:
            if self.__mode == 'database':
                self.toDatabase()
            elif self.__mode == 'tcp':
                self.toTcp()
            elif self.__mode == 'both':
                self.toDatabase()
                self.toTcp()
        except  Exception as e:
            print(e.args)

    def toDatabase(self):
        msg = None
        if self.to == None:
            msg = self.__msg_src.getMsg(self.frm)
        else:
            msg = self.__msg_src.getMsgCollection(self.frm, self.to)

        for id,clientIp,processingData,type in msg:
            print(self.cmd + ' ID=' + str(id) + '...')
            bl = self.__msg_dest.insertMsg(clientIp, processingData, type)
            print(bl)
    
    def toTcp(self):
        msg = None

        if self.to == None:
            msg = self.__msg_src.getMsg(self.frm)
        else:
            msg = self.__msg_src.getMsgCollection(self.frm, self.to)

        for id,clientIp,processingData,type in msg:
            print(self.cmd + ' ID=' + str(id) + '...')

            self.__s.send(processingData)

            data = self.__s.recv(100)
            if data == None or len(data) == 0:
                continue
            print(data)

            '''tmp = []
            while True:
                data = self.__s.recv(1024)
                if not data:
                    break
                tmp.append(data)
            print(tmp)'''

