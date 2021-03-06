#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the GUI of the plots viewer.
"""
import logging
import matplotlib

from PyQt5.QtWidgets import QTabWidget
from gui.plots_qt import Ui_TabWidget_Plots

matplotlib.use("Qt5Agg")
# matplotlib.use MUST be set before backends import: warning E402
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

log = logging.getLogger('root')


class PlotsGUI(QTabWidget):

    """
    classdocs
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        super(PlotsGUI, self).__init__(parent)
        self.ui = Ui_TabWidget_Plots()
        self.ui.setupUi(self)

    def setup(self, analysis):
        self.ana = analysis
        self.__connect_events()
        self.__setup_plots()

    def __setup_plots(self):
        # Time spectrum
        self.mpl_time = MatplotlibWidget(
            title='Time', xlabel='n/a', ylabel='n/a', dpi=70)
        self.mpl_time.setObjectName("matplotlibwidget_Time")
        self.ui.verticalLayout_1.addWidget(self.mpl_time)
        navigation = NavigationToolbar(self.mpl_time, self)
        self.ui.verticalLayout_1.addWidget(navigation)
        # Mass spectrum
        self.mpl_mass = MatplotlibWidget(
            title='Mass', xlabel='n/a', ylabel='n/a', dpi=70)
        self.mpl_mass.setObjectName("matplotlibwidget_Mass")
        self.ui.verticalLayout_2.addWidget(self.mpl_mass)
        navigation = NavigationToolbar(self.mpl_mass, self)
        self.ui.verticalLayout_2.addWidget(navigation)
        # Peaks
        self.mpl_peaks = MatplotlibWidget(
            title='Peaks', xlabel='n/a', ylabel='n/a', dpi=70)
        self.mpl_peaks.setObjectName("matplotlibwidget_Peaks")
        self.ui.verticalLayout_3.addWidget(self.mpl_peaks)
        navigation = NavigationToolbar(self.mpl_peaks, self)
        self.ui.verticalLayout_3.addWidget(navigation)
        # Calib
        self.mpl_calib = MatplotlibWidget(
            title='Calibration', xlabel='n/a', ylabel='n/a', dpi=70)
        self.mpl_calib.setObjectName("matplotlibwidget_Calib")
        self.ui.verticalLayout_4.addWidget(self.mpl_calib)
        navigation = NavigationToolbar(self.mpl_calib, self)
        self.ui.verticalLayout_4.addWidget(navigation)
        # default tab = signal
        self.setCurrentIndex(0)

    def __connect_events(self):
        self.ana.plotTimeRaisedSignal.connect(self.update_time)
        self.ana.plotMassRaisedSignal.connect(self.update_mass)
        self.ana.plotPeaksRaisedSignal.connect(self.update_peaks)
        self.ana.plotCalibRaisedSignal.connect(self.update_calib)
        self.ana.plotClearRaisedSignal.connect(self.clear_plots)

    def update_time(self, shortname, x, y):
        log.debug("event from %s", self.sender())
        title = shortname + " - time spectrum"
        self.mpl_time.plot_data(x, y, title, "Time (ns)", "Intensity (a.u.)")

    def update_mass(self, shortname, mass, y, hold):
        log.debug("event from %s", self.sender())
        title = shortname + " - mass spectrum"
        x = mass
        self.mpl_mass.plot_mass(x, y, title, "m/z", "Intensity (a.u.)", hold)

    def update_peaks(self, shortname, mass, y, xind, yind, mph, mpd, x1, x2):
        log.debug("event from %s", self.sender())
        title = shortname + " - mass spectrum - " + \
            "(mph=" + str(mph) + ", mpd=" + str(mpd) + ")"
        x = mass
        self.mpl_peaks.plot_peaks(
            x, y, xind, yind, title, "m/z", "Intensity (a.u.)", x1, x2)

    def update_calib(self, shortname, mass_list, time_list, calib_mass, time):
        log.debug("event from %s", self.sender())
        title = shortname + "Calibration curve"
        self.mpl_calib.plot_calib(mass_list, time_list, calib_mass, time, title, "m/z", "Time (ns)")

    def clear_plots(self, mass, peaks, calib):
        if mass:
            self.mpl_mass.hide()
        else:
            self.mpl_mass.show()
        if peaks:
            self.mpl_peaks.hide()
        else:
            self.mpl_peaks.show()
        if calib:
            self.mpl_calib.hide()
        else:
            self.mpl_calib.show()


class MatplotlibWidget(Canvas):

    def __init__(self, parent=None, title='Title', xlabel='x label', ylabel='y label', dpi=100):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.canvas = Canvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.hold(False)

        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

    def plot_data(self, x, y, title, xlabel, ylabel):
        self.ax.plot(x, y)
        self.ax.set_title(title, size=10)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.draw()

    def plot_mass(self, x, y, title, xlabel, ylabel, hold=False):
        self.ax.hold(hold)
        self.ax.plot(x, y)
        self.ax.set_title(title, size=10)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.draw()

    def plot_calib(self, mass_list, time_list, calib_mass, time, title, xlabel, ylabel, hold=False):
        self.ax.hold(hold)
        self.ax.plot(mass_list, time_list, 'o', calib_mass, time)
        self.ax.set_title(title, size=10)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.draw()

    def plot_peaks(self, x, y, xind, yind, title, xlabel, ylabel, x1=-1.0, x2=-1.0):
        min_x = x1
        max_x = x2
        # dummy plot to apply the hold=True command
        self.ax.hold(False)
        self.ax.plot(x, y)
        self.draw()
        # real plot
        self.ax.hold(True)
#         self.ax.plot(x, y)
        self.ax.plot(x, y, 'b')
        self.ax.plot(xind, yind, '+', mfc=None, mec='r', mew=2, ms=8)
        self.ax.set_title(title, size=10)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        [x1, x2, y1, y2] = self.ax.axis()
        if min_x < 0.0:
            min_x = x1
        if max_x < 0.0:
            max_x = x2
        self.ax.axis([min_x, max_x, y1, y2])
        # test annotations
        for i, j in zip(xind, yind):
            text = "{:.0f}".format(float(j)) + " (" + \
                "{:.3f}".format(float(i)) + ")"
#             self.ax.annotate("{:.3f}".format(float(j)), xy=(i, j), size=10)
            self.ax.annotate(text, xy=(i, j), xytext=(i, j), size=10)
        self.draw()

if __name__ == '__main__':
    pass
else:
    log.info("Importing... %s", __name__)
