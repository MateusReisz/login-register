# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableView, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 560)
        MainWindow.setStyleSheet(u"background-color: rgb(198, 198, 198);\n"
"background-color: rgb(28, 26, 63);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_home = QPushButton(self.frame)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setMinimumSize(QSize(0, 35))
        self.button_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_home.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 173, 237);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 48, 80);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_home)

        self.button_importxml = QPushButton(self.frame)
        self.button_importxml.setObjectName(u"button_importxml")
        self.button_importxml.setMinimumSize(QSize(0, 35))
        self.button_importxml.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_importxml.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 173, 237);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 48, 80);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_importxml)

        self.button_tables = QPushButton(self.frame)
        self.button_tables.setObjectName(u"button_tables")
        self.button_tables.setMinimumSize(QSize(0, 35))
        self.button_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_tables.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 173, 237);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 48, 80);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_tables)

        self.button_about = QPushButton(self.frame)
        self.button_about.setObjectName(u"button_about")
        self.button_about.setMinimumSize(QSize(0, 35))
        self.button_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_about.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 173, 237);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 48, 80);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_about)

        self.button_contact = QPushButton(self.frame)
        self.button_contact.setObjectName(u"button_contact")
        self.button_contact.setMinimumSize(QSize(0, 35))
        self.button_contact.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_contact.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 173, 237);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(50, 48, 80);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_contact)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.page_tables = QWidget()
        self.page_tables.setObjectName(u"page_tables")
        self.verticalLayout_10 = QVBoxLayout(self.page_tables)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tab_widget = QTabWidget(self.page_tables)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setStyleSheet(u"background-color: rgb(94, 81, 140);\n"
"background-color: rgb(50, 48, 80);")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_9 = QVBoxLayout(self.tables)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.table_storage = QTreeWidget(self.tables)
        self.table_storage.setObjectName(u"table_storage")
        self.table_storage.setStyleSheet(u"background-color: rgb(226, 226, 226);\n"
"")
        self.table_storage.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_storage.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_storage.setAutoScroll(True)

        self.verticalLayout_7.addWidget(self.table_storage)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.table_input = QTreeWidget(self.tables)
        self.table_input.setObjectName(u"table_input")
        self.table_input.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.table_input.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_4.addWidget(self.table_input)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_output = QPushButton(self.frame_2)
        self.button_output.setObjectName(u"button_output")
        self.button_output.setMinimumSize(QSize(100, 25))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setBold(True)
        font.setItalic(False)
        self.button_output.setFont(font)
        self.button_output.setAcceptDrops(False)
        self.button_output.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(35, 173, 237);\n"
"	background-color: rgb(28, 26, 63);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}")

        self.verticalLayout_3.addWidget(self.button_output)

        self.button_refund = QPushButton(self.frame_2)
        self.button_refund.setObjectName(u"button_refund")
        self.button_refund.setMinimumSize(QSize(100, 25))
        self.button_refund.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(35, 173, 237);\n"
"	background-color: rgb(28, 26, 63);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.button_refund)

        self.button_import = QPushButton(self.frame_2)
        self.button_import.setObjectName(u"button_import")
        self.button_import.setMinimumSize(QSize(100, 25))
        self.button_import.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(35, 173, 237);\n"
"	background-color: rgb(28, 26, 63);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.button_import)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.tab_widget.addTab(self.tables, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_16 = QVBoxLayout(self.tab_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_18 = QLabel(self.tab_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"\n"
"color: rgb(66, 55, 140);")

        self.verticalLayout_16.addWidget(self.label_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.button_open_xlsx = QPushButton(self.tab_4)
        self.button_open_xlsx.setObjectName(u"button_open_xlsx")
        self.button_open_xlsx.setMinimumSize(QSize(0, 30))
        self.button_open_xlsx.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_xlsx.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(35, 173, 237);\n"
"	background-color: rgb(28, 26, 63);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}")

        self.horizontalLayout_12.addWidget(self.button_open_xlsx)

        self.button_open_chart = QPushButton(self.tab_4)
        self.button_open_chart.setObjectName(u"button_open_chart")
        self.button_open_chart.setMinimumSize(QSize(0, 30))
        self.button_open_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_chart.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(35, 173, 237);\n"
