# encoding: utf-8
import urllib2
import urllib
import re
import os
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')  

#pageUrl = 'http://www.luoo.net/music/'
#musicUrl = 'http://luoo.800edu.net/low/luoo/radio'
#path = '/home/moran/luoo/'

def updateInfo():
	print u'更新信息 ...'
	html = urllib2.urlopen('http://www.luoo.net/music').read().decode('utf-8')
	
	regex = '(?<=http://www\.luoo\.net/music/)\d+(?=\" class=\"name\")'
	lastAlbum = re.search(regex,html)

	regex = '(?<=class=\"name\"\stitle=\").*(?=\")'
	lastAlbumName = re.search(regex,html)

	print u'最新音乐期刊：Vol.%s %s' % (lastAlbum.group(),lastAlbumName.group())
	print u'完成.\n'
	return int(lastAlbum.group())

def getDownloadPath():
	print u'输入下载路径(如: D:\音乐):'
	downloadPath = raw_input()
	print ''
	while not os.path.isdir(downloadPath):
		print u'路径无效，再次输入路径:'
		downloadPath = raw_input()
	return os.path.join(downloadPath,'luoo')

def getDownloadRange(Min,Max):
	print u'输入将要下载的音乐期刊 : \
				\n如:输入 654 即下载654号音乐期刊\
				\n   输入 101-200 即下载第101至200号音乐期刊\n'
	while True:
		string = raw_input()
		#regex = '^\s*\d{1,3}-\d{1,3}\s*$|^\s*\d{1,3}\s*$'
		regex = '(?<=^)\d{1,3}(?=-)|(?<=-)\d{1,3}(?=$)|(?<=^)\d{1,3}(?=$)'
		result = re.findall(regex,string)
		
		if result != None:
			if len(result) == 2:
				A = int(result[0])
				B = int(result[1])
				if Min<=A<=B<=Max:
					return A,B
			elif len(result) == 1:
				A = int(result[0])
				B = A
				if Min<=A<=Max:
					return A,B
		else:
			print u'无效，再次输入 : '


def getPageHtml (albumNum):
	pageUrl = 'http://www.luoo.net/music/' + '%03d' % albumNum
	html = urllib2.urlopen(pageUrl).read()
	return html.decode('utf-8')

def getMusicUrl(albumNum,musicNum):
	musicUrl = 'http://luoo.800edu.net/low/luoo/radio' + '%d/%02d.mp3' % (albumNum,musicNum)
	return musicUrl

def regexFindAll(regex,html):
	pattern = re.compile(regex)
	result = pattern.findall(html)
	return result

def downloadAlbum(path,albumNum):
	html = getPageHtml (albumNum)
	
	regex = '(?<=<span class=\"vol-title\">).+(?=</span>)'
	albumTitle = regexFindAll(regex,html)
	newPath = os.path.join(path,'Vol.' + str(albumNum) + ' ' + albumTitle[0])
	if not os.path.isdir(newPath):
		os.makedirs(newPath)

	print u'正在下载: Vol.%d %s' % (albumNum,albumTitle[0])

	regex = 'http://img2\.luoo\.net/pics/vol/.*(?=\" alt=\"%s\" class=\"vol-cover)' % albumTitle[0]
	imgUrl = regexFindAll(regex,html)
	imgPath = os.path.join(newPath, albumTitle[0] + '.jpg')
	urllib.urlretrieve(imgUrl[0],imgPath)

	regex = '(?<=<p class=\"name\">).*(?=</p>)'
	musicName = regexFindAll(regex,html)

	for each in range(len(musicName)):
		print u'	正在下载 ' + musicName[each].decode('gbk', 'ignore') + u'.mp3 ...' 
		mp3Path = os.path.join(newPath, '%s.mp3' % musicName[each])
		musicUrl = getMusicUrl(albumNum,each+1)
		urllib.urlretrieve(musicUrl, mp3Path)
		print u'	已完成'
		time.sleep(0.5)

	print u'	\nVol.%d %s 下载完成.\n' % (albumNum,albumTitle[0])


lastAlbum = updateInfo()
downloadPath = getDownloadPath()
A,B = getDownloadRange(1,lastAlbum)
for each in range(A,B+1):
	downloadAlbum(downloadPath,each)
