# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/haobk/Desktop/Mydata/FaceService/face_client/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1473, 926)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:rgb(91,90,90);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toodle = QtWidgets.QFrame(self.frame_top)
        self.frame_toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.frame_toodle.setStyleSheet("background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_toodle.setObjectName("frame_toodle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toodle = QtWidgets.QPushButton(self.frame_toodle)
        self.toodle.setMinimumSize(QtCore.QSize(80, 55))
        self.toodle.setMaximumSize(QtCore.QSize(80, 55))
        self.toodle.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.toodle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/haobk/Desktop/Mydata/FaceService/face_client/ui/icons/1x/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QtCore.QSize(22, 12))
        self.toodle.setFlat(True)
        self.toodle.setObjectName("toodle")
        self.horizontalLayout_3.addWidget(self.toodle)
        self.horizontalLayout.addWidget(self.frame_toodle)
        self.frame_top_east = QtWidgets.QFrame(self.frame_top)
        self.frame_top_east.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_top_east.setStyleSheet("background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top_east.setObjectName("frame_top_east")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_appname = QtWidgets.QFrame(self.frame_top_east)
        self.frame_appname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_appname.setObjectName("frame_appname")
        self.lab_appname = QtWidgets.QLabel(self.frame_appname)
        self.lab_appname.setGeometry(QtCore.QRect(0, 0, 669, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet("color:rgb(255,255,255);")
        self.lab_appname.setObjectName("lab_appname")
        self.horizontalLayout_4.addWidget(self.frame_appname)
        self.frame_user = QtWidgets.QFrame(self.frame_top_east)
        self.frame_user.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_user.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_user.setObjectName("frame_user")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lab_user = QtWidgets.QLabel(self.frame_user)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user.setObjectName("lab_user")
        self.horizontalLayout_9.addWidget(self.lab_user)
        self.horizontalLayout_4.addWidget(self.frame_user)
        self.frame_person = QtWidgets.QFrame(self.frame_top_east)
        self.frame_person.setMinimumSize(QtCore.QSize(55, 55))
        self.frame_person.setMaximumSize(QtCore.QSize(55, 55))
        self.frame_person.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_person.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_person.setObjectName("frame_person")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lab_person = QtWidgets.QLabel(self.frame_person)
        self.lab_person.setMaximumSize(QtCore.QSize(55, 55))
        self.lab_person.setText("")
        self.lab_person.setPixmap(QtGui.QPixmap("/home/haobk/Desktop/Mydata/FaceService/face_client/ui/icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_person.setObjectName("lab_person")
        self.horizontalLayout_8.addWidget(self.lab_person)
        self.horizontalLayout_4.addWidget(self.frame_person)
        self.horizontalLayout.addWidget(self.frame_top_east)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_bottom_west = QtWidgets.QFrame(self.frame_bottom)
        self.frame_bottom_west.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet("background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_west.setObjectName("frame_bottom_west")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_login = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_login.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_login.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_login.setObjectName("frame_login")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_login)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bn_login = QtWidgets.QPushButton(self.frame_login)
        self.bn_login.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_login.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_login.setAutoFillBackground(False)
        self.bn_login.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/haobk/Desktop/Mydata/FaceService/face_client/ui/icons/custom/icons8-login-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_login.setIcon(icon1)
        self.bn_login.setIconSize(QtCore.QSize(40, 40))
        self.bn_login.setCheckable(False)
        self.bn_login.setAutoRepeat(False)
        self.bn_login.setFlat(True)
        self.bn_login.setObjectName("bn_login")
        self.horizontalLayout_6.addWidget(self.bn_login, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.frame_login)
        self.frame_page_1 = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_page_1.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_page_1.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_page_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_page_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_page_1.setObjectName("frame_page_1")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_page_1)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.bn_page_1 = QtWidgets.QPushButton(self.frame_page_1)
        self.bn_page_1.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_page_1.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_page_1.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/haobk/Desktop/Mydata/FaceService/face_client/ui/icons/custom/icons8-device-manager-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_page_1.setIcon(icon2)
        self.bn_page_1.setIconSize(QtCore.QSize(30, 30))
        self.bn_page_1.setFlat(True)
        self.bn_page_1.setObjectName("bn_page_1")
        self.horizontalLayout_16.addWidget(self.bn_page_1, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.frame_page_1)
        self.frame_face_register = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_face_register.setMinimumSize(QtCore.QSize(80, 55))
        self.frame_face_register.setMaximumSize(QtCore.QSize(160, 55))
        self.frame_face_register.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_face_register.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_face_register.setObjectName("frame_face_register")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_face_register)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.bn_face_register = QtWidgets.QPushButton(self.frame_face_register)
        self.bn_face_register.setMinimumSize(QtCore.QSize(80, 55))
        self.bn_face_register.setMaximumSize(QtCore.QSize(160, 55))
        self.bn_face_register.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/haobk/Desktop/Mydata/FaceService/face_client/ui/icons/custom/icons8-fit-to-width-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_face_register.setIcon(icon3)
        self.bn_face_register.setIconSize(QtCore.QSize(30, 30))
        self.bn_face_register.setFlat(True)
        self.bn_face_register.setObjectName("bn_face_register")
        self.horizontalLayout_17.addWidget(self.bn_face_register)
        self.verticalLayout_3.addWidget(self.frame_face_register)
        self.frame_8 = QtWidgets.QFrame(self.frame_bottom_west)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame_bottom_west)
        self.frame_bottom_east = QtWidgets.QFrame(self.frame_bottom)
        self.frame_bottom_east.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_bottom_east.setObjectName("frame_bottom_east")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_bottom_east)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 55))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setStyleSheet("background:rgb(91,90,90);")
        self.page_login.setObjectName("page_login")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.wget_title_home = QtWidgets.QWidget(self.page_login)
        self.wget_title_home.setMaximumSize(QtCore.QSize(16777215, 80))
        self.wget_title_home.setObjectName("wget_title_home")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.wget_title_home)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label = QtWidgets.QLabel(self.wget_title_home)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"QLabel {\n"
