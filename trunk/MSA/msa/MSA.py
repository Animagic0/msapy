#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Jorge Rodr�guez Ara�jo <grrodri@gmail.com>"
__copyright__ = "Copyright (c) 2009 Jorge Rodr�guez Ara�jo"
__license__ = "GPL"
__version__ = "0.3.7"
__date__ = "17-sep-2009"

import sys
import webbrowser

import gui

import msa2d
import draw2d

if __name__ == "__main__":
    if len(sys.argv) == 1:
        gui.run()
    else:
        filename = sys.argv[1]
        
        print "Leyendo los datos de definición de la estructura..."
        (joints, members) = draw2d.load(filename)
        print "Resolviendo la estructura por el método de la rigidez..."
        msa2d.msa(joints, members)
        print "Guardando y mostrando los resultados..."
        draw2d.report(joints, members)
        webbrowser.open('output/report.html')
