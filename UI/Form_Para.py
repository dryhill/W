# -*- coding: utf-8 -*-

"""
Module implementing Form_Para.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from .Ui_para import Ui_Form


class Form_Para(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form_Para, self).__init__(parent)
        self.setupUi(self)