"	background-color: rgb(28, 26, 63);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}")

        self.horizontalLayout_12.addWidget(self.button_open_chart)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.line_filter = QLineEdit(self.tab_4)
        self.line_filter.setObjectName(u"line_filter")
        self.line_filter.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid white;\n"
"border-radius: 1px;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.line_filter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.line_filter)

        self.table_general = QTableView(self.tab_4)
        self.table_general.setObjectName(u"table_general")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 48, 80, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.table_general.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(12)
        self.table_general.setFont(font1)
        self.table_general.setAutoFillBackground(False)
        self.table_general.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.table_general)

        self.tab_widget.addTab(self.tab_4, "")

        self.verticalLayout_10.addWidget(self.tab_widget)

        self.Pages.addWidget(self.page_tables)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_15 = QVBoxLayout(self.page_home)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_32 = QLabel(self.page_home)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_12.addWidget(self.label_32)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_21 = QLabel(self.page_home)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_16.addWidget(self.label_21)

        self.button_page_register = QPushButton(self.page_home)
        self.button_page_register.setObjectName(u"button_page_register")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_page_register.sizePolicy().hasHeightForWidth())
        self.button_page_register.setSizePolicy(sizePolicy1)
        self.button_page_register.setMinimumSize(QSize(0, 50))
        self.button_page_register.setMaximumSize(QSize(16777215, 16777215))
        self.button_page_register.setFont(font)
        self.button_page_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_page_register.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 255, 255);\n"
"	background-color: rgb(1, 3, 38);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.button_page_register)

        self.label_30 = QLabel(self.page_home)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_16.addWidget(self.label_30)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)


        self.verticalLayout_15.addLayout(self.verticalLayout_12)

        self.Pages.addWidget(self.page_home)
        self.page_importxml = QWidget()
        self.page_importxml.setObjectName(u"page_importxml")
        self.verticalLayout_17 = QVBoxLayout(self.page_importxml)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.page_importxml)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 150, -1, -1)
        self.line_import = QLineEdit(self.page_importxml)
        self.line_import.setObjectName(u"line_import")
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        self.line_import.setFont(font3)
        self.line_import.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid white;\n"
"border-radius: 1px;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.line_import.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.line_import)

        self.button_open_import = QPushButton(self.page_importxml)
        self.button_open_import.setObjectName(u"button_open_import")
        self.button_open_import.setMinimumSize(QSize(120, 30))
        self.button_open_import.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(35, 173, 237);\n"
"	\n"
"	background-color: rgb(50, 48, 80);\n"
"	border-top-right-radius: 15px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.button_open_import)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 100, -1, -1)
        self.label_5 = QLabel(self.page_importxml)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.button_import_xml = QPushButton(self.page_importxml)
        self.button_import_xml.setObjectName(u"button_import_xml")
        self.button_import_xml.setMinimumSize(QSize(0, 50))
        self.button_import_xml.setMaximumSize(QSize(16777215, 16777215))
        self.button_import_xml.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 255, 255);\n"
"	background-color: rgb(1, 3, 38);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.button_import_xml)

        self.label_15 = QLabel(self.page_importxml)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.progressBar = QProgressBar(self.page_importxml)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{	\n"
"background-color: rgba(0, 0, 0,0.1);\n"
"color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 75, 149, 255), stop:1 rgba(72, 130, 157, 255));\n"
"border-radius:10px;\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_6.addWidget(self.progressBar)


        self.verticalLayout_17.addLayout(self.verticalLayout_6)

        self.Pages.addWidget(self.page_importxml)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.verticalLayout_5 = QVBoxLayout(self.page_register)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_14 = QLabel(self.page_register)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_6 = QLabel(self.page_register)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(8)
        self.label_6.setFont(font4)
        self.label_6.setAcceptDrops(False)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setMargin(0)
        self.label_6.setIndent(-1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, 50, -1)
        self.label_7 = QLabel(self.page_register)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.line_name = QLineEdit(self.page_register)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid white;\n"
"border-radius: 1px;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")

        self.horizontalLayout_7.addWidget(self.line_name)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, 50, -1)
        self.label_8 = QLabel(self.page_register)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 11px;")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.line_user = QLineEdit(self.page_register)
        self.line_user.setObjectName(u"line_user")
        self.line_user.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid white;\n"
