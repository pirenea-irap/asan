# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PIRENEA\PYTHON\asan\src\gui\analysis_qt.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockWidget_Analysis(object):
    def setupUi(self, DockWidget_Analysis):
        DockWidget_Analysis.setObjectName("DockWidget_Analysis")
        DockWidget_Analysis.resize(1050, 200)
        DockWidget_Analysis.setMinimumSize(QtCore.QSize(1050, 200))
        DockWidget_Analysis.setMaximumSize(QtCore.QSize(1050, 200))
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.groupBox_Mass = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox_Mass.setGeometry(QtCore.QRect(340, 10, 340, 150))
        self.groupBox_Mass.setObjectName("groupBox_Mass")
        self.label_PlotStartMass = QtWidgets.QLabel(self.groupBox_Mass)
        self.label_PlotStartMass.setGeometry(QtCore.QRect(10, 120, 95, 16))
        self.label_PlotStartMass.setObjectName("label_PlotStartMass")
        self.checkBox_Hold = QtWidgets.QCheckBox(self.groupBox_Mass)
        self.checkBox_Hold.setGeometry(QtCore.QRect(260, 120, 70, 17))
        self.checkBox_Hold.setObjectName("checkBox_Hold")
        self.doubleSpinBox_PlotMassX1 = QtWidgets.QDoubleSpinBox(self.groupBox_Mass)
        self.doubleSpinBox_PlotMassX1.setGeometry(QtCore.QRect(110, 120, 60, 20))
        self.doubleSpinBox_PlotMassX1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PlotMassX1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PlotMassX1.setDecimals(1)
        self.doubleSpinBox_PlotMassX1.setMaximum(1000.0)
        self.doubleSpinBox_PlotMassX1.setProperty("value", 10.0)
        self.doubleSpinBox_PlotMassX1.setObjectName("doubleSpinBox_PlotMassX1")
        self.doubleSpinBox_PlotMassX2 = QtWidgets.QDoubleSpinBox(self.groupBox_Mass)
        self.doubleSpinBox_PlotMassX2.setGeometry(QtCore.QRect(180, 120, 60, 20))
        self.doubleSpinBox_PlotMassX2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PlotMassX2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PlotMassX2.setDecimals(1)
        self.doubleSpinBox_PlotMassX2.setMaximum(3000.0)
        self.doubleSpinBox_PlotMassX2.setProperty("value", 600.0)
        self.doubleSpinBox_PlotMassX2.setObjectName("doubleSpinBox_PlotMassX2")
        self.groupBox_Peak = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox_Peak.setGeometry(QtCore.QRect(700, 40, 340, 81))
        self.groupBox_Peak.setObjectName("groupBox_Peak")
        self.label_PeakHeight = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_PeakHeight.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_PeakHeight.setObjectName("label_PeakHeight")
        self.label_PeakDistance = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_PeakDistance.setGeometry(QtCore.QRect(10, 55, 81, 16))
        self.label_PeakDistance.setObjectName("label_PeakDistance")
        self.label_StartMass = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_StartMass.setGeometry(QtCore.QRect(190, 30, 70, 16))
        self.label_StartMass.setObjectName("label_StartMass")
        self.label_EndMass = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_EndMass.setGeometry(QtCore.QRect(190, 55, 70, 16))
        self.label_EndMass.setObjectName("label_EndMass")
        self.doubleSpinBox_PeakHeight = QtWidgets.QDoubleSpinBox(self.groupBox_Peak)
        self.doubleSpinBox_PeakHeight.setGeometry(QtCore.QRect(100, 30, 60, 20))
        self.doubleSpinBox_PeakHeight.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PeakHeight.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PeakHeight.setDecimals(3)
        self.doubleSpinBox_PeakHeight.setMaximum(10000.0)
        self.doubleSpinBox_PeakHeight.setObjectName("doubleSpinBox_PeakHeight")
        self.spinBox_PeakDistance = QtWidgets.QSpinBox(self.groupBox_Peak)
        self.spinBox_PeakDistance.setGeometry(QtCore.QRect(100, 55, 30, 20))
        self.spinBox_PeakDistance.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_PeakDistance.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_PeakDistance.setMaximum(10000)
        self.spinBox_PeakDistance.setProperty("value", 0)
        self.spinBox_PeakDistance.setObjectName("spinBox_PeakDistance")
        self.doubleSpinBox_StartMass = QtWidgets.QDoubleSpinBox(self.groupBox_Peak)
        self.doubleSpinBox_StartMass.setGeometry(QtCore.QRect(260, 30, 60, 20))
        self.doubleSpinBox_StartMass.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_StartMass.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_StartMass.setDecimals(1)
        self.doubleSpinBox_StartMass.setMaximum(1000.0)
        self.doubleSpinBox_StartMass.setObjectName("doubleSpinBox_StartMass")
        self.doubleSpinBox_EndMass = QtWidgets.QDoubleSpinBox(self.groupBox_Peak)
        self.doubleSpinBox_EndMass.setGeometry(QtCore.QRect(260, 55, 60, 20))
        self.doubleSpinBox_EndMass.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_EndMass.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_EndMass.setDecimals(1)
        self.doubleSpinBox_EndMass.setMaximum(1000.0)
        self.doubleSpinBox_EndMass.setObjectName("doubleSpinBox_EndMass")
        self.spinBox_PeakDistanceFound = QtWidgets.QSpinBox(self.groupBox_Peak)
        self.spinBox_PeakDistanceFound.setEnabled(False)
        self.spinBox_PeakDistanceFound.setGeometry(QtCore.QRect(135, 55, 30, 20))
        self.spinBox_PeakDistanceFound.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_PeakDistanceFound.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_PeakDistanceFound.setMaximum(10000)
        self.spinBox_PeakDistanceFound.setProperty("value", 0)
        self.spinBox_PeakDistanceFound.setObjectName("spinBox_PeakDistanceFound")
        self.pushButton_UpdatePlots = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_UpdatePlots.setEnabled(False)
        self.pushButton_UpdatePlots.setGeometry(QtCore.QRect(920, 130, 110, 23))
        self.pushButton_UpdatePlots.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_UpdatePlots.setFont(font)
        self.pushButton_UpdatePlots.setObjectName("pushButton_UpdatePlots")
        self.lineEdit_File = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_File.setEnabled(False)
        self.lineEdit_File.setGeometry(QtCore.QRect(140, 10, 133, 20))
        self.lineEdit_File.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lineEdit_File.setFont(font)
        self.lineEdit_File.setText("")
        self.lineEdit_File.setReadOnly(False)
        self.lineEdit_File.setObjectName("lineEdit_File")
        self.label_Filename = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_Filename.setGeometry(QtCore.QRect(70, 10, 60, 16))
        self.label_Filename.setObjectName("label_Filename")
        DockWidget_Analysis.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_Analysis)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_Analysis)

    def retranslateUi(self, DockWidget_Analysis):
        _translate = QtCore.QCoreApplication.translate
        DockWidget_Analysis.setWindowTitle(_translate("DockWidget_Analysis", "Analysis"))
        self.groupBox_Mass.setTitle(_translate("DockWidget_Analysis", "Mass Calibration"))
        self.label_PlotStartMass.setText(_translate("DockWidget_Analysis", "Plot mass limits"))
        self.checkBox_Hold.setText(_translate("DockWidget_Analysis", "Hold"))
        self.groupBox_Peak.setTitle(_translate("DockWidget_Analysis", "Peak Detection"))
        self.label_PeakHeight.setText(_translate("DockWidget_Analysis", "Peak Height"))
        self.label_PeakDistance.setText(_translate("DockWidget_Analysis", "Peak Distance"))
        self.label_StartMass.setText(_translate("DockWidget_Analysis", "Start Mass"))
        self.label_EndMass.setText(_translate("DockWidget_Analysis", "End Mass"))
        self.pushButton_UpdatePlots.setText(_translate("DockWidget_Analysis", "Update Plots"))
        self.label_Filename.setText(_translate("DockWidget_Analysis", "FILENAME"))

