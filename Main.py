# -*- coding: cp1252 -*-

#!/usr/bin/env python

import sys
import DB_manager as db
# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
##
##
##class Ui_Login(QtGui.QDialog):
##    def __init__(self):
##        QtGui.QDialog.__init__(self)
##        self.dbu = db.DatabaseUtility('UsernamePassword_DB', 'masterTable')
##        self.setupUi(self)
##        
##    def setupUi(self, Login_Dialog):
##        Login_Dialog.setObjectName(_fromUtf8("Login_Dialog"))
##        Login_Dialog.resize(285, 134)
##        self.verticalLayout_2 = QtGui.QVBoxLayout(Login_Dialog)
##        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
##        self.verticalLayout = QtGui.QVBoxLayout()
##        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
##        self.groupBox = QtGui.QGroupBox(Login_Dialog)
##        self.groupBox.setObjectName(_fromUtf8("groupBox"))
##        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
##        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
##        self.horizontalLayout = QtGui.QHBoxLayout()
##        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
##        self.label = QtGui.QLabel(self.groupBox)
##        self.label.setObjectName(_fromUtf8("label"))
##        self.horizontalLayout.addWidget(self.label)
##        self.user_lineEdit = QtGui.QLineEdit(self.groupBox)
##        self.user_lineEdit.setObjectName(_fromUtf8("user_lineEdit"))
##        self.horizontalLayout.addWidget(self.user_lineEdit)
##        self.verticalLayout_3.addLayout(self.horizontalLayout)
##        self.horizontalLayout_2 = QtGui.QHBoxLayout()
##        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
##        self.label_2 = QtGui.QLabel(self.groupBox)
##        self.label_2.setObjectName(_fromUtf8("label_2"))
##        self.horizontalLayout_2.addWidget(self.label_2)
##        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
##        self.password_lineEdit.setInputMask(_fromUtf8(""))
##        self.password_lineEdit.setText(_fromUtf8(""))
##        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
##        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
##        self.horizontalLayout_2.addWidget(self.password_lineEdit)
##        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
##        self.horizontalLayout_4 = QtGui.QHBoxLayout()
##        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
##        self.newUser_btn = QtGui.QPushButton(self.groupBox)
##        self.newUser_btn.setObjectName(_fromUtf8("newUser_btn"))
##        self.horizontalLayout_4.addWidget(self.newUser_btn)
##        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
##        self.horizontalLayout_4.addItem(spacerItem)
##        self.login_btn = QtGui.QPushButton(self.groupBox)
##        self.login_btn.setObjectName(_fromUtf8("login_btn"))
##        self.horizontalLayout_4.addWidget(self.login_btn)
##        self.cancel_btn = QtGui.QPushButton(self.groupBox)
##        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
##        self.horizontalLayout_4.addWidget(self.cancel_btn)
##        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
##        self.verticalLayout.addWidget(self.groupBox)
##        self.verticalLayout_2.addLayout(self.verticalLayout)
##
##        self.retranslateUi(Login_Dialog)
##        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)
##
##    def retranslateUi(self, Login_Dialog):
##        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Daniel\'s User login", None))
##        self.groupBox.setTitle(_translate("Login_Dialog", "Simulation!", None))
##        self.label.setText(_translate("Login_Dialog", "Username", None))
##        self.label_2.setText(_translate("Login_Dialog", "Password", None))
##        self.newUser_btn.setText(_translate("Login_Dialog", "New User", None))
##        self.login_btn.setText(_translate("Login_Dialog", "Login", None))
##        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel", None))
##
##
##    @QtCore.pyqtSignature("on_cancel_btn_clicked()")
##    def Cancel_btn(self):
##        self.close()
##
##    @QtCore.pyqtSignature("on_login_btn_clicked()")
##    def Login_btn(self):
##        username = self.user_lineEdit.text()
##        password = self.password_lineEdit.text()
##        if not username:
##            QtGui.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
##        elif not password:
##            QtGui.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
##        else:
##            self.AttemptLogin(username, password)
##
##    def AttemptLogin(self, username, password):
##        t = self.dbu.GetTable()
##        print (t)
##        for col in t:
##            if username == col[1]:
##                if password == col[2]:
##                    QtGui.QMessageBox.information(self, 'BOOYA!', 'Success!!')
##                    self.services = Ui_MainWindow(self)
##                    self.services.show()
##                    self.close()
##                else:
##                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
##                    return
##
##    @QtCore.pyqtSignature("on_newUser_btn_clicked()")
##    def NewUser_btn(self):
##        self.newUser = Ui_Register(self.dbu)
##        self.newUser.show()
##
##class Ui_Register(QtGui.QDialog):
##    def __init__(self, dbu):
##        QtGui.QDialog.__init__(self)
##        self.setupUi(self)
##        self.dbu = dbu
##
##    def setupUi(self, Register_Dialog):
##        Register_Dialog.setObjectName(_fromUtf8("Register_Dialog"))
##        Register_Dialog.resize(372, 187)
##        Register_Dialog.setModal(True)
##        self.verticalLayout_2 = QtGui.QVBoxLayout(Register_Dialog)
##        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
##        self.verticalLayout = QtGui.QVBoxLayout()
##        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
##        self.groupBox = QtGui.QGroupBox(Register_Dialog)
##        self.groupBox.setObjectName(_fromUtf8("groupBox"))
##        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
##        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
##        self.horizontalLayout = QtGui.QHBoxLayout()
##        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
##        self.label_2 = QtGui.QLabel(self.groupBox)
##        self.label_2.setObjectName(_fromUtf8("label_2"))
##        self.horizontalLayout.addWidget(self.label_2)
##        self.username_lineEdit = QtGui.QLineEdit(self.groupBox)
##        self.username_lineEdit.setObjectName(_fromUtf8("username_lineEdit"))
##        self.horizontalLayout.addWidget(self.username_lineEdit)
##        self.verticalLayout_3.addLayout(self.horizontalLayout)
##        self.horizontalLayout_2 = QtGui.QHBoxLayout()
##        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
##        self.label = QtGui.QLabel(self.groupBox)
##        self.label.setObjectName(_fromUtf8("label"))
##        self.horizontalLayout_2.addWidget(self.label)
##        self.password_lineEdit = QtGui.QLineEdit(self.groupBox)
##        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
##        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
##        self.horizontalLayout_2.addWidget(self.password_lineEdit)
##        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
##        self.horizontalLayout_4 = QtGui.QHBoxLayout()
##        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
##        self.label_3 = QtGui.QLabel(self.groupBox)
##        self.label_3.setObjectName(_fromUtf8("label_3"))
##        self.horizontalLayout_4.addWidget(self.label_3)
##        self.confirmPassword_lineEdit = QtGui.QLineEdit(self.groupBox)
##        self.confirmPassword_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
##        self.confirmPassword_lineEdit.setObjectName(_fromUtf8("confirmPassword_lineEdit"))
##        self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
##        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
##        self.label_4 = QtGui.QLabel(self.groupBox)
##        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
##        self.label_4.setObjectName(_fromUtf8("label_4"))
##        self.verticalLayout_3.addWidget(self.label_4)
##        self.horizontalLayout_3 = QtGui.QHBoxLayout()
##        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
##        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
##        self.horizontalLayout_3.addItem(spacerItem)
##        self.add_btn = QtGui.QPushButton(self.groupBox)
##        self.add_btn.setObjectName(_fromUtf8("add_btn"))
##        self.horizontalLayout_3.addWidget(self.add_btn)
##        self.cancel_btn = QtGui.QPushButton(self.groupBox)
##        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
##        self.horizontalLayout_3.addWidget(self.cancel_btn)
##        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
##        self.verticalLayout.addWidget(self.groupBox)
##        self.verticalLayout_2.addLayout(self.verticalLayout)
##
##        self.retranslateUi(Register_Dialog)
##        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)
##
##    def retranslateUi(self, Register_Dialog):
##        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register New User", None))
##        self.groupBox.setTitle(_translate("Register_Dialog", "I Love Ham!", None))
##        self.label_2.setText(_translate("Register_Dialog", "Username", None))
##        self.label.setText(_translate("Register_Dialog", "Password", None))
##        self.label_3.setText(_translate("Register_Dialog", "Confirm Password", None))
##        self.label_4.setText(_translate("Register_Dialog", "Not Included: Phone, Address, Social Security Number, Credit Card...", None))
##        self.add_btn.setText(_translate("Register_Dialog", "Add", None))
##        self.cancel_btn.setText(_translate("Register_Dialog", "Cancel", None))
##
##
##    @QtCore.pyqtSignature("on_cancel_btn_clicked()")
##    def Cancel_btn(self):
##        self.close()
##
##    @QtCore.pyqtSignature("on_add_btn_clicked()")
##    def Add_btn(self):
##        username = self.username_lineEdit.text()
##        password = self.password_lineEdit.text()
##        cpassword = self.confirmPassword_lineEdit.text()
##        if not username:
##            QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Missing')
##        elif password != cpassword:
##            QtGui.QMessageBox.warning(self, 'Dang it!', 'Passwords Do Not Match')
##        else:
##            t = self.dbu.GetTable()
##            print (t)
##            for col in t:
##                if username == col[1]:
##                    QtGui.QMessageBox.warning(self, 'Dang it!', 'Username Taken. :(')
##            else:
##                self.dbu.AddEntryToTable (username, password)
##                QtGui.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
##                self.close()