"border-radius: 1px;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")

        self.horizontalLayout_8.addWidget(self.line_user)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, 50, -1)
        self.label_9 = QLabel(self.page_register)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.line_password = QLineEdit(self.page_register)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid white;\n"
"border-radius: 1px;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.line_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.line_password)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, -1, 50, -1)
        self.label_10 = QLabel(self.page_register)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.line_password_2 = QLineEdit(self.page_register)
        self.line_password_2.setObjectName(u"line_password_2")
        self.line_password_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid white;\n"
"border-radius: 1px;\n"
"font-family: Trebuchet MS;\n"
"font-size: 21px;")
        self.line_password_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_10.addWidget(self.line_password_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, -1, 50, -1)
        self.label_11 = QLabel(self.page_register)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: rgb(17, 180, 217);\n"
"")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.combo_box_profile = QComboBox(self.page_register)
        self.combo_box_profile.addItem("")
        self.combo_box_profile.addItem("")
        self.combo_box_profile.setObjectName(u"combo_box_profile")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        self.combo_box_profile.setFont(font6)
        self.combo_box_profile.setStyleSheet(u"color: rgb(0, 255, 255);")

        self.horizontalLayout_5.addWidget(self.combo_box_profile)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.page_register)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.button_signup = QPushButton(self.page_register)
        self.button_signup.setObjectName(u"button_signup")
        self.button_signup.setMinimumSize(QSize(0, 50))
        self.button_signup.setFont(font)
        self.button_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_signup.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 255, 255);\n"
