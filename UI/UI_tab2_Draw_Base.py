import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import os
from UI_matplotlib import *


class UI_tab2_Draw_Base(QWidget):
    
    def __init__(self, parent=None): 
        super(UI_tab2_Draw_Base, self).__init__(parent) 
        self.setupUI()
        
        
    def setupUI(self):
       
        self.setLeftUI()
        self.setRtUI()
    
       #总体一个水平布局，坐标是一个坐标点列表，右边是一个画布        
        self.totalHLayout=QHBoxLayout(self)
        self.totalHLayout.addLayout(self.leftLayout)
        self.totalHLayout.addLayout(self.rtLayout)        
        self.setLayout(self.totalHLayout)
        
    def setLeftUI(self):
        
        _translate = QCoreApplication.translate           
       #定义左边坐标点列表，要加个标签“输入基础平面的角点坐标（x，y）（mm）
        self.leftTipLabel =QLabel()
        self.leftTipLabel.setText(_translate("Form", "逆时针输入基础平面角点的xy坐标(mm)"))

        #定义左边表格
        self.tableWidget=QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['编号', 'x坐标', 'y坐标'])
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 80)    
        self.tableWidget.setColumnWidth(2, 80)          
        
        #第一个点（0,0）
        newItem=QTableWidgetItem('1')
        self.tableWidget.setItem(0, 0, newItem)
        newItem=QTableWidgetItem('0')
        self.tableWidget.setItem(0, 1, newItem)   
        newItem=QTableWidgetItem('0')
        self.tableWidget.setItem(0, 2, newItem)   
   
        #第2个点（0,20）
        newItem=QTableWidgetItem('2')
        self.tableWidget.setItem(1, 0, newItem)
        newItem=QTableWidgetItem('20')
        self.tableWidget.setItem(1, 1, newItem)   
        newItem=QTableWidgetItem('0')
        self.tableWidget.setItem(1, 2, newItem)   
      
        #第3个点（20,20）
        newItem=QTableWidgetItem('3')
        self.tableWidget.setItem(2, 0, newItem)
        newItem=QTableWidgetItem('20')
        self.tableWidget.setItem(2, 1, newItem)   
        newItem=QTableWidgetItem('20')
        self.tableWidget.setItem(2, 2, newItem)        
        
        #定义左侧竖向布局
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.leftTipLabel)
        self.leftLayout.addWidget(self.tableWidget)  
          
    
    def setRtUI(self):
        
        #定义绘图区Widget
        self.drawBaseWidget= MatplotlibWidget()
        self.drawBaseWidget.mpl.start_drawBase_plot()
        
        #定义右侧竖向布局
        self.rtLayout = QVBoxLayout()
        self.rtLayout.addWidget(self.drawBaseWidget)        
        
#    def setupUI(self):
#        
#     _translate = QCoreApplication.translate
#        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)         
#
#        #总体一个水平布局，坐标是一个坐标点列表，右边是一个画布        
#        self.totalHLayout=QHBoxLayout(self)
#        
#        #定义左边坐标点列表，要加个标签“输入基础平面的角点坐标（x，y）（mm）
#        self.leftTipLabel =QLabel()
#        self.leftTipLabel.setText(_translate("Form", "逆时针输入基础平面角点的xy坐标(mma)"))
#        
#        #定义左侧Table，要和SQL模型连接
#        self.initializeModel()   
#        self.creatView()
#        
#        #定义左侧竖向布局
#        self.leftLayout = QVBoxLayout()
#        self.leftLayout.addWidget(self.leftTipLabel)
#        self.leftLayout.addWidget(self.view)
#
#        
#        
#        self.totalHLayout.addLayout(self.leftLayout)
#        
#    def initializeModel(self):
#        
#        #保存到文件        
#        if os.path.isfile('basePointCor.db'):
#            os.remove('basePointCor.db')        
#                
#        self.db=QSqlDatabase.addDatabase('QSQLITE')
#        self.db.setDatabaseName('basePointCor.db')
#        
#        self.model=QSqlTableModel()        
#        self.model.setTable('MTCCsql')
#        self.model.setEditStrategy( QSqlTableModel.OnFieldChange)
#        self.model.select()
#        self.model.setHeaderData(0, Qt.Horizontal, "编号")
#        self.model.setHeaderData(1, Qt.Horizontal, "x坐标")
#        self.model.setHeaderData(2, Qt.Horizontal, "y坐标")  
#                
#    def creatView(self):
#        self.view=QTableView()
#        self.view.setModel(self.model)
#        self.view.show()
#        
        
       
        
        
if  __name__ == '__main__':
    app=QApplication(sys.argv)
    ui = UI_tab2_Draw_Base()    
    ui.show()
    sys.exit(app.exec_())       
