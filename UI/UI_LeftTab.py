import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI_tab1_Define_parametere import *
from UI_tab2_Draw_Base import *
from UI_tab3_set_WaterPipe import *
from UI_tab4_calc import *

#define tab
class TabLeft(QTabWidget):
    def __init__(self, parent=None):
        super(TabLeft, self).__init__(parent)
        self.tabDefineParameter=QWidget()
        self.tabDrawBase=QWidget()
        self.tabSetWaterPipe=QWidget()
        self.tabCalc=QWidget()
        
        self.addTab(self.tabDefineParameter, "    参数定义    ")
        self.addTab(self.tabDrawBase, "    基础绘制    ")
        self.addTab(self.tabSetWaterPipe, "    水管布置    ")
        self.addTab(self.tabCalc, "        计算        ")
        
        self.tabDefineParameter_setUI()
        self.tabDrawBase_setUI()
        self.tabSetWaterPipe_setUI()
        self.tabCalc_setUI()
        
    def tabDefineParameter_setUI(self):
        layout = QVBoxLayout()
        tab1 = UI_tab1_Define_parametere()
        layout.addWidget(tab1)
        self.tabDefineParameter.setLayout(layout)    
    
    def tabDrawBase_setUI(self):
        layout = QVBoxLayout()
        tab2 = UI_tab2_Draw_Base()
        layout.addWidget(tab2)
        self.tabDrawBase.setLayout(layout)       
        
    def tabSetWaterPipe_setUI(self):
        layout = QVBoxLayout()
        tab3 = UI_tab3_set_WaterPipe()
        layout.addWidget(tab3)
        self.tabSetWaterPipe.setLayout(layout)  
        
    def tabCalc_setUI(self):
        layout = QVBoxLayout()
        tab4 = UI_tab4_calc()
        layout.addWidget(tab4)
        self.tabCalc.setLayout(layout)          
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    
    demo = TabLeft()    
    demo.show()
    sys.exit(app.exec_())
