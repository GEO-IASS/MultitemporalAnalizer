# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""***************************************************************************
	multitemporalAnalyzer
								A QGIS plugin
	Multitemporal Analyzer
								-------------------
		copyright            : (C) 2013 by Arturo Mendoza / University of Carabobo (Venezuela)
		email                : arturo.amb89@gmail.com
***************************************************************************"""
# Import the PyQt and QGIS libraries
from	PyQt4.QtWebKit	import *
from	PyQt4.QtCore	import *
from	PyQt4.QtGui		import *
from	PyQt4.Qt		import *
from	qgis.core		import *
# Initialize Qt resources from file resources.py
import	doc_rc
import	icon_rc
import	image_rc
import	screenshot_rc
# Import the code for the dialogs
from	ui_selectScenes	import Ui_selectScenes
from	ui_selectPoint	import Ui_selectPoint
from	ui_crossroad	import Ui_crossroad
from	ui_editscene	import Ui_editScene
from	ui_addscene		import Ui_addScene
from	ui_aboutUs		import Ui_aboutUs
from	ui_result		import Ui_result
from	ui_report		import Ui_report
from	ui_help1		import Ui_help1
from	ui_help2		import Ui_help2
from	ui_help3		import Ui_help3
from	ui_help4		import Ui_help4
from	ui_help5		import Ui_help5
from	ui_home			import Ui_home
from	ui_wait			import Ui_wait
# Import others modules
from	datetime		import timedelta, datetime, date, time
from	PIL				import Image, ImageDraw, ImageFont
from	osgeo			import gdal, gdalconst
import	os.path
import	ImageQt
import	random
import	math
import	sys
import	os

tempFolder		= ".multitemporalAnalyzer_temp"
lastScenesPath	= ".lastScenesList.txt"
separatePath	= "/"
sourceSave		= "."
if os.name=="nt":
	home = os.environ['HOME']
	separatePath	= "\\"
	sourceSave		= home + "\\Documents"
	tempFolder		= home + "\\Documents\\" + tempFolder
	lastScenesPath	= home + "\\Documents\\" + lastScenesPath

try:
    _fromUtf8 = str.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = str.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

# Get the neighboring pixels and similar to one shown
def getSimilarPixels(wait, tN, uniqueColor=True, img=None, point=None):
	result = None
	numPix = 0
	tN = float(tN)
	if img!=None and type(point)==tuple:
		result		= Image.new("RGBA", (img.size[0], img.size[1]), (0,0,0,0))
		pixResult	= result.load()
		pixImg		= img.load()
		if len(point)==2:
			if type(point[0])==int and type(point[1])==int:
				if ( point[0] in range(img.size[0]) ) and ( point[1] in range(img.size[1]) ):
					if uniqueColor:
						for x in xrange(img.size[0]):
							for y in xrange(img.size[1]):
								if pixImg[point[0], point[1]] == pixImg[x, y]:
									pixResult[x,y] = (0,0,0,255)
									numPix = numPix + 1
					elif pixResult[point[0], point[1]]==(0,0,0,0):
						t0 = 0.0
						if wait!=None:
							t0 = float(wait.ui.progressBar.value())
							t = tN - t0
						points = [ point ]
						while len(points)>0:
							p = points[0]
							del points[0]
							if pixImg[p[0], p[1]] == pixImg[point[0], point[1]]:
								neighbors = [ (p[0]-1, p[1]), (p[0]-1, p[1]+1), (p[0], p[1]+1), (p[0]+1, p[1]+1), (p[0]+1, p[1]), (p[0]+1, p[1]-1), (p[0], p[1]-1), (p[0]-1, p[1]-1) ]
								while len(neighbors)>0:
									if ( neighbors[0][0] in range(img.size[0]) ) and ( neighbors[0][1] in range(img.size[1]) ) and pixResult[neighbors[0][0], neighbors[0][1]]==(0,0,0,0):
										points.insert(0, neighbors[0])
									del neighbors[0]
								pixResult[p[0], p[1]] = (0,0,0,255)
								numPix = numPix + 1
								del neighbors
							if wait!=None:
								wait.ui.progressBar.setProperty("value", t0 + ((float(numPix)/float(len(points)+numPix))*tN)/2.0 )
							del p
						del t0, points
		del pixResult, pixImg
	if wait!=None:
		wait.ui.progressBar.setProperty("value", float(tN) )
	del tN
	return (numPix, result)

# Returns the area of a surface of suitably
def strArea(area):
	value = float(area)
	unit = ""
	if value>=1000:
		value = value/1000.0
		unit = "K"
	if value>=1000:
		value = value/1000.0
		unit = "M"
	if value>=1000:
		value = value/1000.0
		unit = "G"
	if value>=1000:
		value = value/1000.0
		unit = "T"
	if value>=1000:
		value = value/1000.0
		unit = "P"
	if value>=1000:
		value = value/1000.0
		unit = "E"
	if value>=1000:
		value = value/1000.0
		unit = "Z"
	if value>=1000:
		value = value/1000.0
		unit = "Y"
	return str(value) + " " + unit + "m"

# Class Scene
class scene():
	
	# Class Builder
	def __init__(self, name="", path="", date=None):
		ext = str("" + str(path).lower())
		while ext.find(".")>=0:
			ext = ext[ext.find(".")+1:]
		if ext in ["tif", "tiff"]:
			self.path		= os.path.abspath(str(path))
			self.name		= name
			self.date		= date
			self.tDelta		= 0.0
			self.distTime	= 0.0
			try:
				open(self.path,'r')
			except IOError:
				self.img	= None
				self.path	= None
				self.name	= None
				self.date	= None
			else:
				try:
					self.img = Image.open( self.path )
				except IOError:
					self.img	= None
					self.path	= None
					self.name	= None
					self.date	= None
				else:
					# Getting Image Data
					self.originalsample = gdal.Open(self.path, gdalconst.GA_ReadOnly)												# Get a sample
					self.proj, self.OriginalGTrans = self.originalsample.GetProjection(), self.originalsample.GetGeoTransform()		# Get geoData
					self.originalNColumns, self.originalNRows = self.originalsample.RasterXSize, self.originalsample.RasterYSize	# Get size
					
					if not (self.proj!="" and self.OriginalGTrans!=(0.0, 1.0, 0.0, 0.0, 0.0, 1.0)):
						self.img	= None
						self.path	= None
						self.name	= None
						self.date	= None
						del self.originalsample, self.proj, self.OriginalGTrans, self.originalNColumns, self.originalNRows
					else:
						if self.img.mode != "RGBA":
							self.img = self.img.convert("RGBA")
							
						# Set predetermined interest area
						self.nColumns, self.nRows = self.originalNColumns, self.originalNRows
						self.gTrans = ( self.OriginalGTrans[0], self.OriginalGTrans[1], self.OriginalGTrans[2], self.OriginalGTrans[3], self.OriginalGTrans[4], self.OriginalGTrans[5] )
						self._x0, self._y0, self._xV, self._yV = self.gTrans[0], self.gTrans[3], self.gTrans[1], self.gTrans[5]
						self._nx, self._ny = ( ( self.nColumns * self._xV ) + self._x0 ), ( ( self.nRows * self._yV ) + self._y0 )
						self.Column0, self.ColumnN = 0, self.originalNColumns
						self.Row0, self.RowN = 0, self.originalNRows
						self._xN, self._yN = self._nx, self._ny
						self._subSet = False
		else:
			self.img	= None
			self.path	= None
			self.name	= None
			self.date	= None
		del ext
	
	# Get a time delta of the scene
	def timeDelta(self):
		self.tDelta = float(self.date.day-1)
		for i in range(self.date.year):
			if i%4==0:
				self.tDelta = self.tDelta + 366.0
			else:
				self.tDelta = self.tDelta + 365.0
		for i in range(self.date.month):
			if i in [1, 3, 5, 7, 8, 10, 12]:
				self.tDelta = self.tDelta + 31.0
			elif i in [4, 6, 9, 11]:
				self.tDelta = self.tDelta + 30.0
			elif self.date.year%4==0:
				self.tDelta = self.tDelta + 29.0
			else:
				self.tDelta = self.tDelta + 28.0
		self.tDelta = self.tDelta + float(self.date.hour)/24.0 + float(self.date.minute)/(1.0/24.0)
		return self.tDelta
	
	# Get a sub set of the scene
	def subSet(self, x0 = None, y0 = None, xN = None, yN = None):
		if x0==None:
			x0 = self._x0
		if y0==None:
			y0 = self._y0
		if xN==None:
			xN = self._nx
		if yN==None:
			yN = self._yN
		if x0>xN:
			aux = x0
			x0 = xN
			xN = aux
			del aux
		if yN>y0:
			aux = y0
			y0 = yN
			yN = aux
			del aux
		if x0<self.gTrans[0]:
			x0 = self.gTrans[0]
		if y0>self.gTrans[3]:
			y0 = self.gTrans[3]
		if xN>self._nx:
			xN = self._nx
		if yN<self._ny:
			yN = self._ny
		if not( x0==self._x0 and y0==self._y0 and xN==self._xN and yN==self._yN ):
			self._x0, self._y0, self._xN, self._yN = x0, y0, xN, yN
			if x0 == self.gTrans[0] and y0 == self.gTrans[3] and xN == self._nx and yN == self._ny:
				self._subArea = False
				self.img = Image.open( self.path )
				self.nColumns, self.nRows = self.originalNColumns, self.originalNRows
				self.gTrans = ( self.OriginalGTrans[0], self.OriginalGTrans[1], self.OriginalGTrans[2], self.OriginalGTrans[3], self.OriginalGTrans[4], self.OriginalGTrans[5] )
				self.Column0, self.ColumnN = 0, self.originalNColumns
				self.Row0, self.RowN = 0, self.originalNRows
			else:
				self._subArea = True
				self.gTrans = ( self._x0, self.OriginalGTrans[1], self.OriginalGTrans[2], self._y0, self.OriginalGTrans[4], self.OriginalGTrans[5] )
				self.Column0 = int( ( float(self.gTrans[0]) - float(self.OriginalGTrans[0]) ) / self.gTrans[1] )
				self.ColumnN = int( ( float(self._xN) - float(self.OriginalGTrans[0]) ) / self.gTrans[1] )
				self.nColumns = self.ColumnN - self.Column0
				self.Row0 = int( ( float(self.gTrans[3]) - float(self.OriginalGTrans[3]) ) / self.gTrans[5] )
				self.RowN = int( ( float(self._yN) - float(self.OriginalGTrans[3]) ) / self.gTrans[5] )
				self.nRows = self.RowN - self.Row0
				self.img = Image.open( self.path )
				self.img = self.img.crop((self.Column0, self.Row0, self.ColumnN, self.RowN))
		else:
			self.img = Image.open( self.path )
			self.nColumns, self.nRows = self.originalNColumns, self.originalNRows
			self.gTrans = ( self.OriginalGTrans[0], self.OriginalGTrans[1], self.OriginalGTrans[2], self.OriginalGTrans[3], self.OriginalGTrans[4], self.OriginalGTrans[5] )
			self._x0, self._y0, self._xV, self._yV = self.gTrans[0], self.gTrans[3], self.gTrans[1], self.gTrans[5]
			self._nx, self._ny = ( ( self.nColumns * self._xV ) + self._x0 ), ( ( self.nRows * self._yV ) + self._y0 )
			self.Column0, self.ColumnN = 0, self.originalNColumns
			self.Row0, self.RowN = 0, self.originalNRows
			self._xN, self._yN = self._nx, self._ny
			self._subSet = False
		return None
	
	# Resize scene with respect to the pixel area
	def setPixelSize(self, dX=None, dY=None):
		if type(dX)==int:
			dX	= float(dX)
		elif type(dX)!=float:
			dX	= self.OriginalGTrans[1]
		if type(dY)==int:
			dY	= float(dY)
		elif type(dY)!=float:
			dY	= self.OriginalGTrans[5]
		if not (dX==self.gTrans[1] and dY==self.gTrans[5]):
			self.gTrans		= ( self._x0, dX, self.OriginalGTrans[2], self._y0, self.OriginalGTrans[4], dY )
			self.Column0	= int( ( float(self.gTrans[0]) - float(self.OriginalGTrans[0]) ) / self.gTrans[1] )
			self.ColumnN	= int( ( float(self._xN) - float(self.OriginalGTrans[0]) ) / self.gTrans[1] )
			self.nColumns	= self.ColumnN - self.Column0
			self.Row0		= int( ( float(self.gTrans[3]) - float(self.OriginalGTrans[3]) ) / self.gTrans[5] )
			self.RowN		= int( ( float(self._yN) - float(self.OriginalGTrans[3]) ) / self.gTrans[5] )
			self.nRows		= self.RowN - self.Row0
			self.img		= self.img.resize((self.nColumns, self.nRows))
			self._subSet	= True
		else:
			self._subSet	= False
		return None
	
	# Resize scene
	def resize(self, nColumns, nRows):
		if type(nColumns)==float:
			nColumns = int(nColumns)
		elif type(nColumns)!=int:
			nColumns = self.nColumns
		if type(nRows)==float:
			nRows = int(nRows)
		elif type(nRows)!=int:
			nRows = self.nRows
		if not (nColumns==self.nColumns and nRows==self.nRows):
			dX = float( nColumns * OriginalGTrans[1] / self.nColumns )
			dY = float( nRows * OriginalGTrans[5] / self.nRows )
			self.setPixelSize( dX, dY )
			del dX, dY
		return None
	
	# Class Destroyer
	def __del__(self):
		if self.img==None:
			del self._nx, self._ny, self._subSet, self._x0, self._xN, self._xV, self._y0, self._yN, self._yV, self.Column0, self.ColumnN, self.gTrans, self.nColumns, self.nRows, self.OriginalGTrans, self.originalNColumns, self.originalNRows, self.originalsample, self.proj, self.Row0, self.RowN
		del self.path, self.name, self.date, self.tDelta, self.distTime, self.img
		del self

# Class Scenes List
class scenes():
	
	# Clear the scenes list
	def clear(self):
		del self.nColumns, self.nRows, self.proj, self.gTrans
		self.nColumns, self.nRows, self.proj, self.gTrans = None, None, None, None
		self.point	= None
		while len(self.onlyLandCover)>0:
			del self.onlyLandCover[0]
		while len(self.scenes)>0:
			del self.scenes[0]
		return None
	
	# Class Builder
	def __init__(self):
		self.nColumns, self.nRows		= None, None
		self.proj, self.gTrans			= None, None
		self.onlyLandCover, self.scenes	= [], []
		self.point						= None
	
	# Get the geographical size max
	def sizeMax(self):
		x0, xN = 0, 0
		y0, yN = 0, 0
		if len( self.scenes )>0:
			xN, y0 = 999999999, 999999999
			for i in xrange(0,len( self.scenes )):
				s_x0, s_xN = self.scenes[i].gTrans[0], self.scenes[i].gTrans[0]+(self.scenes[i].gTrans[1]*self.scenes[i].nColumns)
				s_y0, s_yN = self.scenes[i].gTrans[3], self.scenes[i].gTrans[3]+(self.scenes[i].gTrans[5]*self.scenes[i].nRows)
				if s_x0 > x0:
					x0 = s_x0
				if s_xN < xN:
					xN = s_xN
				if s_y0 < y0:
					y0 = s_y0
				if s_yN > yN:
					yN = s_yN
				del s_x0, s_y0, s_xN, s_yN
		return x0, xN, y0, yN
	
	# Validates an external scene in the scenes list
	def valid(self, name, path, date):
		n, p, d, g = False, False, False, True
		for sc in self.scenes:
			p = p or (sc.path == path)
			n = n or (sc.name == name)
			d = d or (sc.date == date)
		if len(self.scenes)>0:
			x0, xN, y0, yN = self.sizeMax()
			sample = gdal.Open(path, gdalconst.GA_ReadOnly)
			gTrans = sample.GetGeoTransform()
			s_x0, s_xN = gTrans[0], gTrans[0]+(gTrans[1]*sample.RasterXSize)
			s_y0, s_yN = gTrans[3], gTrans[3]+(gTrans[5]*sample.RasterYSize)
			if not( s_x0>=x0 and s_x0<=xN and s_xN>=x0 and s_xN<=xN and s_y0<=y0 and s_y0>=yN and s_yN<=y0 and s_yN>=yN ):
				g = False
			del x0, xN, y0, yN, sample, gTrans, s_x0, s_xN, s_y0, s_yN
		return not n, not p, not d, g
	
	# Add scene in scenes list
	def add(self, name, path, date):
		go, i = True, 0
		while go:
			if i<len(self.scenes):
				if self.scenes[i].date < date:
					i = i + 1
				else:
					go = False
			else:
				go = False
		newScn = scene(name, path, date)
		if newScn.img != None:
			self.scenes.insert( i, newScn )
		del go, i, newScn
		return None
	
	# Get a tags list of the scenes list
	def tagList(self):
		result = []
		year, month, day, hour, minute = True, True, True, True, True
		if len(self.scenes)>1:
			i = 0
			while i<len(self.scenes)-1:
				year	= year and (self.scenes[i].date.year==self.scenes[i+1].date.year)
				month	= month and (self.scenes[i].date.month==self.scenes[i+1].date.month)
				day		= day and (self.scenes[i].date.day==self.scenes[i+1].date.day)
				hour	= hour and (self.scenes[i].date.hour==self.scenes[i+1].date.hour)
				minute	= minute and (self.scenes[i].date.minute==self.scenes[i+1].date.minute)
				i = i + 1
			day		= day
			month	= month and day
			year	= year
			hour	= hour and minute
			day		= not day
			month	= not month
			year	= not year
			hour	= not hour
			del i
		for sc in self.scenes:
			date = ""
			if year:
				date = str(sc.date.year)
			if month:
				if date!="":
					date = date + "/"
				date = date + str(sc.date.strftime('%B'))[:3]
			if day:
				if date!="":
					date = date + "/"
				date = date + str(sc.date.day)
			if hour:
				if date!="":
					date = date + " - "
				sHour = str(sc.date.hour)
				if sc.date.hour<10:
					sHour = "0" + sHour
				sMinute = str(sc.date.minute)
				if sc.date.minute<10:
					sMinute = "0" + sMinute
				date = date + sHour + ":" + sMinute
				del sHour, sMinute
			if date!="":
				date = "(" + date + ") "
			result.append( date + sc.name )
			del date
		del year, month, day, hour, minute
		return result
	
	# Prepare the scenes for analysis
	def process(self, wait=None):
		if len(self.scenes)>0:
			if len(self.scenes)>1:
				if wait!=None:
					wait.show()
					wait.ui.progressBar.setProperty("value", 0)
				x0, xN, y0, yN = self.sizeMax()
				pix = (0.0, 0.0)
				size = (0,0)
				area = 99999999999
				tamPix = 0.0
				tN = float((len(self.scenes)*3)+(len(self.scenes)-1))
				t = 0
				for j in range(len( self.scenes )):
					self.scenes[j].subSet(x0,y0,xN,yN)
					auxTam = abs( self.scenes[j].gTrans[1] * self.scenes[j].gTrans[5] )
					if auxTam>tamPix:
						pix = (self.scenes[j].gTrans[1], self.scenes[j].gTrans[5])
						tamPix = auxTam
					del auxTam
					t = t + 1
					if wait!=None:
						wait.ui.progressBar.setProperty("value", ((float(t)/tN)*100.0) )
				for j in range(len( self.scenes )):
					self.scenes[j].setPixelSize(pix[0], pix[1])
					auxTam = abs( self.scenes[j].nColumns * self.scenes[j].nRows )
					if auxTam<area:
						size = (self.scenes[j].nColumns, self.scenes[j].nRows)
						area = auxTam
					del auxTam
					t = t + 1
					if wait!=None:
						wait.ui.progressBar.setProperty("value", ((float(t)/tN)*100.0) )
				for j in range(len( self.scenes )):
					self.scenes[j].resize(size[0], size[1])
					self.scenes[j].timeDelta()
					t = t + 1
					if wait!=None:
						wait.ui.progressBar.setProperty("value", ((float(t)/tN)*100.0) )
				self.scenes[ len( self.scenes )-1 ].distTime = 1.0
				if len(self.scenes)>2:
					date = self.scenes[len( self.scenes )-1].tDelta - self.scenes[0].tDelta
					for j in xrange(1, len( self.scenes )-1):
						self.scenes[j].distTime = float( ( self.scenes[j].tDelta - self.scenes[0].tDelta ) / date )
						t = t + 1
						if wait!=None:
							wait.ui.progressBar.setProperty("value", ((float(t)/tN)*100.0) )
					del date
				del x0, xN, y0, yN, pix, size, area, tamPix, tN, t
				if wait!=None:
					wait.ui.progressBar.setProperty("value", 100)
			self.scenes[0].distTime = 0.0
			self.proj, self.gTrans = self.scenes[0].proj, self.scenes[0].gTrans
			self.nColumns, self.nRows = self.scenes[0].nColumns, self.scenes[0].nRows
		return None
	
	# Class Destroyer
	def __del__(self):
		while len(self.onlyLandCover)>0:
			del self.onlyLandCover[0]
		while len(self.scenes)>0:
			del self.scenes[0]
		del self.onlyLandCover, self.scenes, self.nColumns, self.nRows, self.proj, self.gTrans, self.point
		del self

listScenes = scenes()

# Help to select scenes dialog
class help1Dialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_help1()
		self.ui.setupUi(self)
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, 
		del self

# Help to select point dialog
class help2Dialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_help2()
		self.ui.setupUi(self)
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, 
		del self

# Help to result dialog
class help3Dialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_help3()
		self.ui.setupUi(self)
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, 
		del self

# Help to add scene dialog
class help4Dialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_help4()
		self.ui.setupUi(self)
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, 
		del self

# Help to crossroad dialog
class help5Dialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_help5()
		self.ui.setupUi(self)
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, 
		del self

# Decide the scenes list
class crossroadDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_crossroad()
		self.ui.setupUi(self)
		self.auxList = None
	
	# Show a help dialogue
	def help(self):
		dlg = help5Dialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show the Dialogue
	def show(self, auxList=None):
		self.auxList = auxList
		if self.auxList==None:
			self.accept()
		else:
			tags1, tags2 = self.auxList.tagList(), listScenes.tagList()
			self.ui.list1.clear()
			self.ui.list2.clear()
			for tag in tags1:
				self.ui.list1.addItem( QListWidgetItem(_translate("gapCorrecter", str(tag), None)) )
			for tag in tags2:
				self.ui.list2.addItem( QListWidgetItem(_translate("gapCorrecter", str(tag), None)) )
			del tags1, tags2
		return None
	
	# Change the new scenes list
	def process(self):
		if self.ui.buttonList1.isChecked():
			sc = self.auxList.scenes[0]
			listScenes.clear()
			listScenes.add(sc.name, sc.path, sc.date)
			del sc
		self.accept()
		return None
	
	# Class Destroyer
	def __del__(self):
		if self.auxList!=None:
			while len(self.auxList)>0:
				del self.auxList[0]
		del self.ui, self.iface, self.auxList
		del self

# Add a selected scene
class addSceneDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface		= iface
		QDialog.__init__(self)
		self.openedList	= []
		self.path		= sourceSave
		self.now		= None
		self.ui			= Ui_addScene()
		self.ui.setupUi(self)
	
	# Show a help dialogue
	def help(self):
		dlg = help4Dialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Change the hour of the scene date
	def editHour(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year and self.ui.month.value()==self.now.month and self.ui.day.value()==self.now.day and self.ui.hour.value()==self.now.hour:
			if self.ui.minute.value()>self.now.minute:
				self.ui.minute.setProperty( "value", self.now.minute )
			self.ui.minute.setMaximum( self.now.minute )
		else:
			self.ui.minute.setMaximum( 59 )
		return None
	
	# Change the day of the scene date
	def editDay(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year and self.ui.month.value()==self.now.month and self.ui.day.value()==self.now.day:
			if self.ui.hour.value()>self.now.hour:
				self.ui.hour.setProperty( "value", self.now.hour )
			self.ui.hour.setMaximum( self.now.hour )
		else:
			self.ui.hour.setMaximum( 23 )
		self.editHour()
		return None
	
	# Change the month of the scene date
	def editMonth(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year and self.ui.month.value()==self.now.month:
			if self.ui.day.value()>self.now.day:
				self.ui.day.setProperty( "value", self.now.day )
			self.ui.day.setMaximum( self.now.day )
		elif self.ui.month.value() in [1,3,5,7,8,10,12]:
			if self.ui.day.value()>31:
				self.ui.day.setProperty( "value", 31 )
			self.ui.day.setMaximum( 31 )
		elif self.ui.month.value() in [4,6,9,11]:
			if self.ui.day.value()>30:
				self.ui.day.setProperty( "value", 30 )
			self.ui.day.setMaximum( 30 )
		else:
			febDays = 28
			if self.ui.year.value()%4 == 0:
				febDays = 29
			if self.ui.day.value()>febDays:
				self.ui.day.setProperty( "value", febDays )
			self.ui.day.setMaximum( febDays )
			del febDays
		self.editDay()
		return None
	
	# Change the year of the scene date
	def editYear(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year:
			if self.ui.month.value()>self.now.month:
				self.ui.month.setProperty( "value", self.now.month )
			self.ui.month.setMaximum( self.now.month )
		else:
			self.ui.month.setMaximum( 12 )
		self.editMonth()
		return None
	
	# Refresh opened scenes list
	def refreshOpened(self):
		rasterLayers = self.iface.legendInterface().layers()
		while len(self.openedList)>0:
			del self.openedList[0]
		for lyr in rasterLayers:
			if lyr.type()==QgsMapLayer.RasterLayer:
				ext = str(lyr.source()).lower()
				while ext.find(".")>=0:
					ext = ext[ext.find(".")+1:]
				if ext in ["tif", "tiff"]:
					try:
						open(lyr.source(),'r')
					except IOError:
						None
					else:
						try:
							Image.open( lyr.source() )
						except IOError:
							None
						else:
							sample = gdal.Open( lyr.source(), gdalconst.GA_ReadOnly)
							proj, gTrans = sample.GetProjection(), sample.GetGeoTransform()
							if proj!="" and gTrans!=(0.0, 1.0, 0.0, 0.0, 0.0, 1.0):
								go = True
								for sc in listScenes.scenes:
									if sc.path == lyr.source():
										go = False
								if go:
									self.openedList.append( lyr.name() )
								del go
							del sample, proj, gTrans
				del ext
		self.ui.openedLayer.clear()
		for tag in self.openedList:
			self.ui.openedLayer.addItem( QListWidgetItem(_translate("gapCorrecter", str(tag), None)) )
		del rasterLayers
		return None
	
	# Change the scene ID
	def editID(self):
		name = str((self.ui.ID.text()).replace("/","").replace(" ","").replace(".","").replace(";","").replace("_","").replace("-","").replace("\\","").replace(":","").replace(",","").replace("(","").replace(")","")).lower()
		self.ui.ID.setText(name)
		del name
		return None
	
	# Change the scene path
	def editPath(self):
		name = self.ui.layerPath.text()
		name = str(os.path.abspath(name))
		while name.find(separatePath+separatePath)>=0:
			name = name.replace(separatePath+separatePath,separatePath)
		while name.find(separatePath)>=0:
			name = name[name.find(separatePath)+1:]
		if name.find(".")>=0:
			name = name[:name.find(".")]
		self.ui.ID.setText(name)
		self.editID()
		self.ui.buttonPath.setChecked( True )
		del name
		return None
	
	# Search a raster image
	def searchFile(self):
		path = QFileDialog.getOpenFileName(self, 'Select a Raster Layer', self.path, "TIFF (*.tif *.tiff)")
		path = str(os.path.abspath(path))
		if len(path)>0:
			self.ui.layerPath.setText(path)
			self.editPath()
			self.path = ""
			while path.find(separatePath)>=0:
				self.path = self.path + path[:path.find(separatePath)+1]
				path = path[path.find(separatePath)+1:]
		del path
		return None
	
	# Select a raster image
	def selectLayer(self):
		selecItems = self.ui.openedLayer.selectedItems()
		if len( selecItems ) == 1:
			self.ui.ID.setText( selecItems[0].text() )
			self.editID()
			self.ui.buttonOpened.setChecked( True )
		del selecItems	
		return None
	
	# Active mode path
	def activePath(self):
		name = self.ui.layerPath.text()
		if len(name)==0:
			self.searchFile()
		else:
			self.editPath()
		del name
		return None
	
	# Active mode list
	def activeList(self):
		if len( self.openedList ) == 0:
			self.activePath()
		else:
			self.selectLayer()
		return None
	
	# Show the Dialogue
	def show(self):
		self.now = datetime.now()
		self.ui.year.setMaximum( self.now.year )
		self.ui.year.setProperty( "value", self.now.year )
		self.ui.month.setProperty( "value", 1 )
		self.ui.day.setProperty( "value", 1 )
		self.ui.hour.setProperty( "value", 0 )
		self.ui.day.setProperty( "value", 0 )
		self.ui.ID.setText("")
		self.ui.layerPath.setText("")
		self.editYear()
		self.refreshOpened()
		if len(self.openedList)==0:
			self.searchFile()
			if self.ui.ID.text()=="":
				self.accept()
		return None
	
	# Validate the data and add the new scene
	def process(self):
		path = ""
		iD = self.ui.ID.text()
		selecItems = self.ui.openedLayer.selectedItems()
		if self.ui.buttonPath.isChecked():
			path = self.ui.layerPath.text()
			path = os.path.abspath(path)
		elif self.ui.buttonOpened.isChecked() and len( selecItems ) == 1:
			rasterLayers = self.iface.legendInterface().layers()
			for lyr in rasterLayers:
				if lyr.type()==QgsMapLayer.RasterLayer and lyr.name()==selecItems[0].text():
					path = lyr.source()
					path = os.path.abspath(path)
			del rasterLayers
		if path == "":
			QMessageBox.critical(self, "Alert!", "Select a raster layer." )
		elif iD == "":
			QMessageBox.critical(self, "Alert!", "Write the scene ID." )
		else:
			try:
				open(path,'r')
			except IOError:
				QMessageBox.critical(self, "Alert!", "File path invalid!" )
			else:
				try:
					Image.open( path )
				except IOError:
					QMessageBox.critical(self, "Alert!", "Corrupt file!" )
				else:
					sample = gdal.Open( path, gdalconst.GA_ReadOnly)
					proj, gTrans = sample.GetProjection(), sample.GetGeoTransform()
					if not( proj!="" and gTrans!=(0.0, 1.0, 0.0, 0.0, 0.0, 1.0) ):
						QMessageBox.critical(self, "Alert!", "This scene wasn't georeferenced!" )
					else:
						date = datetime(self.ui.year.value(), self.ui.month.value(), self.ui.day.value(), self.ui.hour.value(), self.ui.minute.value())
						n, p, d, g = listScenes.valid(iD, path, date)
						if not p:
							QMessageBox.critical(self, "Alert!", "This scene exists!" )
						elif not n:
							QMessageBox.critical(self, "Alert!", "This scene ID exists!" )
						elif not d:
							QMessageBox.critical(self, "Alert!", "There is a scene of the same date!" )
						elif not g:
							self.accept()
							dlg = crossroadDialog(self.iface)
							auxList = scenes()
							auxList.add(iD, path, date)
							if len(auxList.scenes)>0:
								dlg.show(auxList)
								dlg.exec_()
							auxList.clear()
							del auxList, dlg
						else:
							listScenes.add(iD, path, date)
							self.accept()
						del date, n, p, d, g
					del sample, proj, gTrans
		del path, iD, selecItems
		return None
	
	# Class Destroyer
	def __del__(self):
		while len(self.openedList)>0:
			del self.openedList[0]
		del self.ui, self.iface, self.path, self.now, self.openedList
		del self

# Edit the selected scene
class editSceneDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface	= iface
		QDialog.__init__(self)
		self.ui		= Ui_editScene()
		self.ui.setupUi(self)
		self.index	= None
		self.now	= None
	
	# Change the hour of the scene date
	def editHour(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year and self.ui.month.value()==self.now.month and self.ui.day.value()==self.now.day and self.ui.hour.value()==self.now.hour:
			if self.ui.minute.value()>self.now.minute:
				self.ui.minute.setProperty( "value", self.now.minute )
			self.ui.minute.setMaximum( self.now.minute )
		else:
			self.ui.minute.setMaximum( 59 )
		return None
	
	# Change the day of the scene date
	def editDay(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year and self.ui.month.value()==self.now.month and self.ui.day.value()==self.now.day:
			if self.ui.hour.value()>self.now.hour:
				self.ui.hour.setProperty( "value", self.now.hour )
			self.ui.hour.setMaximum( self.now.hour )
		else:
			self.ui.hour.setMaximum( 23 )
		self.editHour()
		return None
	
	# Change the month of the scene date
	def editMonth(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year and self.ui.month.value()==self.now.month:
			if self.ui.day.value()>self.now.day:
				self.ui.day.setProperty( "value", self.now.day )
			self.ui.day.setMaximum( self.now.day )
		elif self.ui.month.value() in [1,3,5,7,8,10,12]:
			if self.ui.day.value()>31:
				self.ui.day.setProperty( "value", 31 )
			self.ui.day.setMaximum( 31 )
		elif self.ui.month.value() in [4,6,9,11]:
			if self.ui.day.value()>30:
				self.ui.day.setProperty( "value", 30 )
			self.ui.day.setMaximum( 30 )
		else:
			febDays = 28
			if self.ui.year.value()%4 == 0:
				febDays = 29
			if self.ui.day.value()>febDays:
				self.ui.day.setProperty( "value", febDays )
			self.ui.day.setMaximum( febDays )
			del febDays
		self.editDay()
		return None
	
	# Change the year of the scene date
	def editYear(self):
		self.now = datetime.now()
		if self.ui.year.value()==self.now.year:
			if self.ui.month.value()>self.now.month:
				self.ui.month.setProperty( "value", self.now.month )
			self.ui.month.setMaximum( self.now.month )
		else:
			self.ui.month.setMaximum( 12 )
		self.editMonth()
		return None
	
	# Change the scene ID
	def editID(self):
		name = (self.ui.ID.text()).replace("/","").replace(" ","").replace(".","").replace(";","").replace("_","").replace("-","").replace("\\","").replace(":","").replace(",","").replace("(","").replace(")","").lower()
		self.ui.ID.setText(name)
		del name
		return None
	
	# Remove the scene selected
	def delete(self):
		if self.index!=None:
			del listScenes.scenes[self.index]
			self.accept()
		return None
	
	# Show the Dialogue
	def show(self, index):
		self.ui.year.setProperty( "value", listScenes.scenes[index].date.year )
		self.ui.month.setProperty( "value", listScenes.scenes[index].date.month )
		self.ui.day.setProperty( "value", listScenes.scenes[index].date.day )
		self.ui.hour.setProperty( "value", listScenes.scenes[index].date.hour )
		self.ui.minute.setProperty( "value", listScenes.scenes[index].date.minute )
		self.ui.ID.setText( listScenes.scenes[index].name )
		self.index = index
	
	# Validate the new data and edit the selected scene
	def process(self):
		newDate = datetime(self.ui.year.value(), self.ui.month.value(), self.ui.day.value(), self.ui.hour.value(), self.ui.minute.value())
		newID = self.ui.ID.text()
		if newID == "":
			QMessageBox.critical(self, "Alert!", "Write the scene ID." )
		else:
			n, d = False, False
			if len(listScenes.scenes)>1:
				i = 0
				while i<len(listScenes.scenes):
					if i!=self.index:
						n = n or (listScenes.scenes[i].name == newID)
						d = d or (listScenes.scenes[i].date == newDate)
					i = i + 1
				del i
			if n:
				QMessageBox.critical(self, "Alert!", "This scene ID exists." )
			elif d:
				QMessageBox.critical(self, "Alert!", "There is a scene of the same date." )
			else:
				if listScenes.scenes[self.index].name!=newID:
					listScenes.scenes[self.index].name = newID
				if listScenes.scenes[self.index].date!=newDate:
					path	= listScenes.scenes[self.index].path
					path	= os.path.abspath(str(path))
					del listScenes.scenes[self.index]
					listScenes.add(newID, path, newDate)
					del path
				self.accept()
			del n, d
		del newDate, newID
		return None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, self.index, self.now
		del self

# Show a about us dialogue
class aboutUsDialog(QDialog):
	
	# Remove the temporal folder
	def _removeTempFolder(self, dirPath=None):
		if dirPath==None:
			dirPath = os.path.abspath(self.tempFolder)
		else:
			dirPath = os.path.abspath(dirPath)
		if os.path.isfile(dirPath):
			try:
				os.remove(dirPath)
			except OSError:
				None
		elif os.path.isdir(dirPath):
			files = os.listdir(dirPath)
			for f in files:
				self._removeTempFolder(dirPath+separatePath+f)
			try:
				os.removedirs(dirPath)
			except OSError:
				None
			del files
		return None
	
	# Create a temporal folder
	def _createTempFolder(self):
		try:
			os.mkdir(self.tempFolder)
		except OSError:
			self._removeTempFolder()
			try:
				os.mkdir(self.tempFolder)
			except OSError:
				None
			else:
				if os.name=="nt":
					os.system( "attrib +h " + self.tempFolder )
		else:
			if os.name=="nt":
				os.system( "attrib +h " + self.tempFolder )
		return None
	
	# Class Builder
	def __init__(self, iface):
		self.iface	= iface
		QDialog.__init__(self)
		self.ui		= Ui_aboutUs()
		self.ui.setupUi(self)
		self.tempFolder = tempFolder + "2"
		self._createTempFolder()
		QFile.copy(":/plugins/multitemporalanalyzer/doc/degreeThesis.pdf",self.tempFolder+separatePath+"degreeThesis.pdf")
		if os.name=="nt":
			pdf = QFile(self.tempFolder+separatePath+"degreeThesis.pdf")
			pdf.setPermissions(QFile.ReadOther)
			pdf.setPermissions(QFile.WriteOther)
			pdf.setPermissions(QFile.ExeOther)
			pdf.close()
			del pdf
	
	# Open the degree thesis
	def degreeThesis(self):
		if os.name=="nt":
			comand = self.tempFolder+separatePath+"degreeThesis.pdf"
		else:
			comand = " /usr/bin/gnome-open  "+self.tempFolder+separatePath+"degreeThesis.pdf"
		os.system( comand )
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		self._removeTempFolder()
		del self.ui, self.iface, self.tempFolder
		del self

# Show a processing bar
class waitDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface	= iface
		QDialog.__init__(self)
		self.ui		= Ui_wait()
		self.ui.setupUi(self)
		self.ui.progressBar.setProperty("value", 0)
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface
		del self

# Get the land cover from a geographic coordinate
class selectPointDialog(QDialog):
	
	# Refresh raster image
	def refreshImage(self):
		im = listScenes.scenes[ len(listScenes.scenes)-1 ].img
		if im!=None:
			self.im = im.copy()
			iW, iH = self.lH*self.im.size[0]/self.im.size[1], self.lH
			if iW>self.lW:
				iW, iH = self.lW, self.lW*self.im.size[1]/self.im.size[0]
			self.im = self.im.resize((iW, iH))
			x = self.x * self.im.size[0] / im.size[0]
			y = self.y * self.im.size[1] / im.size[1]
			color = "red"
			draw = ImageDraw.Draw(self.im)
			draw.line((x, 0, x, self.im.size[1]), color)
			draw.line((0, y, self.im.size[0], y), color)
			QtImage1	= ImageQt.ImageQt(self.im)
			QtImage		= QImage(QtImage1)
			pixmap	= QPixmap.fromImage(QtImage)
			self.ui.scene.setPixmap( pixmap )
			del iW, iH, x, y, color, draw, QtImage1, QtImage, pixmap
		else:
			self.im 	= None
			self.ui.scene.setPixmap( None )
		del im
		return None
	
	# Get the point in the raster image of the geographical coordinate
	def setPoint(self):
		self.x = int( round( abs( ( self.ui.pointX.value() - self._x0 ) / self._xV ) , 0 ) )
		if self.x > listScenes.nColumns:
			self.x = listScenes.nColumns
		self.y = int( round( abs( ( self.ui.pointY.value() - self._y0 ) / self._yV ) , 0 ) )
		if self.y > listScenes.nRows:
			self.y = listScenes.nRows
		self.refreshImage()
		return None
	
	# Get the geographical coordinate of the point in the raster image
	def getPos(self , event):
		if self.im!=None:
			x = event.pos().x() - int( round( ( self.lW - self.im.size[0] ) / 2, 0 ) )
			y = event.pos().y() - int( round( ( self.lH - self.im.size[1] ) / 2, 0 ) )
			if x in range(self.im.size[0]) and y in range(self.im.size[1]):
				x = int( round( x * listScenes.nColumns / self.im.size[0], 0 ) )
				y = int( round( y * listScenes.nRows / self.im.size[1], 0 ) )
				valueX = float( ( x * self._xV ) + self._x0 )
				valueY = float( ( y * self._yV ) + self._y0 )
				self.ui.pointX.setProperty( "value", valueX )
				self.ui.pointY.setProperty( "value", valueY )
				self.setPoint()
				del valueX, valueY
			del x, y
		return None
	
	# Class Builder
	def __init__(self, iface):
		self.iface = iface
		QDialog.__init__(self)
		self.ui = Ui_selectPoint()
		self.ui.setupUi(self)
		self.x, self.y = 0, 0
		self._x0, self._y0 = listScenes.gTrans[0], listScenes.gTrans[3]
		self._xV, self._yV = abs(listScenes.gTrans[1]), abs(listScenes.gTrans[5])
		self._xN, self._yN = ( ( listScenes.nColumns * self._xV ) + self._x0 ), ( ( listScenes.nRows * self._yV ) + self._y0 )
		self.ui.scene.mousePressEvent = self.getPos
		self.lW, self.lH = 421, 221
		self.im = None
	
	# Show a help dialogue
	def help(self):
		dlg = help2Dialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show the Dialogue
	def show(self):
		self.ui.pointX.setMinimum( self._x0 )
		self.ui.pointX.setMaximum( self._xN )
		self.ui.pointY.setMinimum( self._y0 )
		self.ui.pointY.setMaximum( self._yN )
		self.ui.pointX.setSingleStep( self._xV )
		self.ui.pointY.setSingleStep( self._yV )
		self.ui.pointX.setProperty( "value", float( round( ( self._xN + self._x0 ) / 2.0 ) ) )
		self.ui.pointY.setProperty( "value", float( round( ( self._yN + self._y0 ) / 2.0 ) ) )
		self.ui.yesButton.setChecked( True )
		self.setPoint()
	
	# Runs multitemporal analysis from the scenes and data collected
	def process(self):
		self.accept()
		self.wait = waitDialog(self.iface)
		self.wait.ui.progressBar.setProperty("value", 0)
		listScenes.point = (self.x, self.y)
		self.wait.show()
		while len(listScenes.onlyLandCover)>0:
			del listScenes.onlyLandCover[0]
		i = 1
		for sc in listScenes.scenes:
			porc = ((float(i)/float(len(listScenes.scenes)*2.0))*100.0)
			listScenes.onlyLandCover.append( getSimilarPixels(self.wait, porc, self.ui.yesButton.isChecked(), sc.img, listScenes.point) )
			self.wait.ui.progressBar.setProperty("value", porc )
			del porc
			i = i + 1
		if len(listScenes.onlyLandCover)==0 and listScenes.point!=None:
			listScenes.point = None
		elif len(listScenes.onlyLandCover)>0:
			t = 50.0
			tN = t/float(len(listScenes.onlyLandCover)+1)
			x0, y0, xN, yN = (listScenes.onlyLandCover[0])[1].size[0]-1, (listScenes.onlyLandCover[0])[1].size[1]-1, 0, 0
			for sc in listScenes.onlyLandCover:
				pix = sc[1].load()
				x = sc[1].size[0]
				while x>0:
					x = x - 1
					y = sc[1].size[1]
					while y>0:
						y = y - 1
						if pix[x,y]!=(0,0,0,0):
							if x<x0:
								x0 = x
							if x>xN:
								xN = x
							if y<y0:
								y0 = y
							if y>yN:
								yN = y
					del y
				t = t + tN
				self.wait.ui.progressBar.setProperty("value", t)
				del pix, x
			for sc in range(len(listScenes.onlyLandCover)):
				value = abs( float(listScenes.onlyLandCover[sc][0]) * float(listScenes.gTrans[1]) * float(listScenes.gTrans[5]) ) / 1000.0
				listScenes.onlyLandCover[sc] = (value, listScenes.onlyLandCover[sc][1].crop((x0, y0, xN+1, yN+1)))
				del value
			del t, tN, x0, y0, xN, yN
		self.wait.ui.progressBar.setProperty("value", 100)
		del self.wait, i
		return None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface, self.x, self.y, self._x0, self._y0, self._xV, self._yV, self._xN, self._yN, self.lW, self.lH, self.im
		del self

# Show the results of the analysis
class reportDialog(QDialog):
	
	# Show a about us dialogue
	def aboutUs(self):
		dlg = aboutUsDialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Save the report in a file
	def save(self):
		filePath=None
		while filePath==None:
			filePath = str(QFileDialog.getSaveFileName(self, 'Save the report', sourceSave, "PDF (*.pdf)"))
			if filePath!="":
				if filePath.find(".pdf")<0:
					QMessageBox.critical(self, "Alert!", "The file extension must be ""pdf""." )
					filePath = None
				elif len(filePath)<5:
					QMessageBox.critical(self, "Alert!", "The report name is not valid." )
					filePath = None
		if filePath!="" and filePath!=None:
			self.printer	= QPrinter(QPrinterInfo.defaultPrinter(),QPrinter.HighResolution)
			self.printer.setColorMode(QPrinter.Color)
			self.printer.setOutputFormat(QPrinter.PdfFormat)
			self.printer.setOrientation(QPrinter.Portrait)
			self.printer.setPaperSize(QPrinter.A4)
			self.printer.setFullPage(True)
			self.printer.setResolution(72)
			self.printer.setOutputFileName(filePath)
			self.web.print_(self.printer)
		del filePath
		return None
	
	# Print the report
	def printReport(self):
		self.printer	= QPrinter()
		dialog			= QPrintDialog(self.printer, self)
		if dialog.exec_()==QDialog.Accepted:
			self.web.print_(self.printer)
		del dialog
		return None
	
	# Class Builder
	def __init__(self, iface):
		self.iface		= iface
		QDialog.__init__(self)
		self.ui			= Ui_report()
		self.ui.setupUi(self)
		self.web		= QWebView()
		self.printer	= QPrinter()
		self.graphic	= None
		self.tempFolder	= tempFolder
		self.web.setZoomFactor(1)
	
	# Remove the temporary folder for report elements
	def _removeTempFolder(self, dirPath=None):
		if dirPath==None:
			dirPath = os.path.abspath(self.tempFolder)
		else:
			dirPath = os.path.abspath(dirPath)
		if os.path.isfile(dirPath):
			try:
				os.remove(dirPath)
			except OSError:
				None
		elif os.path.isdir(dirPath):
			files = os.listdir(dirPath)
			for f in files:
				self._removeTempFolder(dirPath+separatePath+f)
			try:
				os.removedirs(dirPath)
			except OSError:
				None
			del files
		return None
	
	# Create a temporary folder for report elements
	def _createTempFolder(self):
		try:
			os.mkdir(self.tempFolder)
		except OSError:
			self._removeTempFolder()
			try:
				os.mkdir(self.tempFolder)
			except OSError:
				None
			else:
				if os.name=="nt":
					os.system( "attrib +h " + self.tempFolder )
		if os.name=="nt":
			os.system( "attrib +h " + self.tempFolder )
		sizeX = 350
		if self.graphic!=None:
			im = self.graphic.copy()
			if (im.size[0]>0) and (im.size[1]>0):
				im		= im.resize((sizeX, int(round(sizeX*im.size[1]/im.size[0],0))))
				draw	= ImageDraw.Draw(im)
				for i in range(20):
					auxY = int( round( ( float(i) / 20.0 ) * im.size[1], 0 ) )
					draw.line((0, auxY, 5, auxY), (0,0,0,255))
					if i%5==0:
						draw.line((6, auxY, 10, auxY), (0,0,0,255))
						draw.text( (7, auxY), str((20-i)*5)+"%", (0,0,0) )
				
				tags = listScenes.tagList()
				
				xN = im.size[0]/len(tags)
				for i in range(len(tags)):
					txt = tags[i][str(tags[i]).find("(")+1:str(tags[i]).find(") ")]
					w, h = draw.textsize(txt)
					if i<(len(listScenes.scenes)-1):
						w = w + 3
					draw.text( (((i+1)*xN)-w, im.size[1]-h-5), txt, (0,0,0) )
				im.save(self.tempFolder+separatePath+"graphic.png")
				del tags, draw
			del im
		i = 1
		for cover in listScenes.onlyLandCover:
			im = cover[1].copy()
			if (im.size[0]+im.size[1])>0:
				pix = im.load()
				for x in range(im.size[0]):
					for y in range(im.size[1]):
						if pix[x,y]!=(0,0,0,0):
							pix[x,y] = (0,0,0,255)
				im = im.resize((sizeX, int(round(sizeX*im.size[1]/im.size[0],0))))
				im.save(self.tempFolder+separatePath+"cover"+str(i)+".png")
				del pix
			i = i + 1
			del im
		del i, sizeX
		return None
	
	# Show the Dialogue
	def show(self):
		tags = listScenes.tagList()
		self._createTempFolder()
		htmlGo		= "<!DOCTYPE HTML PUBLIC ""-//W3C//DTD HTML 4.0//EN"" ""http://www.w3.org/TR/REC-html40/strict.dtd""><html><head><meta name=""qrichtext"" content=""1"" /></head><body>"
		htmlEnd		= "</body></html>"
		htmlBody	= ""
		printBody	= "<h1>Multitemporal Analysis Report</h1>"
		
		# Date
		msg		= ""
		if len(tags)>1:
			msg	= " to " + tags[len(tags)-1][tags[len(tags)-1].find("(")+1:tags[len(tags)-1].find(")")]
		if len(tags)>0:
			msg	= tags[0][tags[0].find("(")+1:tags[0].find(")")] + msg
			htmlBody	= htmlBody + "<b>Date:</b><blockquote>" + msg + ".</blockquote>"
			printBody	= printBody + "<b>Date:</b><blockquote>" + msg + ".</blockquote>"
		
		# Extent coordinates
		msg		= ""
		if len(tags)>0:
			extent 		= listScenes.sizeMax()
			msg			= "<blockquote><b>x:</b> " + str(int(round(extent[0],0))) + " to "+ str(int(round(extent[1],0))) + ".</blockquote><blockquote><b>y:</b> " + str(int(round(extent[3],0))) + " to " + str(int(round(extent[2],0))) + ".</blockquote>"
			htmlBody	= htmlBody + "<b>Extent coordinates:</b> " + msg
			printBody	= printBody + "<b>Extent coordinates:</b> " + msg
			del extent
		
		# Image Size
		msg		= ""
		if len(tags)>0:
			area		= (abs(listScenes.gTrans[1])*abs(listScenes.gTrans[5]))
			htmlBody	= htmlBody + "<b>Image size:</b><blockquote>" + str(listScenes.onlyLandCover[0][1].size[0]) + "x" + str(listScenes.onlyLandCover[0][1].size[1]) + " pixels (" + strArea(area) + "<span style=\" vertical-align:super;\">2</span>/pixel).</blockquote>"
			printBody	= printBody + "<b>Image size:</b><blockquote>" + str(listScenes.onlyLandCover[0][1].size[0]) + "x" + str(listScenes.onlyLandCover[0][1].size[1]) + " pixels (" + strArea(area) + "<span style=\" vertical-align:super;\">2</span>/pixel).</blockquote>"
			del area
		
		# Tabla & Graphic
		path = os.path.abspath(self.tempFolder+separatePath+"graphic.png")
		pathUrl = QUrl.fromLocalFile(path).toString()
		msg		= ""
		if len(tags)>0:
			tableGo1		= "<table border=""0""><tr><td><img src="" " + path + " "" /></td><td><table border=""1""><tr><td>Date</td><td>Area</td></tr>"
			tableGo2		= "<table border=""0""><tr><td><img src="" " + pathUrl + " "" /></td><td><table border=""1""><tr><td>Date</td><td>Area</td></tr>"
			tableEnd	= "</table></td></tr></table>"
			for i in range(len(listScenes.scenes)):
				msg = msg + "<tr><td>" + str(tags[i])[str(tags[i]).find("(")+1:str(tags[i]).find(")")] + "</td><td>" + strArea(listScenes.onlyLandCover[i][0]) + "<span style=\" vertical-align:super;\">2</span></td></tr>"
			htmlBody	= htmlBody + "<b>Graphic:</b><blockquote>" + tableGo1 + msg + tableEnd + "</blockquote>" + "<hr>"
			printBody	= printBody + "<b>Graphic:</b><blockquote>" + tableGo2 + msg + tableEnd + "</blockquote>" + "<hr>"
			del tableGo1, tableGo2, tableEnd
		
		# Scenes
		msg		= ""
		msgUrl	= ""
		for i in range(len(listScenes.scenes)):
			path = os.path.abspath(self.tempFolder+separatePath+"cover"+str(i+1)+".png")
			sc = "Scene " + str(i+1) + " (" + tags[i][tags[i].find("(")+1:tags[i].find(")")] + "): " + strArea(listScenes.onlyLandCover[i][0]) + "<span style=\" vertical-align:super;\">2</span>"
			sc = sc + "<blockquote><img src="" "+path+" "" /></blockquote>"
			msg = msg + sc + "<Br>"
			path = QUrl.fromLocalFile(path).toString()
			sc = "Scene " + str(i+1) + " (" + tags[i][tags[i].find("(")+1:tags[i].find(")")] + "): " + strArea(listScenes.onlyLandCover[i][0]) + "<span style=\" vertical-align:super;\">2</span>"
			sc = sc + "<blockquote><img src="" "+path+" "" /></blockquote>"
			msgUrl = msgUrl + sc + "<Br>"
			del sc
		htmlBody	= htmlBody + "<b>Scenes:</b><blockquote>" + msg + "</blockquote>"
		printBody	= printBody + "<b>Scenes:</b><blockquote>" + msgUrl + "</blockquote>" + "<hr>"
		printBody	= printBody + "QGIS Plugin: Multitemporal Analyzer. Arturo Mendoza (arturo.amb89@gmail.com)<Br>"
		printBody	= printBody + "University of Carabobo (Venezuela)"
		self.web.setHtml( htmlGo + printBody + htmlEnd )
		self.ui.textEdit.setHtml( htmlGo + htmlBody + htmlEnd )
		del htmlBody, htmlEnd, htmlGo, msg, msgUrl, path, pathUrl, printBody, tags
		return None
	
	# Class Destroyer
	def __del__(self):
		self._removeTempFolder()
		del self.ui, self.iface, self.web, self.printer
		del self

# Show the results of the analysis
class resultDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface				= iface
		QDialog.__init__(self)
		self.scaleLine_color	= (0,0,0,255)
		self.scaleLine_size		= 5
		self.reportDlg			= reportDialog(self.iface)
		self.ui					= Ui_result()
		self.ui.setupUi(self)
		self.dlg				= None
		self.resultingScenes	= []
	
	# Chage tab in the dialog
	def setTab(self):
		selecItems = self.ui.scenesList.selectedItems()
		if len( selecItems ) == 1:
			aux = str(selecItems[0].text())
			aux = aux[:aux.find(" (")]
			tags = listScenes.tagList()
			for i in range(len(tags)):
				if str(tags[i])[str(tags[i]).find("(")+1:str(tags[i]).find(")")]==aux:
					self.ui.tabWidget.setCurrentIndex(i+1)
			del aux, tags
		del selecItems
		return None
	
	# Show a about us dialogue
	def aboutUs(self):
		dlg = aboutUsDialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show a help dialogue
	def help(self):
		dlg = help3Dialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show the report dialogue
	def report(self):
		self.reportDlg.show()
		self.reportDlg.exec_()
		return None
	
	# Close this dialog and show home dialog of the plugin
	def new(self):
		self.accept()
		self.dlg = homeDialog(self.iface)
		self.dlg.show()
		self.dlg.exec_()
		return None
	
	# Show the Dialogue
	def show(self):
		if len(listScenes.onlyLandCover)>0:
			tags = listScenes.tagList()
			
			sizeLabel	= (682, 341)
			sizeImg		= (682, 341)
			if sizeLabel[1]>sizeLabel[0]:
				sizeImg = (int(round(sizeLabel[0]*sizeImg[1]/sizeLabel[1],0)), sizeImg[1])
			else:
				sizeImg = (sizeImg[0], int(round(sizeLabel[1]*sizeImg[0]/sizeLabel[0],0)))
			result	= Image.new("RGBA", sizeImg, (0,0,0,0))
			draw	= ImageDraw.Draw(result)
			
			areaMax	= 0.0
			for cover in listScenes.onlyLandCover:
				if cover[0]>areaMax:
					areaMax = cover[0]
			sizeX	= sizeImg[0]-self.scaleLine_size
			sizeY	= sizeImg[1]-self.scaleLine_size
			minX	= self.scaleLine_size
			maxX	= sizeImg[0]-self.scaleLine_size
			points	= []
			
			lineSize = 2
			if lineSize<1:
				lineSize = 1
			
			x0, xN = minX, (float(maxX-minX)/float(len(listScenes.scenes)))
			x1 = xN
			for i in range(len(listScenes.scenes)):
				if i==(len(listScenes.scenes)-1):
					x0, x1 = x1, maxX
				elif i>0:
					x0, x1 = x1, x1+xN
				y = int(round(sizeY-((sizeY*listScenes.onlyLandCover[i][0])/areaMax),0))
				points.append( (x0, y) )
				points.append( (x1, y) )
				del y
			
			points = [(minX, sizeY)] + points + [(maxX, sizeY)]
			draw.polygon(points, (200,200,200,255))
			lineColor = (75, 75, 75, 255)
			for i in range(len(points)-1):
				if points[i][1]!=points[i+1][1]:
					y = points[i+1][1]
					if points[i][1]<points[i+1][1]:
						y = points[i][1]
					for j in range(lineSize):
						draw.line((points[i][0]-j, sizeY, points[i+1][0]-j, y), lineColor)
					del y
				else:
					for j in range(lineSize):
						draw.line((points[i][0], points[i][1]+j, points[i+1][0], points[i+1][1]+j), lineColor)
			for i in range(self.scaleLine_size):
				draw.line((i, 0, i, sizeY), (0,0,0,255))
				draw.line((0, sizeY-i, sizeImg[0], sizeY-i), (0,0,0,255))
			
			self.reportDlg.graphic = result.copy()
			
			n = 20
			deltaY = float(sizeY)/float(n)
			for i in range(n):
				draw.line((self.scaleLine_size, int(float(i)*deltaY), self.scaleLine_size*4.0, int(float(i)*deltaY)), (0,0,0,255))
			
			y = int(float(n-2)*deltaY)
			for i in range(len(listScenes.scenes)):
				txt = tags[i][str(tags[i]).find("(")+1:str(tags[i]).find(") ")]
				w, h = draw.textsize(txt)
				if i<(len(listScenes.scenes)-1):
					w = w + 3
				draw.text( (((i+1)*xN)-w, y), txt, (0,0,0) )
			
			n = 4
			porc = 100
			deltaY = float(sizeY)/float(n)
			for i in range(n):
				y = int(float(i)*deltaY)
				draw.line( (self.scaleLine_size*4.0, y, self.scaleLine_size*8.0, y), (0,0,0,255) )
				draw.text( (self.scaleLine_size+1, y), (str(int(porc*(float(n-i)/float(n))))+"%"), (0,0,0) )
			draw.text( (self.scaleLine_size+1, (int(sizeY)-self.scaleLine_size-8)), "0 %", (0,0,0) )
			
			QtImage1	= ImageQt.ImageQt(result)
			QtImage2	= QImage(QtImage1)
			pixmap		= QPixmap.fromImage(QtImage2)
			self.ui.graphic.setPixmap( pixmap )
			
			self.resultingScenes = []
			for i in range(len(listScenes.onlyLandCover)):
				self.resultingScenes.append( ( QWidget(), None , None , None , None ) )
				
				img = QLabel( self.resultingScenes[i][0] )
				lH, lW = 261, 821
				img.setGeometry(QRect(10, 70, lW, lH))
				img.setText("")
				im = listScenes.onlyLandCover[i][1].copy()
				if im.size[0]>0 and im.size[1]>0:
					iW, iH = lH*im.size[0]/im.size[1], lH
					if iW>lW:
						iW, iH = lW, lW*im.size[1]/im.size[0]
					im = im.resize((iW, iH))
					QtImage1	= ImageQt.ImageQt(im)
					QtImage2	= QImage(QtImage1)
					pixmap		= QPixmap.fromImage(QtImage2)
					img.setPixmap( pixmap )
					img.setAlignment(Qt.AlignCenter)
					
					iD = QLabel( self.resultingScenes[i][0] )
					iD.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">"+listScenes.scenes[i].name+"</span></p></body></html>")
					iD.setGeometry(QRect(10, 10, 521, 21))
					iD.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
					
					dateTime = QLabel( self.resultingScenes[i][0] )
					dateTime.setText(str(tags[i])[str(tags[i]).find("(")+1:str(tags[i]).find(") ")])
					dateTime.setGeometry(QRect(10, 30, 521, 21))
					dateTime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
					
					area = QLabel( self.resultingScenes[i][0] )
					
					value = float(listScenes.onlyLandCover[i][0])
					area.setText("<html><head/><body><p>"+strArea(listScenes.onlyLandCover[i][0])+"<span style=\" vertical-align:super;\">2</span></p></body></html>")
					area.setGeometry(QRect(10, 50, 521, 21))
					area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
					
					self.ui.tabWidget.addTab( self.resultingScenes[i][0] , str(tags[i])[str(tags[i]).find("(")+1:str(tags[i]).find(") ")] )
					self.resultingScenes[i] = (self.resultingScenes[i][0], img, iD, dateTime, area)
					del iW, iH, iD, dateTime, area, value
				del img, im, lH, lW
			for i in range(len(tags)):
				if str(tags[i]).find("(")>=0:
					tag = tags[i][str(tags[i]).find("(")+1:str(tags[i]).find(") ")]
					self.ui.scenesList.addItem( QListWidgetItem(_translate("", str(tag)+" ("+strArea(listScenes.onlyLandCover[i][0])+"2)", None)) )
					del tag
			
			while len(points)>0:
				del points[0]
			del deltaY, draw, lineColor, lineSize, maxX, minX, n, pixmap, points, QtImage1
			del QtImage2, result, sizeImg, sizeLabel, sizeX, sizeY, x0, x1, xN, y
	
	# Class Destroyer
	def __del__(self):
		del self.scaleLine_color, self.scaleLine_size, self.reportDlg, self.iface, self.ui, self.dlg, self.resultingScenes
		del self

# Select the scenes for the analysis.
class selectScenesDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface		= iface
		QDialog.__init__(self)
		self.ui			= Ui_selectScenes()
		self.ui.setupUi(self)
		self.listPath	= sourceSave
		self.listName	= ""
		self.save		= True
		self.lastScenes	= False
		self.add		= None
	
	# Refres tags of the scenes list
	def refreshTags(self):
		tags = listScenes.tagList()
		self.ui.listLayer.clear()
		for tag in tags:
			self.ui.listLayer.addItem( QListWidgetItem(_translate("gapCorrecter", str(tag), None)) )
		del tags
		return None
	
	# Save the scenes list
	def _save(self, filePath=None):
		while filePath==None:
			filePath = str(os.path.abspath(str(QFileDialog.getSaveFileName(self, 'Save the Layers List', self.listPath, "TXT (*.txt)"))))
			if len(filePath)>0 and filePath.find(".txt")<0:
				QMessageBox.critical(self, "Alert!", "The file extension must be ""txt""." )
				filePath = None
		if filePath!="":
			filePath = str(os.path.abspath(filePath))
			self.listName = "" + filePath
			self.listPath = ""
			while self.listName.find(separatePath)>=0:
				self.listPath = self.listPath + self.listName[:self.listName.find(separatePath)+1]
				self.listName = self.listName[self.listName.find(separatePath)+1:]
			self.listPath = os.path.abspath(self.listPath)
			
			fileList = None
			try:
				open(filePath,'r')
			except IOError:
				fileList = open(filePath,'w')
			else:
				os.remove(filePath)
				fileList = open(filePath,'w')
			
			fileList.write("Multitemporal Analyzer\n")
			for sc in listScenes.scenes:
				fileList.write(sc.name + " " + str(sc.date) + " " + sc.path + "\n")
			fileList.close()
			self.save = False
			del fileList
			
			if os.name=="nt":
				fileList = QFile(filePath)
				fileList.setPermissions(QFile.ReadOther)
				fileList.setPermissions(QFile.WriteOther)
				fileList.setPermissions(QFile.ExeOther)
				fileList.close()
				del fileList
		return None
	
	# Save the scenes list
	def saveList(self):
		if len(listScenes.scenes)==0:
			QMessageBox.critical(self, "Alert!", "You must add (at least) a scene." )
		elif self.lastScenes:
			self._save()
		elif not self.save:
			QMessageBox.warning(self, "Alert!", "The set list of scenes hasn't been modified.")
		else:
			self._save()
		return None
	
	# Load a scenes list
	def Open(self, filePath=""):
		add = 0
		if filePath != "":
			filePath = str(os.path.abspath(filePath))
			self.listName = "" + filePath
			self.listPath = ""
			while self.listName.find(separatePath)>=0:
				self.listPath = self.listPath + self.listName[:self.listName.find(separatePath)+1]
				self.listName = self.listName[self.listName.find(separatePath)+1:]
			fileList = open(filePath,'r')
			line = fileList.readline()
			if line == "Multitemporal Analyzer\n":
				line = str(fileList.readline())
				while line!="":
					name = line[:line.find(" ")]
					line = line[line.find(" ")+1:]
					year = line[ :line.find(" ") ]
					month = year[ year.find("-")+1: ]
					day = int(month[ month.find("-")+1: ])
					year = int(year[ :year.find("-") ])
					month = int(month[ :month.find("-") ])
					line = line[line.find(" ")+1:]
					hour = line[:line.find(" ")]
					minute = hour[ hour.find(":")+1 : ]
					minute = int(minute[ : minute.find(":") ])
					hour = int(hour[:hour.find(":")])
					date = datetime(year, month, day, hour, minute)
					path = line[line.find(" ")+1:line.find("\n")]
					n, p, d, g = listScenes.valid(name, path, date)
					if n and p and d and g:
						try:
							open(path,'r')
						except IOError:
							None
						else:
							try:
								Image.open( path )
							except IOError:
								None
							else:
								add = add + 1
								listScenes.add(name, path, date)
					line = fileList.readline()
					del name, path, year, month, day, hour, minute, n, p, d, g
				if add==len(listScenes.scenes):
					self.save = False
				else:
					self.save = True
					self.lastScenes	= False
			fileList.close()
			self.refreshTags()
			del line, fileList
		del add
		return None
	
	# Load a scenes list
	def openList(self):
		self.Open( QFileDialog.getOpenFileName(self, 'Select a Layers List', self.listPath, "TXT (*.txt)") )
		return None
	
	# Add a new scene in the scene list
	def add(self):
		before = len(listScenes.scenes)
		self.add = addSceneDialog(self.iface)
		self.add.show()
		self.add.exec_()
		if before != len(listScenes.scenes):
			self.save = True
		self.refreshTags()
		del before
		return None
	
	# Remove the selected scene of the scene list
	def remove(self):
		selecItem = self.ui.listLayer.selectedItems()
		if len(selecItem)==1:
			i = 0
			go = True
			name = str(selecItem[0].text())
			name = name[name.find(") ")+2:]
			while i<len(listScenes.scenes) and go:
				if name==listScenes.scenes[i].name:
					go = False
					self.save = True
					self.lastScenes	= False
					del listScenes.scenes[i]
				i = i + 1
			self.refreshTags()
			del i, go, name
		elif len(listScenes.scenes)>0 and len(selecItem)==0:
			msg = ""
			if len(listScenes.scenes)>1:
				msg = "You don't select any scene.\nDo you want to remove all scenes?"
			else:
				msg = "You don't select the scene.\nDo you want to remove the scene?"
			ret = QMessageBox.warning(self, "Alert!", msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No )
			if ret == QMessageBox.Yes:
				listScenes.clear()
				self.refreshTags()
			del msg, ret
		del selecItem
		return None
	
	# Show a help dialogue
	def help(self):
		dlg = help1Dialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show a about us dialogue
	def aboutUs(self):
		dlg = aboutUsDialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Edit the selected scene of the scene list
	def edit(self):
		selecItem = self.ui.listLayer.selectedItems()
		if len(selecItem)==1:
			i = 0
			go = True
			name = str(selecItem[0].text())
			name = name[name.find(") ")+2:]
			while i<len(listScenes.scenes) and go:
				if name==listScenes.scenes[i].name:
					dlg = editSceneDialog(self.iface)
					go = False
					dlg.show(i)
					result = dlg.exec_()
					if result == 1:
						self.save = True
						self.lastScenes	= False
						self.refreshTags()
					del dlg, result
				else:
					i = i + 1
			del i, go, name
		del selecItem
		return None
	
	# Show the Dialogue
	def show(self):
		self.refreshTags()
		return None
	
	# Prepare the scenes for analysis
	def process(self):
		if len(listScenes.scenes)<2:
			QMessageBox.critical(self, "Alert!", "You must add (at least) two scenes." )
		else:
			self.accept()
			self._save(lastScenesPath)
			if os.name=="nt":
				os.system( "attrib +h " + lastScenesPath )
			if self.save:
				ret = QMessageBox.warning(self, "Alert!", "The set list of scenes has been modified.\nDo you want to save your changes?", QMessageBox.Save | QMessageBox.Discard, QMessageBox.Save)
				if ret==QMessageBox.Save:
					self.saveList()
				del ret
			self.wait = waitDialog(self.iface)
			listScenes.process(self.wait)
			del self.wait
			sp = selectPointDialog(self.iface)
			sp.show()
			result = sp.exec_()
			if result == 1:
				r = resultDialog(self.iface)
				r.show()
				r.exec_()
				del r
			del sp, result
		return None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.listPath, self.listName, self.iface, self.save, self.lastScenes, self.add
		del self

# Main dialog of the plugin
class homeDialog(QDialog):
	
	# Class Builder
	def __init__(self, iface):
		self.iface	= iface
		QDialog.__init__(self)
		self.ui		= Ui_home()
		self.ui.setupUi(self)
	
	# Load a new scenes list
	def createList(self):
		self.accept()
		listScenes.clear()
		dlgAdd1 = addSceneDialog(self.iface)
		dlgAdd1.show()
		resultAdd = dlgAdd1.exec_()
		if resultAdd == 1 and len(listScenes.scenes)==1:
			dlgAdd2 = addSceneDialog(self.iface)
			dlgAdd2.show()
			dlgAdd2.exec_()
			del dlgAdd2
		dlg = selectScenesDialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg, dlgAdd1, resultAdd
		return None
	
	# Load a scenes list
	def openList(self):
		self.accept()
		listScenes.clear()
		dlg = selectScenesDialog(self.iface)
		dlg.openList()
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Load the analyzed last scenes list
	def lastList(self):
		self.accept()
		listScenes.clear()
		dlg = selectScenesDialog(self.iface)
		try:
			open(lastScenesPath,'r')
		except IOError:
			None
		else:
			dlg.Open(lastScenesPath)
			if len(listScenes.scenes)>0:
				dlg.lastScenes = True
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show a about us dialogue
	def aboutUs(self):
		dlg = aboutUsDialog(self.iface)
		dlg.show()
		dlg.exec_()
		del dlg
		return None
	
	# Show the Dialogue
	def show(self):
		None
	
	# Class Destroyer
	def __del__(self):
		del self.ui, self.iface
		del self

# Main class of the plugin
class multitemporalAnalyzer:
	
	# Class Builder
	def __init__(self, iface):
		self.iface		= iface
		self.plugin_dir	= os.path.dirname(__file__)
		locale			= str(QSettings().value("locale/userLocale"))[0:2]
		localePath		= os.path.join(self.plugin_dir, 'i18n', 'multitemporalanalyzer_{}.qm'.format(locale))
		self.translator = None
		self.action		= None
		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)
			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)
		self.dlg		= homeDialog(self.iface)
		del locale, localePath
	
	# Initialization in QGIS
	def initGui(self):
		self.action = QAction(
			QIcon(":/plugins/multitemporalanalyzer/icon/icon.png"),
			u"Multitemporal Analyzer", self.iface.mainWindow())
		self.action.triggered.connect(self.run)
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"&Multitemporal Analyzer", self.action)
	
	# Remove to QGIS
	def unload(self):
		self.iface.removePluginMenu(u"&Multitemporal Analyzer", self.action)
		self.iface.removeToolBarIcon(self.action)
	
	# Run the plugin
	def run(self):
		listScenes.clear()
		self.dlg.show()
		self.dlg.exec_()
	
	# Class Destroyer
	def __del__(self):
		del listScenes, self.iface, self.plugin_dir, self.translator, self.dlg, self.action
		del self
