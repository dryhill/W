import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI_tab4_calc(QWidget):
    
    def __init__(self, parent=None): 
        super(UI_tab4_calc, self).__init__(parent) 
        self.setupUI()
        
         
    def setupUI(self):
        
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)   
        self.settopUI()
        self.setbottomUI()
        
       #总体一个竖直布局，上面是按钮计算，打印计算书，保存温度云图，下面是一个文本框显示计算书     
        self.totalVLayout=QVBoxLayout(self)
        self.totalVLayout.addLayout(self.topLayout)
        self.totalVLayout.addLayout(self.bottomLayout)        
        self.setLayout(self.totalVLayout)  
  
    def settopUI(self):
        
        _translate = QCoreApplication.translate
        self.CalcPushButton =QPushButton()
        self.CalcPushButton.setText(_translate("Form", "计算"))  
        self.printWordPushButton =QPushButton()
        self.printWordPushButton.setText(_translate("Form", "打印计算书"))     
        self.printFigPushButton =QPushButton()
        self.printFigPushButton.setText(_translate("Form", "保存温度云图")) 
 
        self.topLayout = QHBoxLayout()
        self.topLayout.addWidget(self.CalcPushButton)
        self.topLayout.addWidget(self.printWordPushButton)
        self.topLayout.addWidget(self.printFigPushButton)    
    
    def setbottomUI(self):  
        _translate = QCoreApplication.translate        
        self.bottomLayout = QHBoxLayout()
        self.textWidget = QTextEdit()
        self.bottomLayout.addWidget(self.textWidget)
        self.textWidget.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">大体积混凝土水管冷却温度测算计算书</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. 工程编号:JC1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. 工程参数</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">基础长度：20m</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">基础宽度：20m</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">基础厚度：5m</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))        
        
        
if  __name__ == '__main__':
    app=QApplication(sys.argv)
    ui = UI_tab4_calc()    
    ui.show()
    sys.exit(app.exec_())           