"	background-color: rgb(1, 3, 38);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.button_signup)

        self.label_13 = QLabel(self.page_register)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.Pages.addWidget(self.page_register)
        self.page_contact = QWidget()
        self.page_contact.setObjectName(u"page_contact")
        self.verticalLayout_14 = QVBoxLayout(self.page_contact)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_19 = QLabel(self.page_contact)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        self.label_19.setFont(font7)

        self.verticalLayout_13.addWidget(self.label_19)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.page_contact)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_18.addWidget(self.label_25)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_24 = QLabel(self.page_contact)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        self.label_24.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label_24)

        self.label_20 = QLabel(self.page_contact)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        font8 = QFont()
        font8.setUnderline(False)
        font8.setKerning(True)
        self.label_20.setFont(font8)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_20)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_2)

        self.label_26 = QLabel(self.page_contact)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_18.addWidget(self.label_26)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.page_contact)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_19.addWidget(self.label_29)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_28 = QLabel(self.page_contact)
        self.label_28.setObjectName(u"label_28")
        sizePolicy3.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy3)
        self.label_28.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.label_28)

        self.label_27 = QLabel(self.page_contact)
        self.label_27.setObjectName(u"label_27")
        sizePolicy4.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy4)
        self.label_27.setScaledContents(True)
        self.label_27.setOpenExternalLinks(True)

        self.horizontalLayout_13.addWidget(self.label_27)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_13)

        self.label_33 = QLabel(self.page_contact)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_19.addWidget(self.label_33)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_34 = QLabel(self.page_contact)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_20.addWidget(self.label_34)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_35 = QLabel(self.page_contact)
        self.label_35.setObjectName(u"label_35")
        sizePolicy3.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy3)

        self.horizontalLayout_14.addWidget(self.label_35)

        self.label_22 = QLabel(self.page_contact)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setScaledContents(True)
        self.label_22.setOpenExternalLinks(True)

        self.horizontalLayout_14.addWidget(self.label_22)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_14)

        self.label_36 = QLabel(self.page_contact)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_20.addWidget(self.label_36)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_37 = QLabel(self.page_contact)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_26.addWidget(self.label_37)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_38 = QLabel(self.page_contact)
        self.label_38.setObjectName(u"label_38")
        sizePolicy3.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.label_38)

        self.label_23 = QLabel(self.page_contact)
        self.label_23.setObjectName(u"label_23")
        sizePolicy4.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy4)
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setScaledContents(True)
        self.label_23.setOpenExternalLinks(True)

        self.horizontalLayout_15.addWidget(self.label_23)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_15)

        self.label_39 = QLabel(self.page_contact)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_26.addWidget(self.label_39)


        self.verticalLayout.addLayout(self.horizontalLayout_26)


        self.verticalLayout_13.addLayout(self.verticalLayout)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.Pages.addWidget(self.page_contact)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_11 = QVBoxLayout(self.page_about)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_16 = QLabel(self.page_about)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 20))
        self.label_16.setMaximumSize(QSize(16777215, 50))
        self.label_16.setFont(font7)

        self.verticalLayout_11.addWidget(self.label_16)

        self.label_17 = QLabel(self.page_about)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_17)

        self.Pages.addWidget(self.page_about)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.button_importxml.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.button_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.button_about.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.button_contact.setText(QCoreApplication.translate("MainWindow", u"CONTACT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">STORAGE</span></p></body></html>", None))
        ___qtreewidgetitem = self.table_storage.headerItem()
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Item Note", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Value Nfe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"User", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Key", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Date Issue", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serial", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#fefefe;\">INPUT</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.table_input.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"User", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Date Output", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Date Import", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Serial", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.button_output.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.button_refund.setText(QCoreApplication.translate("MainWindow", u"Refund", None))
        self.button_import.setText("")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#181434;\">General</span></p></body></html>", None))
        self.button_open_xlsx.setText(QCoreApplication.translate("MainWindow", u"Generate Excel", None))
        self.button_open_chart.setText(QCoreApplication.translate("MainWindow", u"Generate chart", None))
        self.line_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"General", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"files/logo.png\"/></p></body></html>", None))
        self.label_21.setText("")
        self.button_page_register.setText(QCoreApplication.translate("MainWindow", u"Register User", None))
        self.label_30.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#55ffff;\">IMPORT XML</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.line_import.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.line_import.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select the folder  --->", None))
        self.button_open_import.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.label_5.setText("")
        self.button_import_xml.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.label_15.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"files/register.png\"/></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#00ffff;\">Sign Up</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#c7c1d7;\">Please fill out the form below to create your account.</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00ffff;\">Name:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00ffff;\">User:</span></p></body></html>", None))
        self.line_user.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00ffff;\">Password:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00ffff;\">Confirm Password:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00ffff;\">Profile</span></p></body></html>", None))
        self.combo_box_profile.setItemText(0, QCoreApplication.translate("MainWindow", u"User", None))
        self.combo_box_profile.setItemText(1, QCoreApplication.translate("MainWindow", u"Admin", None))

        self.label_12.setText("")
        self.button_signup.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.label_13.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#55ffff;\">CONTACT</span></p></body></html>", None))
        self.label_25.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"files/dev.png\"/></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Developer: Mateus Reis</span></p></body></html>", None))
        self.label_26.setText("")
        self.label_29.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"files/o-email.png\"/></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://www.google.com/intl/pt-BR/gmail/about/\"><span style=\" font-size:16pt; text-decoration: none; color:#ffffff;\">mateusreisengc@outlook.com</span></a></p></body></html>", None))
        self.label_33.setText("")
        self.label_34.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"files/github.png\"/></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://github.com/MateusReisz\"><span style=\" font-size:16pt; text-decoration: none; color:#ffffff;\">github.com/MateusReisz</span></a></p></body></html>", None))
        self.label_36.setText("")
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"files/linkedin.png\"/></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://www.linkedin.com/in/mateus-reis-devfull/\"><span style=\" font-size:16pt; text-decoration: none; color:#ffffff;\">linkedin/mateus-reis-devfull</span></a></p></body></html>", None))
        self.label_39.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#55ffff;\">ABOUT</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">This system imports XML files and controls inventory according to the input of notes and outputs indicated by the user.</span></p></body></html>", None))
    # retranslateUi

