#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
#Copyright (C)2010 Abhinandh <abhinandh@gmail.com>
#Copyleft (C)2012 IMPIZA  <gsruthin@gmail.com>
#This Program in licenser under General Public License Ver 3
    
import sys
from PyQt4.QtGui import QApplication, QSystemTrayIcon

from droptarget import DropWidget
import icons_rc
    
def main():
    app = QApplication(sys.argv)
        
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray", "I couldn't detect any system tray on this system.")
        return -1
    mainWidget = DropWidget()
    mainWidget.show()
    sys.exit(app.exec_())
        
if __name__=='__main__':
    main()
