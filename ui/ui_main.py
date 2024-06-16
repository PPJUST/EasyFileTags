# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainRURrkn.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(409, 273)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_add_tag = QToolButton(self.groupBox)
        self.toolButton_add_tag.setObjectName(u"toolButton_add_tag")

        self.horizontalLayout.addWidget(self.toolButton_add_tag)

        self.toolButton_delete_tag = QToolButton(self.groupBox)
        self.toolButton_delete_tag.setObjectName(u"toolButton_delete_tag")

        self.horizontalLayout.addWidget(self.toolButton_delete_tag)

        self.toolButton_restore_tag = QToolButton(self.groupBox)
        self.toolButton_restore_tag.setObjectName(u"toolButton_restore_tag")

        self.horizontalLayout.addWidget(self.toolButton_restore_tag)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.listWidget_tag = QListWidget(self.groupBox)
        self.listWidget_tag.setObjectName(u"listWidget_tag")

        self.verticalLayout_2.addWidget(self.listWidget_tag)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.toolButton_restore_tag_file = QToolButton(self.groupBox_2)
        self.toolButton_restore_tag_file.setObjectName(u"toolButton_restore_tag_file")

        self.horizontalLayout_4.addWidget(self.toolButton_restore_tag_file)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.listWidget_tag_file = QListWidget(self.groupBox_2)
        self.listWidget_tag_file.setObjectName(u"listWidget_tag_file")

        self.verticalLayout_6.addWidget(self.listWidget_tag_file)

        self.splitter.addWidget(self.groupBox_2)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_filename_original = QLabel(self.layoutWidget)
        self.label_filename_original.setObjectName(u"label_filename_original")
        self.label_filename_original.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_filename_original)

        self.label_down = QLabel(self.layoutWidget)
        self.label_down.setObjectName(u"label_down")

        self.verticalLayout_3.addWidget(self.label_down)

        self.label_filename_preview = QLabel(self.layoutWidget)
        self.label_filename_preview.setObjectName(u"label_filename_preview")
        self.label_filename_preview.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_filename_preview)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.comboBox_tags = QComboBox(self.layoutWidget)
        self.comboBox_tags.setObjectName(u"comboBox_tags")

        self.horizontalLayout_2.addWidget(self.comboBox_tags)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_clear = QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_3.addWidget(self.pushButton_clear)

        self.pushButton_confirm = QPushButton(self.layoutWidget)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")

        self.horizontalLayout_3.addWidget(self.pushButton_confirm)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4.setStretch(0, 1)
        self.splitter.addWidget(self.layoutWidget)

        self.horizontalLayout_5.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7b80\u6613Tag", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49Tag", None))
        self.toolButton_add_tag.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_delete_tag.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.toolButton_restore_tag.setText(QCoreApplication.translate("MainWindow", u"\u8fd8\u539f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bc6\u522bTag", None))
        self.toolButton_restore_tag_file.setText(QCoreApplication.translate("MainWindow", u"\u8fd8\u539f", None))
        self.label_filename_original.setText(QCoreApplication.translate("MainWindow", u"\u62d6\u5165\u5230\u6b64\u5904", None))
        self.label_down.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.label_filename_preview.setText(QCoreApplication.translate("MainWindow", u"\u9884\u671f\u6587\u4ef6\u540d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6807\u8bc6\u7b26:", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664Tag", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4fee\u6539", None))
    # retranslateUi

