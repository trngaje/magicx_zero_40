# encoding=utf8
import importlib
import sys
import os.path

if sys.version[0] == '2':
	importlib.reload(sys)
	sys.setdefaultencoding('utf-8')

#ESLIST = sys.argv[1]
import xml.etree.ElementTree as ET
tree = ET.parse('gamelist.xml')
root = tree.getroot()

import re
a = open('saveRoms.json', 'w')
a.close()

f = open('saveRoms.json', 'a+')
f.write ( '{\"TateGame\":{')

for game in root.iterfind('game'):
	path = game.find('path').text
	if path == None:	path = ''
	else:
		path = re.sub("\.[^.]*$", "", path)
		path = re.sub("./", "", path)

	name = game.find('name').text
	if name == None:	name = ''

	developer = game.findtext('developer')
	if developer == None:	developer = ''

	genre = game.findtext('genre')
	if genre == None:	genre = ''

	players = game.findtext('players')
	if players == None:	players = ''

	releasedate = game.findtext("releasedate")
	if releasedate == None:     releasedate = ''

    # {"TateGame":{"1941.zip":{"romName":"1941_good"}}}
	#f = open('saveRoms.json', 'a+')
	#f.write ( '{\"TateGame\":{\"' + path + '.zip\":{\"romName\":\"' + name + '\"}}}\n')
	if os.path.isfile(path + '.zip'):
		f.write ( '\"' + path + '.zip\":{\"romName\":\"' + name + '\"},')

	#f.write ( 'game (\n' )
	#f.write ( '\tname ' + path + '\n')
	#f.write ( '\tdescription \"' + name + '\"\n' )
	#if releasedate != "":	f.write ( '\tyear ' +  releasedate + '\n')
	#f.write ( '\tmanufacturer \"' + developer + '\"\n' )
	#f.write ( ')\n\n' ) 

f.write ('}}\n')
f.close()
