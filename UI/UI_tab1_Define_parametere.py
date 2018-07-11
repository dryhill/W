import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI_tab1_Define_parametere(QWidget):
    
    def __init__(self, parent=None): 
        super(UI_tab1_Define_parametere, self).__init__(parent) 
        self.setupUI()
        
         
    def setupUI(self):
        
        _translate = QCoreApplication.translate
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)         

        #总体一个竖向布局        
        self.totalVerticalLayout=QVBoxLayout(self)
       
        #一-基础参数
        #3-3个GroupBOX挨个定义
        #3-1第一个groupbox-基础尺寸
        self.baseSizeGroupBox =QGroupBox()
        self.baseSizeGroupBox.setTitle(_translate("Form", "基础尺寸"))        
        #布局放在groupBox中
        self.baseLengthLabel =QLabel()
        self.baseLengthLabel.setText(_translate("Form", "基础长度(m)"))  
        self.baseLengthLineEdit = QLineEdit()  

        self.baseWidthLabel =QLabel()
        self.baseWidthLabel.setText(_translate("Form", "基础宽度(m)"))  
        self.baseWidthLineEdit = QLineEdit() 
        
        self.baseThickLabel =QLabel()
        self.baseThickLabel.setText(_translate("Form", "基础厚度(m)"))  
        self.baseThickLineEdit = QLineEdit()         
        
        self.baseSizeVerticalLayout = QVBoxLayout(self.baseSizeGroupBox)
        self.baseSizeVerticalLayout.addWidget(self.baseLengthLabel)
        self.baseSizeVerticalLayout.addWidget(self.baseLengthLineEdit)     
        self.baseSizeVerticalLayout.addWidget(self.baseWidthLabel)
        self.baseSizeVerticalLayout.addWidget(self.baseWidthLineEdit)    
        self.baseSizeVerticalLayout.addWidget(self.baseThickLabel)
        self.baseSizeVerticalLayout.addWidget(self.baseThickLineEdit)   
  
        #3-2第2个groupbox-材料用量
        self.materialGroupBox =QGroupBox()
        self.materialGroupBox.setTitle(_translate("Form", "单位体积混凝土中的材料用量(kg/m3)"))        
        #布局放在groupBox中
        self.cementLabel =QLabel()
        self.cementLabel.setText(_translate("Form", "水泥"))  
        self.cementLineEdit = QLineEdit()  

        self.ashLabel =QLabel()
        self.ashLabel.setText(_translate("Form", "粉煤灰"))  
        self.ashLineEdit = QLineEdit() 
        
        self.slagLabel =QLabel()
        self.slagLabel.setText(_translate("Form", "矿渣"))  
        self.slagLineEdit = QLineEdit()         
        
        self.materialVerticalLayout = QVBoxLayout(self.materialGroupBox)
        self.materialVerticalLayout.addWidget(self.cementLabel)
        self.materialVerticalLayout.addWidget(self.cementLineEdit)     
        self.materialVerticalLayout.addWidget(self.ashLabel)
        self.materialVerticalLayout.addWidget(self.ashLineEdit)    
        self.materialVerticalLayout.addWidget(self.slagLabel)
        self.materialVerticalLayout.addWidget(self.slagLineEdit)   
        
        
       #3-3第2个groupbox-养护条件
        self.maintainGroupBox =QGroupBox()
        self.maintainGroupBox.setTitle(_translate("Form", "浇筑养护条件"))        
        #布局放在groupBox中  
        self.concreteTempLabel =QLabel()
        self.concreteTempLabel.setText(_translate("Form", "混凝土入模温度"))  
        self.concreteTempLineEdit = QLineEdit()    
        self.coverLabel =QLabel()
        self.coverLabel.setText(_translate("Form", "基础表面是否覆盖保温层")) 
        
        self.coverHorizontalLayout=QHBoxLayout()
        self.converYesCheckBox =QCheckBox()
        self.converYesCheckBox.setText(_translate("Form", "是"))        
        self.coverNoCheckBox =  QCheckBox()    
        self.coverNoCheckBox.setText(_translate("Form", "否"))        
        self.coverHorizontalLayout.addWidget(self.converYesCheckBox)
        self.coverHorizontalLayout.addWidget(self.coverNoCheckBox)        
        
        self.maintainVerticalLayout= QVBoxLayout(self.maintainGroupBox)
        self.maintainVerticalLayout.addWidget(self.concreteTempLabel)  
        self.maintainVerticalLayout.addWidget(self.concreteTempLineEdit)  
        self.maintainVerticalLayout.addWidget(self.coverLabel)     
        self.maintainVerticalLayout.addLayout(self.coverHorizontalLayout) 

        #2-中间一个水平布局，放置3个GroupBox
        self.parameterHorizontalLayout =QHBoxLayout()
        self.parameterHorizontalLayout.addWidget(self.baseSizeGroupBox)        
        self.parameterHorizontalLayout.addWidget(self.materialGroupBox)      
        self.parameterHorizontalLayout.addWidget(self.maintainGroupBox) 
        
        #二-冷水参数
        self.WaterGroupBox =QGroupBox()
        self.WaterGroupBox.setTitle(_translate("Form", "冷却水参数"))        
        #布局放在groupBox中
        self.waterSpeedLabel =QLabel()
        self.waterSpeedLabel.setText(_translate("Form", "冷却水流量（0.8～3.2m3/h)"))  
        self.waterSpeedLineEdit = QLineEdit()  

        self.deltaTempLabel =QLabel()
        self.deltaTempLabel.setText(_translate("Form", "冷却水入管温度与混凝土入模温度之差（0～20℃)"))  
        self.deltaTempLineEdit = QLineEdit() 
        
        self.maxPipeLengthLabel =QLabel()
        self.maxPipeLengthLabel.setText(_translate("Form", "冷却水管最长单圈长度(0～200m)"))  
        self.maxPipeLengthLineEdit = QLineEdit()   
            
        #用form格式排列
                
        self.waterFormLayout = QFormLayout(self.WaterGroupBox)
        self.waterFormLayout.setWidget(0, QFormLayout.LabelRole, self.waterSpeedLabel)
        self.waterFormLayout.setWidget(0, QFormLayout.FieldRole, self.waterSpeedLineEdit)  
        self.waterFormLayout.setWidget(1, QFormLayout.LabelRole, self.deltaTempLabel)
        self.waterFormLayout.setWidget(1, QFormLayout.FieldRole, self.deltaTempLineEdit)       
        self.waterFormLayout.setWidget(2, QFormLayout.LabelRole, self.maxPipeLengthLabel)
        self.waterFormLayout.setWidget(2, QFormLayout.FieldRole, self.maxPipeLengthLineEdit) 
     
        #三-水管布置方式       
        self.PipeArrangeGroupBox =QGroupBox()
        self.PipeArrangeGroupBox.setTitle(_translate("Form", "冷却水管布置方式")) 
      
        self.PipeArrangeYesCheckBox = QCheckBox()  
        self.PipeArrangeNoCheckBox  = QCheckBox()  
        self.PipeArrangeYesCheckBox.setText(_translate("Form", "自动布置"))
        self.PipeArrangeNoCheckBox.setText(_translate("Form", "手动输入"))
        
        self.PipeArrangeHorizontalLayout = QHBoxLayout(self.PipeArrangeGroupBox)
        self.PipeArrangeHorizontalLayout.addWidget(self.PipeArrangeYesCheckBox)
        self.PipeArrangeHorizontalLayout.addWidget(self.PipeArrangeNoCheckBox) 
 
        #四-水管布置方向      
        self.PipeArrangeDirectionGroupBox =QGroupBox()
        self.PipeArrangeDirectionGroupBox.setTitle(_translate("Form", "冷却水管布置方向")) 
      
        self.PipeArrangeXdirectionCheckBox = QCheckBox()  
        self.PipeArrangeYdirectionCheckBox  = QCheckBox()  
        self.PipeArrangeXdirectionCheckBox.setText(_translate("Form", "X方向"))
        self.PipeArrangeYdirectionCheckBox.setText(_translate("Form", "Y方向"))
        
        self.PipeArrangeDirectionLayout = QHBoxLayout(self.PipeArrangeDirectionGroupBox)
        self.PipeArrangeDirectionLayout.addWidget(self.PipeArrangeXdirectionCheckBox)
        self.PipeArrangeDirectionLayout.addWidget(self.PipeArrangeYdirectionCheckBox) 
        
        #五-温差限值℃     
        self.TempMaxGroupBox =QGroupBox()
        self.TempMaxGroupBox.setTitle(_translate("Form", "温差限值℃"))
        
        self.TempMaxLabel =QLabel()
        self.TempMaxLabel.setText(_translate("Form", "表面与中心温差限值"))  
        self.TempMaxLineEdit = QLineEdit() 
        self.TempMaxHLayout = QHBoxLayout(self.TempMaxGroupBox)
        self.TempMaxHLayout.addWidget(self.TempMaxLabel)
        self.TempMaxHLayout.addWidget(self.TempMaxLineEdit)
        
        
        self.PipeLayout = QHBoxLayout()
        self.PipeLayout.addWidget(self.PipeArrangeGroupBox)
        self.PipeLayout.addWidget(self.PipeArrangeDirectionGroupBox)  
        self.PipeLayout.addWidget(self.TempMaxGroupBox)     
        

       #四-确定取消
       
        self.YesNohorizontalLayout=QHBoxLayout()
        self.YesPushButton = QPushButton()    
        self.NoPushButton = QPushButton() 
        self.YesNohorizontalLayout.addItem(spacerItem)
        self.YesNohorizontalLayout.addWidget(self.YesPushButton)
        self.YesNohorizontalLayout.addWidget(self.NoPushButton)               
        self.YesPushButton.setText(_translate("Form", "确定"))
        self.NoPushButton.setText(_translate("Form", "取消"))        

        
        #主体
        self.totalVerticalLayout.addLayout(self.parameterHorizontalLayout)   
        self.totalVerticalLayout.addWidget(self.WaterGroupBox)     
        self.totalVerticalLayout.addLayout(self.PipeLayout)         
        self.totalVerticalLayout.addLayout(self.YesNohorizontalLayout)     
           

if __name__=='__main__':
    app=QApplication(sys.argv)
    ui = UI_tab1_Define_parametere()    
#    ui.setGeometry(100, 100, 800, 600)
    ui.show()
    sys.exit(app.exec_())