import pylab
from ps8 import *
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1433, 723)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 110, 571, 211))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 160, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.simpleSimLabel = QtGui.QLabel(self.frame)
        self.simpleSimLabel.setGeometry(QtCore.QRect(10, 0, 301, 211))
        self.simpleSimLabel.setText(_fromUtf8(""))
        self.simpleSimLabel.setPixmap(QtGui.QPixmap(_fromUtf8("../../Documents/insuranc.jpg")))
        self.simpleSimLabel.setObjectName(_fromUtf8("simpleSimLabel"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 231, 141))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 30, 401, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(800, 110, 591, 211))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(310, 160, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(300, -10, 271, 171))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 281, 161))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("../../Documents/insurance image8.jpg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(210, 350, 571, 211))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(330, 20, 241, 121))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 170, 231, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 15, 301, 181))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("../../Documents/insurance image7.jpg")))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 40, 181, 591))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 20, 141, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 220, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 360, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 500, 141, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.frame_4)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(800, 350, 591, 211))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.pushButton_12 = QtGui.QPushButton(self.frame_5)
        self.pushButton_12.setGeometry(QtCore.QRect(320, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.label_8 = QtGui.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(310, 20, 231, 111))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(5, 30, 271, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("../../Documents/insurance image2.jpg")))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1433, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave_all = QtGui.QAction(MainWindow)
        self.actionSave_all.setObjectName(_fromUtf8("actionSave_all"))
        self.actionIndent_Here = QtGui.QAction(MainWindow)
        self.actionIndent_Here.setObjectName(_fromUtf8("actionIndent_Here"))
        self.actionDedent_here = QtGui.QAction(MainWindow)
        self.actionDedent_here.setObjectName(_fromUtf8("actionDedent_here"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_all)
        self.menuEdit.addAction(self.actionIndent_Here)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDedent_here)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Simple Simulation", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Here, the patient does not take</span></p><p><span style=\" font-size:12pt; color:#0000ff;\">any drugs and the viruses</span></p><p><span style=\" font-size:12pt; color:#0000ff;\">do not acquire resistance to </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">drugs</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">RESEARCH SERVICES</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">Below are some of our services.</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">You can find more services at the services tab</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Simulation with drug", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Here, we consider the effects of both </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">administering drugs to the patient</span></p><p><span style=\" font-size:12pt; color:#0000ff;\">and the ability of virus particle </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">offspring to inherit or mutate.</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">Here,we explore the effect ofdelaying </span></p><p><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">treatment on the ability of the </span></p><p><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">drug to eradicate the virus </span></p><p><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">population.</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("MainWindow", "Delayed Treatment", None))
        self.pushButton_4.setText(_translate("MainWindow", "Welcome", None))
        self.pushButton_5.setText(_translate("MainWindow", "Sign in", None))
        self.pushButton_6.setText(_translate("MainWindow", "Simple Sim", None))
        self.pushButton_7.setText(_translate("MainWindow", "SimDrug", None))
        self.pushButton_8.setText(_translate("MainWindow", "DelayedTreat", None))
        self.pushButton_9.setText(_translate("MainWindow", "TwoDrugs", None))
        self.pushButton_10.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_11.setText(_translate("MainWindow", "Log out", None))
        self.pushButton_12.setText(_translate("MainWindow", "2 independent drugs", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Here,we use two </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">independently-acting </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">drugs to treat the virus.</span></p></body></html>", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionSave_all.setText(_translate("MainWindow", "Save all", None))
        self.actionIndent_Here.setText(_translate("MainWindow", "Indent Here", None))
        self.actionDedent_here.setText(_translate("MainWindow", "Dedent here", None))
        self.pushButton_2.clicked.connect(self.openForm)
        self.pushButton_6.clicked.connect(self.openForm)
        self.pushButton_7.clicked.connect(self.openForm1)
        self.pushButton.clicked.connect(self.openForm1)
        self.pushButton_3.clicked.connect(self.openForm4)
        self.pushButton_8.clicked.connect(self.openForm4)
        self.pushButton_9.clicked.connect(self.openForm3)
        self.pushButton_12.clicked.connect(self.openForm3)
        self.pushButton_5.clicked.connect(self.openForm5)
        self.pushButton_11.clicked.connect(self.openForm5)
        self.pushButton_10.clicked.connect(self.openForm6)

    def openForm(self):
        self.parameter = Ui_Form(self)
        self.parameter.show()
    def openForm1(self):
        self.parameter1 = Ui_Form1(self)
        self.parameter1.show()
    def openForm3(self):
        self.parameter3 = Ui_Form3(self)
        self.parameter3.show()
    def openForm4(self):
        self.parameter4 = Ui_Form4(self)
        self.parameter4.show()
    def openForm5(self):
        self.parameter5 = Ui_Login()
        self.parameter5.show()
        self.close()
    def openForm6(self):
        self.close()
    
      



class Ui_Form(QtGui.QWidget):
    def __init__(self,dbu):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.theViruses = 100.0
        self.maxipop = 1000.0
        self.maxibirthpop = 0.1
        self.clearingprob = 0.05
        self.timesteps = 300
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(619, 641)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 70, 501, 111))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 281, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(340, 70, 151, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 20, 151, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 511, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 491, 91))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(30, 290, 501, 161))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 261, 61))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 30, 151, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 241, 51))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 100, 151, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 480, 231, 61))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(370, 500, 151, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 570, 201, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Viruses</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum sustainable virus population</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">SimplePatient should be instantiated with the following parameters:</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Each SimpleVirus instance in the viruses list should be initialized </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">with the following parameters</span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum Reproduction </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">Probability for a Virus Particle</span></p></body></html>", None))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum Clearance</span></p><p><span style=\" font-size:12pt; color:#0000ff;\">Probability for a Virus Particle</span></p></body></html>", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">The number of time steps </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">on which to simulate change</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "Run simulation", None))
        self.pushButton.clicked.connect(self.getValues)
        

    def getValues(self):
        self.theViruses = float(self.lineEdit_2.text())
        self.maxipop = float(self.lineEdit.text())
        self.maxibirthpop = float(self.lineEdit_3.text())
        self.clearingprob = float(self.lineEdit_4.text())
        self.timesteps = float(self.lineEdit_5.text())
        simulationWithoutDrug(self.theViruses,self.maxipop,self.maxibirthpop,self.clearingprob,self.timesteps)


