# -*- coding: utf-8 -*-
"""***************************************************************************
	multitemporalAnalyzer
								A QGIS plugin
	Multitemporal Analyzer
								-------------------
		copyright            : (C) 2013 by Arturo Mendoza / University of Carabobo (Venezuela)
		email                : arturo.amb89@gmail.com
***************************************************************************"""

def name():
	return "Multitemporal Analyzer"

def description():
	return "Multitemporal Analyzer of the surface area variation of a land cover. (University of Carabobo, Venezuela)"

def version():
	return "Version 0.7"

def icon():
	return "icon/icon.png"

def qgisMinimumVersion():
	return "1.0"

def qgisMaximumVersion():
	return "2.99"

def author():
	return "Arturo Mendoza"

def email():
	return "arturo.amb89@gmail.com"

def category():
    return "Raster"

def classFactory(iface):
	from multitemporalanalyzer import multitemporalAnalyzer
	return multitemporalAnalyzer(iface)

def homepage():
    return "http://multitemporalanalyzer.webs.com/"

def tracker():
    return "https://github.com/mrturo/multitemporalAnalizer/issues"

def repository():
    return "https://github.com/mrturo/multitemporalAnalizer.git"
