# -*- coding: utf-8 -*-
from CommandChain import CommandChain
import os
# from testCommandChain import TestCommandChain

if __name__ == "__main__":
    #main()
    #t = TestCommandChain()
	#t.test()
	try:
		cmds = CommandChain()
		cmds.loadCmdList(os.getcwd()+"/usecase_drive/case_01.txt");
		cmds.execute()	
	except  Exception as e:
            print(e.args)