class Ui_Form1(QtGui.QWidget):
    def __init__(self,dbu):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.theViruses = 100.0
        self.maxipop = 1000.0
        self.maxibirthpop = 0.1
        self.clearingprob = 0.05
        self.timesteps = 300

    def setupUi(self, Form1):
        Form1.setObjectName(_fromUtf8("Form1"))
        Form1.resize(722, 738)
        self.pushButton = QtGui.QPushButton(Form1)
        self.pushButton.setGeometry(QtCore.QRect(400, 690, 201, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Form1)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 511, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_2 = QtGui.QFrame(Form1)
        self.frame_2.setGeometry(QtCore.QRect(80, 290, 501, 291))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 261, 61))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 30, 151, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 241, 51))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 100, 151, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_12 = QtGui.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 160, 281, 51))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_10 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(340, 170, 151, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 230, 231, 51))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_11 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(340, 240, 151, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_7 = QtGui.QLineEdit(Form1)
        self.lineEdit_7.setGeometry(QtCore.QRect(420, 620, 151, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.frame = QtGui.QFrame(Form1)
        self.frame.setGeometry(QtCore.QRect(80, 70, 501, 111))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 281, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_8 = QtGui.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 70, 151, 21))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 20, 151, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_10 = QtGui.QLabel(Form1)
        self.label_10.setGeometry(QtCore.QRect(80, 590, 231, 61))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form1)
        self.label_11.setGeometry(QtCore.QRect(80, 200, 491, 91))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(_translate("Form1", "Form", None))
        self.pushButton.setText(_translate("Form1", "Run simulation", None))
        self.label_2.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Patient should be instantiated with the following parameters:</span></p></body></html>", None))
        self.label_7.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum Reproduction </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">Probability for a Virus Particle</span></p></body></html>", None))
        self.label_8.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum Clearance</span></p><p><span style=\" font-size:12pt; color:#0000ff;\">Probability for a Virus Particle</span></p></body></html>", None))
        self.label_12.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Drugs to include in experiment</span></p></body></html>", None))
        self.label_13.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Probability of a mutation in a </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">virus particle’s offspring</span></p></body></html>", None))
        self.label_4.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Viruses</span></p></body></html>", None))
        self.label_9.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum sustainable virus population</span></p></body></html>", None))
        self.label_10.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">The number of time steps </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">on which to simulate change</span></p></body></html>", None))
        self.label_11.setText(_translate("Form1", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Each ResistantVirus instance in the viruses list should be initialized </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">with the following parameters</span></p></body></html>", None))
        self.pushButton.clicked.connect(self.getValues)
    def getValues(self):
        self.theViruses = float(self.lineEdit_9.text())
        self.maxipop = float(self.lineEdit_8.text())
        self.maxibirthpop = float(self.lineEdit_5.text())
        self.clearingprob = float(self.lineEdit_6.text())
        self.timesteps = float(self.lineEdit_7.text())
        self.mutprob = float(self.lineEdit_11.text())
        simulationWithDrug(self.theViruses,self.maxipop,self.maxibirthpop,self.clearingprob,self.timesteps,self.mutprob)
    

