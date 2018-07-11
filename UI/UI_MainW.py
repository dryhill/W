import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_LeftTab import *

class MainW(QMainWindow):
    
    def __init__(self, parent=None):        
        super(MainW, self).__init__(parent)
        self.status=self.statusBar()
        self.status.showMessage('大体积混凝土温度控制', 5000)
        self.setWindowTitle('大体积混凝土温度控制')
    
        
        #定义菜单栏和动作
        self.createActions()
        self.createMenus()
#        self.createToolbars()
   
        #定义窗口布局
        #整体一个竖直布局，里面填
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)    
        
        self.addTitleLabel()
        self.addLeftTabView()
    
    
    
    def addTitleLabel(self):
    #1-顶部大标题
        _translate = QCoreApplication.translate        
        self.titleLabel = QLabel(self)
        self.titleLabel.setText(_translate("Form", "大体积混凝土基础温度计算"))
        font = QFont()
        font.setPointSize(25)
        self.titleLabel.setFont(font)
        #左右弹性
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)        
        self.titleHorizontalLayout = QHBoxLayout() 
        self.titleHorizontalLayout.addItem(spacerItem)
        self.titleHorizontalLayout.addWidget(self.titleLabel)
        self.titleHorizontalLayout.addItem(spacerItem)  
        
        #总体大竖向布局添加
        self.layout.addLayout(self.titleHorizontalLayout)
        
    def addLeftTabView(self):
        
        self.tabWidget = QWidget()
        self.leftTabUi = TabLeft()
        self.layout.addWidget(self.leftTabUi)
        
        
       
    def createActions(self):
        self.newAction = QAction(
                QIcon(':/images/new.png'), "新建",
                self, shortcut="Ctrl+N", statusTip="新建项目")    
        
        self.saveAction = QAction(
                QIcon(':/images/save.png'), "保存",
                self, shortcut="Ctrl+N", statusTip="保存项目") 

        self.saveasAction = QAction(
                QIcon(':/images/saveas.png'), "另存为",
                self, shortcut="Ctrl+Shift+S", statusTip="另存项目")    
   
        self.quitAction = QAction(
                QIcon(':/images/quit.png'), "保存",
                self, shortcut="Ctrl+Q", statusTip="退出目")
             
    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&文件")
        self.fileMenu.addAction(self.newAction)  
        self.fileMenu.addAction(self.saveAction)   
        self.fileMenu.addAction(self.saveasAction)   
        self.fileMenu.addAction(self.quitAction)           
             
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/3D_Mycelium_Minecraft_Png_128px_1119161_easyicon.net.ico"))
    mainWindow = MainW()    
    mainWindow.setGeometry(100, 100, 800, 600)
    mainWindow.show()
    sys.exit(app.exec_())