"    font-size: 50px;\n"
"    font-weight: bold;\n"
"    color: #333333;\n"
"color:rgb(255,255,255);\n"
"font:  \"Times New Roman\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_36.addWidget(self.label)
        self.verticalLayout_18.addWidget(self.wget_title_home)
        self.wget_login = QtWidgets.QWidget(self.page_login)
        self.wget_login.setObjectName("wget_login")
        self.gridLayout = QtWidgets.QGridLayout(self.wget_login)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_5 = QtWidgets.QWidget(self.wget_login)
        self.widget_5.setMinimumSize(QtCore.QSize(500, 300))
        self.widget_5.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget_5.setStyleSheet("QWidget {\n"
"        background-color: #f5f5f5;\n"
"    border-radius: 8px;\n"
"\n"
"    }\n"
"\n"
"    QLabel {\n"
"        font-size: 18px;\n"
"        color: #333333;\n"
"    }\n"
"\n"
"    QLineEdit {\n"
"        padding: 8px;\n"
"        font-size: 16px;\n"
"        border: 1px solid #cccccc;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        padding: 8px 16px;\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"        color: #ffffff;\n"
"        background-color: #3498db;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #1e87c7;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #136793;\n"
"    }")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.widget_12 = QtWidgets.QWidget(self.widget_5)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_39 = QtWidgets.QLabel(self.widget_12)
        self.label_39.setMinimumSize(QtCore.QSize(150, 0))
        self.label_39.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_31.addWidget(self.label_39)
        self.bt_ip = QtWidgets.QLineEdit(self.widget_12)
        self.bt_ip.setObjectName("bt_ip")
        self.horizontalLayout_31.addWidget(self.bt_ip)
        self.verticalLayout_19.addWidget(self.widget_12)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_35 = QtWidgets.QLabel(self.widget_6)
        self.label_35.setMinimumSize(QtCore.QSize(150, 0))
        self.label_35.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_38.addWidget(self.label_35)
        self.bt_username = QtWidgets.QLineEdit(self.widget_6)
        self.bt_username.setObjectName("bt_username")
        self.horizontalLayout_38.addWidget(self.bt_username)
        self.verticalLayout_19.addWidget(self.widget_6)
        self.widget_11 = QtWidgets.QWidget(self.widget_5)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_37 = QtWidgets.QLabel(self.widget_11)
        self.label_37.setMinimumSize(QtCore.QSize(150, 0))
        self.label_37.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_19.addWidget(self.label_37)
        self.bt_password = QtWidgets.QLineEdit(self.widget_11)
        self.bt_password.setObjectName("bt_password")
        self.horizontalLayout_19.addWidget(self.bt_password)
        self.verticalLayout_19.addWidget(self.widget_11)
        self.widget_13 = QtWidgets.QWidget(self.widget_5)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.wg_login = QtWidgets.QWidget(self.widget_13)
        self.wg_login.setObjectName("wg_login")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.wg_login)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.bt_login = QtWidgets.QPushButton(self.wg_login)
        self.bt_login.setObjectName("bt_login")
        self.horizontalLayout_25.addWidget(self.bt_login)
        self.horizontalLayout_42.addWidget(self.wg_login)
        self.wg_logout = QtWidgets.QWidget(self.widget_13)
        self.wg_logout.setObjectName("wg_logout")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.wg_logout)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.bt_logout = QtWidgets.QPushButton(self.wg_logout)
        self.bt_logout.setObjectName("bt_logout")
        self.horizontalLayout_24.addWidget(self.bt_logout)
        self.horizontalLayout_42.addWidget(self.wg_logout)
        self.verticalLayout_19.addWidget(self.widget_13)
        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_18.addWidget(self.wget_login)
        self.stackedWidget.addWidget(self.page_login)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("background:rgb(91,90,90);")
        self.page_1.setObjectName("page_1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.page_1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.page_1)
        self.page_face_register = QtWidgets.QWidget()
        self.page_face_register.setObjectName("page_face_register")
        self.horizontalLayout_117 = QtWidgets.QHBoxLayout(self.page_face_register)
        self.horizontalLayout_117.setObjectName("horizontalLayout_117")
        self.wg_page_main = QtWidgets.QWidget(self.page_face_register)
        self.wg_page_main.setStyleSheet("/* Main Window */\n"
"QMainWindow {\n"
"    background-color: #2E3440;\n"
"    color: #ECEFF4;\n"
"    font-family: \'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #ECEFF4;\n"
"    font-size: 12pt;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Table View */\n"
"QTableView {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    gridline-color: #4C566A;\n"
"    border: 1px solid #4C566A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #4C566A;\n"
"    color: #ECEFF4;\n"
"    padding: 5px;\n"
"    border: 1px solid #4C566A;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #4C566A;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #5E81AC;\n"
"    color: #ECEFF4;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: #5E81AC;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #4C566A;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #81A1C1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C566A;\n"
"}\n"
"\n"
"/* Line Edit */\n"
"QLineEdit {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #4C566A;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Combo Box */\n"
"QComboBox {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #4C566A;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #4C566A;\n"
"    selection-background-color: #5E81AC;\n"
"}\n"
"\n"
"/* Group Box */\n"
"QGroupBox {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #4C566A;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"}\n"
"")
        self.wg_page_main.setObjectName("wg_page_main")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.wg_page_main)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_register = QtWidgets.QFrame(self.wg_page_main)
        self.frame_register.setMinimumSize(QtCore.QSize(900, 0))
        self.frame_register.setMaximumSize(QtCore.QSize(900, 16777215))
        self.frame_register.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_register.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_register.setObjectName("frame_register")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_register)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_register)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_image_1 = QtWidgets.QFrame(self.frame_4)
        self.frame_image_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_1.setObjectName("frame_image_1")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_image_1)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.lb_image_1 = QtWidgets.QLabel(self.frame_image_1)
        self.lb_image_1.setObjectName("lb_image_1")
        self.horizontalLayout_28.addWidget(self.lb_image_1)
        self.horizontalLayout_15.addWidget(self.frame_image_1)
        self.frame_image_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_image_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_2.setObjectName("frame_image_2")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_image_2)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.lb_image_2 = QtWidgets.QLabel(self.frame_image_2)
        self.lb_image_2.setObjectName("lb_image_2")
        self.horizontalLayout_27.addWidget(self.lb_image_2)
        self.horizontalLayout_15.addWidget(self.frame_image_2)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_image_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_image_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_3.setObjectName("frame_image_3")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_image_3)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.lb_image_3 = QtWidgets.QLabel(self.frame_image_3)
        self.lb_image_3.setObjectName("lb_image_3")
        self.horizontalLayout_29.addWidget(self.lb_image_3)
        self.horizontalLayout_18.addWidget(self.frame_image_3)
        self.frame_image_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_image_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_4.setObjectName("frame_image_4")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_image_4)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lb_image_4 = QtWidgets.QLabel(self.frame_image_4)
        self.lb_image_4.setObjectName("lb_image_4")
        self.horizontalLayout_23.addWidget(self.lb_image_4)
        self.horizontalLayout_18.addWidget(self.frame_image_4)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_register)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_20.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.bt_name = QtWidgets.QLineEdit(self.frame_7)
        self.bt_name.setMinimumSize(QtCore.QSize(200, 0))
        self.bt_name.setObjectName("bt_name")
        self.horizontalLayout_20.addWidget(self.bt_name)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_21.addWidget(self.label_3)
        self.bt_face_id = QtWidgets.QLineEdit(self.frame_9)
        self.bt_face_id.setMinimumSize(QtCore.QSize(200, 0))
        self.bt_face_id.setObjectName("bt_face_id")
        self.horizontalLayout_21.addWidget(self.bt_face_id)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.verticalLayout_5.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_10 = QtWidgets.QFrame(self.frame_register)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton = QtWidgets.QPushButton(self.frame_10)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_22.addWidget(self.pushButton)
        self.bn_open_images = QtWidgets.QPushButton(self.frame_10)
        self.bn_open_images.setMaximumSize(QtCore.QSize(150, 16777215))
        self.bn_open_images.setObjectName("bn_open_images")
        self.horizontalLayout_22.addWidget(self.bn_open_images)
        self.bn_register = QtWidgets.QPushButton(self.frame_10)
        self.bn_register.setMaximumSize(QtCore.QSize(150, 16777215))
        self.bn_register.setObjectName("bn_register")
        self.horizontalLayout_22.addWidget(self.bn_register)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.horizontalLayout_7.addWidget(self.frame_register)
        self.frame_face_data = QtWidgets.QFrame(self.wg_page_main)
        self.frame_face_data.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_face_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_face_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_face_data.setObjectName("frame_face_data")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_face_data)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_6 = QtWidgets.QFrame(self.frame_face_data)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_image_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_image_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image_5.setObjectName("frame_image_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_image_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lb_image_5 = QtWidgets.QLabel(self.frame_image_5)
        self.lb_image_5.setMinimumSize(QtCore.QSize(0, 300))
        self.lb_image_5.setObjectName("lb_image_5")
        self.verticalLayout_9.addWidget(self.lb_image_5)
        self.horizontalLayout_26.addWidget(self.frame_image_5)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.frame_11 = QtWidgets.QFrame(self.frame_face_data)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tableView = QtWidgets.QTableView(self.frame_11)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_10.addWidget(self.tableView)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_10.addWidget(self.pushButton_4)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.horizontalLayout_7.addWidget(self.frame_face_data)
        self.horizontalLayout_117.addWidget(self.wg_page_main)
        self.stackedWidget.addWidget(self.page_face_register)
        self.horizontalLayout_14.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_low = QtWidgets.QFrame(self.frame_bottom_east)
        self.frame_low.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_low.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_low.setStyleSheet("")
        self.frame_low.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_low.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_low.setObjectName("frame_low")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_tab = QtWidgets.QFrame(self.frame_low)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_tab.setFont(font)
        self.frame_tab.setStyleSheet("background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_tab.setObjectName("frame_tab")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lab_tab = QtWidgets.QLabel(self.frame_tab)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.lab_tab.setFont(font)
        self.lab_tab.setStyleSheet("color:rgb(255,255,255);")
        self.lab_tab.setObjectName("lab_tab")
        self.horizontalLayout_12.addWidget(self.lab_tab)
        self.horizontalLayout_11.addWidget(self.frame_tab)
        self.frame_drag = QtWidgets.QFrame(self.frame_low)
        self.frame_drag.setMinimumSize(QtCore.QSize(20, 20))
        self.frame_drag.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_drag.setStyleSheet("background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_drag.setObjectName("frame_drag")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_11.addWidget(self.frame_drag)
        self.verticalLayout_2.addWidget(self.frame_low)
        self.horizontalLayout_2.addWidget(self.frame_bottom_east)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_appname.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lab_user.setText(_translate("MainWindow", "<html><head/><body><p>IMS</p></body></html>"))
        self.bn_login.setToolTip(_translate("MainWindow", "Home"))
        self.bn_login.setText(_translate("MainWindow", "Đăng nhập"))
        self.bn_page_1.setToolTip(_translate("MainWindow", "Bug"))
        self.bn_page_1.setText(_translate("MainWindow", "Điểm danh"))
        self.bn_face_register.setToolTip(_translate("MainWindow", "Cloud"))
        self.bn_face_register.setText(_translate("MainWindow", "Đăng kí khuôn mặt"))
        self.label.setText(_translate("MainWindow", "ĐĂNG NHẬP "))
        self.label_39.setText(_translate("MainWindow", "Địa chỉ IP"))
        self.label_35.setText(_translate("MainWindow", "Tên đăng nhập"))
        self.label_37.setText(_translate("MainWindow", "Mật khẩu"))
        self.bt_login.setText(_translate("MainWindow", "Đăng nhập"))
        self.bt_logout.setText(_translate("MainWindow", "Đăng xuất"))
        self.label_6.setText(_translate("MainWindow", "page 1"))
        self.lb_image_1.setText(_translate("MainWindow", "image_1"))
        self.lb_image_2.setText(_translate("MainWindow", "image_2"))
        self.lb_image_3.setText(_translate("MainWindow", "image_3"))
        self.lb_image_4.setText(_translate("MainWindow", "image_4"))
        self.label_2.setText(_translate("MainWindow", "Họ và tên"))
        self.label_3.setText(_translate("MainWindow", "Mã số"))
        self.pushButton.setText(_translate("MainWindow", "Đăng kí từ thư mục"))
        self.bn_open_images.setText(_translate("MainWindow", "Chọn ảnh"))
        self.bn_register.setText(_translate("MainWindow", "Đăng ký"))
        self.lb_image_5.setText(_translate("MainWindow", "image"))
        self.pushButton_4.setText(_translate("MainWindow", "Làm mới"))
        self.lab_tab.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.frame_drag.setToolTip(_translate("MainWindow", "Drag"))