class Ui_Form3(QtGui.QWidget):
    def __init__(self,dbu):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.theViruses = 100.0
        self.maxipop = 1000.0
        self.maxibirthpop = 0.1
        self.clearingprob = 0.05
        self.timesteps = 300
    def setupUi(self, Form3):
        Form3.setObjectName(_fromUtf8("Form3"))
        Form3.resize(836, 733)
        self.lineEdit_7 = QtGui.QLineEdit(Form3)
        self.lineEdit_7.setGeometry(QtCore.QRect(400, 630, 151, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.frame = QtGui.QFrame(Form3)
        self.frame.setGeometry(QtCore.QRect(60, 80, 501, 111))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 281, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_8 = QtGui.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 70, 151, 21))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 20, 151, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_2 = QtGui.QLabel(Form3)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 511, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_2 = QtGui.QFrame(Form3)
        self.frame_2.setGeometry(QtCore.QRect(60, 300, 501, 291))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 261, 61))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 30, 151, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 241, 51))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 100, 151, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_12 = QtGui.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 160, 281, 51))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_10 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(340, 170, 151, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 230, 231, 51))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_11 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(340, 240, 151, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.pushButton = QtGui.QPushButton(Form3)
        self.pushButton.setGeometry(QtCore.QRect(600, 610, 201, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_10 = QtGui.QLabel(Form3)
        self.label_10.setGeometry(QtCore.QRect(60, 600, 231, 61))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form3)
        self.label_11.setGeometry(QtCore.QRect(60, 210, 491, 91))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(_translate("Form3", "Form", None))
        self.label_4.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Viruses</span></p></body></html>", None))
        self.label_9.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum sustainable virus population</span></p></body></html>", None))
        self.label_2.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Patient should be instantiated with the following parameters:</span></p></body></html>", None))
        self.label_7.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum Reproduction </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">Probability for a Virus Particle</span></p></body></html>", None))
        self.label_8.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Maximum Clearance</span></p><p><span style=\" font-size:12pt; color:#0000ff;\">Probability for a Virus Particle</span></p></body></html>", None))
        self.label_12.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Drugs to include in experiment</span></p></body></html>", None))
        self.label_13.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Probability of a mutation in a </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">virus particle\'s offspring</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form3", "Run simulation", None))
        self.label_10.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">The number of time steps </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">on which to simulate change</span></p></body></html>", None))
        self.label_11.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Each ResistantVirus instance in the viruses list should be initialized </span></p><p><span style=\" font-size:12pt; color:#0000ff;\">with the following parameters</span></p></body></html>", None))
        self.pushButton.clicked.connect(self.getValues)
    def getValues(self):
        self.theViruses = float(self.lineEdit_9.text())
        self.maxipop = float(self.lineEdit_8.text())
        self.maxibirthpop = float(self.lineEdit_5.text())
        self.clearingprob = float(self.lineEdit_6.text())
        self.timesteps = float(self.lineEdit_7.text())
        self.mutprob = float(self.lineEdit_11.text())
        simulationTwoDrugsDelayedTreatment(self.theViruses,self.maxipop,self.maxibirthpop,self.clearingprob,self.timesteps,self.mutprob)


