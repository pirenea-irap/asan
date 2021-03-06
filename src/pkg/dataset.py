#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the PIRENEA raw datasets.
"""
import struct

import logging
log = logging.getLogger('root')


class Dataset(object):

    """
    Manage AROMA files (ASCII).

    :Example:

    """

    def __init__(self, filename=""):
        """
        Constructor
        """
        self.filename = filename
        self.points = 0
        self.time = []
        self.mass = []
        self.spectrum = []
        self.headtext = ""
        self.isCalibAvailable = False
        self.isCalibDone = False
        self.datetime = ""
        self.coefs = []

        self.__read_file()

#         self.__find_limits()

    def __read_file(self):
        """
        Read an AROMA file in ASCII format.
        """
        try:
            with open(self.filename, mode='rt', encoding='utf_8') as filer:
                self.isCalibAvailable = False
                index = 0
                for line in filer:
                    #                     if line.strip():
                    if '|' not in line:
                        self.headtext += line
                        if '.mz' in line:
                            self.isCalibAvailable = True
                        if 'Date' in line:
                            self.datetime = line.split('Date & Time:')[1].strip()
                    else:
                        if self.isCalibAvailable:
                            self.time.append(
                                float(line.split('|')[0].strip()))
                            self.mass.append(
                                float(line.split('|')[1].strip()))
                            self.spectrum.append(
                                float(line.split('|')[2].strip()))
                        else:
                            self.time.append(
                                float(line.split('|')[0].strip()))
                            self.spectrum.append(
                                float(line.split('|')[1].strip()))
                        index += 1

            if not self.isCalibAvailable:
                self.headtext += "\nNO CALIBRATION FILE\n"
                log.info("No calibration file for mass")
            self.points = index
            log.debug("points %d", self.points)

        except (IOError) as error:
            log.error("Unable to open : %s", error)
        except (struct.error) as error:
            log.error("Not a valid binary file : %s", error)

    def write_calib(self, calib_name):
        """
        Write a calibrated spectrum in ASCII format, store it in a different place
        """
        try:
            log.debug("Written file %s...", calib_name)
            with open(calib_name, mode='w', encoding='utf_8') as file:
                file.write(self.headtext)
                for i in range(self.points):
                    file.write(str(self.time[i]) + " | " + str(self.mass[i]) + " | " +
                               str(self.spectrum[i]) + ' |' + "\n")

        except (IOError) as error:
            log.error("Unable to write into: %s", error)
        except (struct.error) as error:
            log.error("Not a valid data file : %s", error)

    def write_mmass(self, mmass_name):
        """
        Write a calibrated spectrum in ASCII format, compatible with mmass software
        """
        try:
            log.debug("Written file %s...", mmass_name)
            with open(mmass_name, mode='w', encoding='utf_8') as file:
                for i in range(self.points):
                    file.write(str(self.mass[i]) + " " + str(self.spectrum[i]) + "\n")
        except (IOError) as error:
            log.error("Unable to write into: %s", error)
        except (struct.error) as error:
            log.error("Not a valid data file : %s", error)

    def update_mass(self, calib_mass):
        self.mass = calib_mass
        self.isCalibDone = True

if __name__ == '__main__':

    """
    main method to avoid error messages in pylint.
    """
    filename = "G:\\HASSAN\\Aroma\\Spectra\\2016-01-28\\Cor_1.txt"
#     filename = "G:\\HASSAN\\Aroma\\Spectra\\2016-01-28\\HS_mix_1.txt"
    raw = Dataset(filename)
    mass = raw.mass

else:
    log.info("Importing... %s", __name__)
