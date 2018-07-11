import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import os
from UI_matplotlib import *


class UI_tab3_set_WaterPipe(QWidget):
    
    def __init__(self, parent=None): 
        super(UI_tab3_set_WaterPipe, self).__init__(parent) 
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
       #定义左边坐标点列表
        self.leftXYTipLabel =QLabel()
        self.leftXYTipLabel.setText(_translate("Form", "输入各道水管平面间距(mm)"))

        #1-定义平面间距表格
        self.tableXYWidget=QTableWidget()
        self.tableXYWidget.setRowCount(5)
        self.tableXYWidget.setColumnCount(2)
        self.tableXYWidget.setHorizontalHeaderLabels(['编号', '平面间距'])
        self.tableXYWidget.setColumnWidth(0, 40)
        self.tableXYWidget.setColumnWidth(1, 80)             
        
        #第一道
        newItem=QTableWidgetItem('1')
        self.tableXYWidget.setItem(0, 0, newItem)
        newItem=QTableWidgetItem('2*9')
        self.tableXYWidget.setItem(0, 1, newItem)   

       #定义左边坐标点列表
        self.leftZTipLabel =QLabel()
        self.leftZTipLabel.setText(_translate("Form", "输入各道水管竖向间距(mm)"))
        
        #2-定义厚度方向间距表格
        self.tableZWidget=QTableWidget()
        self.tableZWidget.setRowCount(5)
        self.tableZWidget.setColumnCount(2)
        self.tableZWidget.setHorizontalHeaderLabels(['编号', '竖向间距'])
        self.tableZWidget.setColumnWidth(0, 40)
        self.tableZWidget.setColumnWidth(1, 80)             
        
        #第一道
        newItem=QTableWidgetItem('1')
        self.tableZWidget.setItem(0, 0, newItem)
        newItem=QTableWidgetItem('2*2')
        self.tableZWidget.setItem(0, 1, newItem)  

        #3-1指定水管平面布置形式
        self.pipeXYGroupBox =QGroupBox()
        self.pipeXYGroupBox.setTitle(_translate("Form", "水管平面布置形式"))  
       
        self.pipeXYLayout = QGridLayout(self.pipeXYGroupBox)        
        self.pipeXYLayout.addWidget(self.createCellWidget("单向",
                ':/images/pipeSingleDirection.png'), 0, 0)                
        self.pipeXYLayout.addWidget(self.createCellWidget("条形",
                ':/images/pipeOneway.png'), 0, 1)
        self.pipeXYLayout.addWidget(self.createCellWidget("回形",
                ':/images/pipeCircle.png'), 0, 2)                
     
        #3-2指定水管竖向布置形式
        self.pipeZGroupBox =QGroupBox()
        self.pipeZGroupBox.setTitle(_translate("Form", "水管竖向布置形式")) 
        
        self.pipeZLayout = QGridLayout(self.pipeZGroupBox)
        self.pipeZLayout.addWidget(self.createCellWidget("对齐布置",
                ':/images/pipeZregular.png'), 0, 0)                
        self.pipeZLayout.addWidget(self.createCellWidget("梅花形布置",
                ':/images/pipeZstagger.png'), 0, 1)


        #定义左侧竖向布局
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.leftXYTipLabel)
        self.leftLayout.addWidget(self.tableXYWidget)  
        self.leftLayout.addWidget(self.leftZTipLabel)
        self.leftLayout.addWidget(self.tableZWidget) 
        self.leftLayout.addWidget(self.pipeXYGroupBox)     
        self.leftLayout.addWidget(self.pipeZGroupBox)           
    
    def setRtUI(self):
        
        #定义绘图区Widget
        self.drawBaseWidget= MatplotlibWidget()
        self.drawBaseWidget.mpl.start_drawBase_plot()
        self.drawBaseWidget.mpl.start_drawPipe_plot()        
        
        #定义右侧竖向布局
        self.rtLayout = QVBoxLayout()
        self.rtLayout.addWidget(self.drawBaseWidget)        
        
    def createCellWidget(self, text, image):
        button = QToolButton()
        button.setText(text)
        button.setIcon(QIcon(image))
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
#        self.backgroundButtonGroup.addButton(button)

        layout = QGridLayout()
        layout.addWidget(button, 0, 0, Qt.AlignHCenter)
        layout.addWidget(QLabel(text), 1, 0, Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        return widget 
        
if  __name__ == '__main__':
    app=QApplication(sys.argv)
    ui = UI_tab3_set_WaterPipe()    
    ui.show()
    sys.exit(app.exec_())       