class Ui_Form4(QtGui.QWidget):
    def __init__(self,dbu):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.timestepsBefore = 300
        self.timestepsAfter = 450
        
    def setupUi(self, Form4):
        Form4.setObjectName(_fromUtf8("Form4"))
        Form4.resize(846, 573)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        Form4.setFont(font)
        self.label = QtGui.QLabel(Form4)
        self.label.setGeometry(QtCore.QRect(50, 50, 471, 241))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form4)
        self.lineEdit.setGeometry(QtCore.QRect(430, 320, 191, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Form4)
        self.label_2.setGeometry(QtCore.QRect(50, 310, 341, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form4)
        self.pushButton.setGeometry(QtCore.QRect(370, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Book Antiqua"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form4)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 510, 151, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Form4)
        self.label_3.setGeometry(QtCore.QRect(50, 360, 301, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Form4)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 370, 191, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        Form4.setWindowTitle(_translate("Form4", "Form", None))
        self.label.setText(_translate("Form4", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; font-style:normal; color:#0000ff;\">Here, we will explore the effect ofdelaying treatment on the</span></p><p><span style=\" font-size:12pt; font-weight:400; font-style:normal; color:#0000ff;\">ability of the drug to eradicate the virus population.</span></p><p><span style=\" font-size:12pt; font-weight:400; font-style:normal; color:#0000ff;\">We will run a simulation to observe </span></p><p><span style=\" font-size:12pt; font-weight:400; font-style:normal; color:#0000ff;\">trends in the distributions of patient outcomes.</span></p></body></html>", None))
        self.label_2.setText(_translate("Form4", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; font-style:normal; color:#0000ff;\">Timesteps before administering treatment</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form4", "Run Simulation", None))
        self.pushButton_2.setText(_translate("Form4", "Back", None))
        self.label_3.setText(_translate("Form4", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; font-style:normal; color:#0000ff;\">Timesteps after administering Treatment</span></p></body></html>", None))
        self.pushButton.clicked.connect(self.getValues)

    def getValues(self):
        self.timestepsBefore = int(self.lineEdit.text())
        self.timestepsAfter = int(self.lineEdit_2.text())
        simulationDelayedTreatment(self.timestepsBefore,self.timestepsAfter)
        
def simulationTwoDrugsDelayedTreatment(virus,maxPop,maxBirthProb,clearProb,timestep,mutProb):

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    viruses = []
    timesteps = []
    finalViruses = []
    
    resistances = {'guttagonol':False, 'grimpex':False}
    pbar = QtGui.QProgressBar()
    pbar.setGeometry(500,300,250,20)
    pbar.setAutoFillBackground(True)
    pbar.show()
    
    reps = 20
    timeBeforeGuttagonol = 150
    timeBeforeGrimpex = 150
    timeAfterDrugs = 150
    xmin = 0
    xmax = 450
    ymin = 0
    ymax = reps
    
    patient = Patient(viruses, maxPop)
    for time in range(timeBeforeGrimpex + timeAfterDrugs):
        timesteps.append(time)
    for rep in range(reps):
        print "Patient number #",reps
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))    
        for y in range(timeBeforeGuttagonol):
            patient.update()
        patient.addPrescription('guttagonol')
        for x in range(timeBeforeGuttagonol, timeBeforeGuttagonol + timeBeforeGrimpex):
            patient.update()
        patient.addPrescription('grimpex')
        for z in range(timeBeforeGrimpex, timeBeforeGuttagonol + timeBeforeGrimpex + timeAfterDrugs):
            patient.update()
        finalViruses.append(patient.update())
        print "Total viruses",finalViruses
        pbar.setValue(rep)
    pylab.hist(finalViruses, 10)
    axes = pylab.gca()
    axes.set_xlim([xmin,xmax])
    axes.set_ylim([ymin,ymax])
    pylab.title('Viruses after 300 Timesteps')
    pylab.xlabel('# of Viruses')
    pylab.ylabel('# of Patients')
    pylab.show()
    
def simulationDelayedTreatment(timeBeforeDrug,timeAfterDrug):

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    pbar1 = QtGui.QProgressBar()
    pbar1.setGeometry(500,300,250,20)
    pbar1.setAutoFillBackground(True)
    pbar1.show()

    xmin = 0
    xmax = 450
    ymin = 0
 
    

    #initiate parameters
    finalViruses = []
    viruses = []
    timesteps = []
    resistances = {'guttagonol' : False}
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    mutProb = 0.005
    #number of trials to take the average of
    reps = 20
    ymax = reps
    #create our patient
    patient = Patient(viruses, maxPop)
    #timesteps will have all the times in our range
    for time in range(timeBeforeDrug + timeAfterDrug):
        timesteps.append(time)
    #run simulation 'reps' times
    for rep in range(reps):
        "patient number ",rep
        #initiate 100 viruses
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        for j in range(timeBeforeDrug):
            patient.update()
        #prescribe guttagonol
        patient.addPrescription('guttagonol')
        for k in range(timeBeforeDrug, timeBeforeDrug+timeAfterDrug):
            patient.update()
        finalViruses.append(patient.update())
        "Number of viruses:",finalViruses[rep]," for patient #",rep
        "Total viruses:",finalViruses
        pbar1.setValue(int(float(rep)/float(reps) * 100))
    pylab.hist(finalViruses, 10)
    
    pylab.title('100 patients -- timesteps before treatment,timesteps after treatment')
    pylab.xlabel('# of Viruses')
    pylab.ylabel('# of Patients')
    pylab.show()

def simulationWithoutDrug(virus,maxPop,maxBirthProb,clearProb,timestep):

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    pbar2 = QtGui.QProgressBar()
    pbar2.setGeometry(500,300,250,20)
    pbar2.setAutoFillBackground(True)
    pbar2.show()
    #create lists for viruses, timesteps, and numbers of viruses
    viruses = []
    timesteps = []
    numbers = []
    #set max population, max birthrate, and probability of death
    #initiate patient
    patient = SimplePatient(viruses, maxPop)
    #initiate a list of 100 viruses
    for i in range(100):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    #create list of virus counts corresponding to each of 300 timesteps
    for j in range(300):
        timesteps.append(j)
        numbers.append(patient.update())
        pbar2.setValue(int(float(j)/float(300)) * 100)
    ###USED FOR GRAPH:
    ###return numbers
    #graph virus population against time
    pylab.plot(timesteps, numbers)
    pylab.title('Virus Population Change Over Time')
    pylab.xlabel('# of Timesteps Elapsed')
    pylab.ylabel('Virus Population')
    pylab.show()
      
def simulationWithDrug(virus,maxPop,maxBirthProb,clearProb,times,mutProb):

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    pbar3 = QtGui.QProgressBar()
    pbar3.setGeometry(500,300,250,20)
    pbar3.setAutoFillBackground(True)
    pbar3.show()
    #initiate lists for plotting purposes
    allViruses = []
    resistantViruses = []
    averageViruses = []
    averageResistantViruses = []
    #initiate parameters
    viruses = []
    timesteps = []
    resistances = {'guttagonol' : False}
    timeBeforeDrug = 150
    timeAfterDrug = 150
    #number of trials to take the average of
    reps = 1
    #create our patient
    patient = Patient(viruses, maxPop)
    #set up our lists
    #timesteps will have all the times in our range
    #allViruses and resistantViruses start out with 0 for each time
    for time in range(timeBeforeDrug + timeAfterDrug):
        timesteps.append(time)
        allViruses.append(0)
        resistantViruses.append(0)
        averageViruses.append(0)
        averageResistantViruses.append(0)
    #run simulation 'reps' times
    for rep in range(reps):
        #initiate 100 viruses
        for i in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        #add to totals for each timestep before guttagonol is prescribed
        for j in range(timeBeforeDrug):
            allViruses[j] += patient.update()
            resistantViruses[j] += patient.getResistPop(['guttagonol'])
        #prescribe guttagonol
        patient.addPrescription('guttagonol')
        #add to totals for each timestep after guttagonol is prescribed
        for k in range(timeBeforeDrug, timeBeforeDrug+timeAfterDrug):
            allViruses[k] += patient.update()
            resistantViruses[k] += patient.getResistPop(['guttagonol'])
        pbar3.setValue(int(float(rep)/float(reps)) * 100)
    #average values for each timestep over number of trials
    print allViruses
    print resistantViruses
    for time in range(timeBeforeDrug + timeAfterDrug):
        averageViruses[time] = float(allViruses[time])/reps
        averageResistantViruses[time] = float(resistantViruses[time])/reps
    #plot both graphs
    pylab.plot(timesteps, averageViruses)
    pylab.plot(timesteps, averageResistantViruses)
    pylab.title('Virus Population Change over Time')
    pylab.xlabel('# of Timesteps Elapsed')
    pylab.legend(('Viruses', 'Resistant Viruses'))
    pylab.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
