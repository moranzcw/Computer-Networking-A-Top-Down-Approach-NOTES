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

# def getMusicUrl(albumNum,musicNum):
#     musicUrl = 'http://luoo.800edu.net/low/luoo/radio' + '%d/%02d.mp3' % (albumNum,musicNum)
#     return musicUrl

# def regexFindAll(regex,html):
#     pattern = re.compile(regex)
#     result = pattern.findall(html)
#     return result

# def downloadAlbum(path,albumNum):
#     html = getPageHtml (albumNum)
    
#     regex = '(?<=<span class=\"vol-title\">).+(?=</span>)'
#     albumTitle = regexFindAll(regex,html)
#     newPath = os.path.join(path,'Vol.' + str(albumNum) + ' ' + albumTitle[0])
#     if not os.path.isdir(newPath):
#         os.makedirs(newPath)

#     print u'正在下载: Vol.%d %s' % (albumNum,albumTitle[0])

#     regex = 'http://img2\.luoo\.net/pics/vol/.*(?=\" alt=\"%s\" class=\"vol-cover)' % albumTitle[0]
#     imgUrl = regexFindAll(regex,html)
#     imgPath = os.path.join(newPath, albumTitle[0] + '.jpg')
#     urllib.urlretrieve(imgUrl[0],imgPath)

#     regex = '(?<=<p class=\"name\">).*(?=</p>)'
#     musicName = regexFindAll(regex,html)

#     for each in range(len(musicName)):
#         print u'    正在下载 ' + musicName[each].decode('gbk', 'ignore') + u'.mp3 ...' 
#         mp3Path = os.path.join(newPath, '%s.mp3' % musicName[each])
#         musicUrl = getMusicUrl(albumNum,each+1)
#         urllib.urlretrieve(musicUrl, mp3Path)
#         print u'    已完成'
#         time.sleep(0.5)

#     print u'    \nVol.%d %s 下载完成.\n' % (albumNum,albumTitle[0])


# lastAlbum = updateInfo()
# downloadPath = getDownloadPath()
# A,B = getDownloadRange(1,lastAlbum)
# for each in range(A,B+1):
#     downloadAlbum(downloadPath,each)


# visitedListFile = open('visited list.txt','a+')
# unvisitedListFile = open('unvisited list.txt','a+')



# https://api.douban.com/v2/movie/10463953

def getPageHtml (movieNum):
    pageUrl = 'https://api.douban.com/v2/movie/' + movieNum
    html = urllib2.urlopen(pageUrl).read()
    return html.decode('utf-8')

def updateVisiteList(visitedList,movieNum):
    if len(visitedList)/2 < 1:
        if movieNum <= visitedList[len(visitedList)/2]:
            visitedList.insert(len(visitedList)/2,movieNum);
        if movieNum == visitedList[len(visitedList)/2]:
            return;
        if movieNum >= visitedList[len(visitedList)/2]:
            visitedList.insert(len(visitedList)/2+1,movieNum);
        

visitedList = []
unvisitedList = ['10463953']



