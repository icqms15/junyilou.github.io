# -*- coding:utf-8 -*-
import os, sys, urllib2, datetime, json, time
def filesize(url):
	opener = urllib2.build_opener()
	request = urllib2.Request(url)
	request.get_method = lambda: 'HEAD'
	try: response = opener.open(request); response.read()
	except Exception, e: return 0
	else: return int(dict(response.headers).get('content-length', 0))
def down(rtl):
	spr = "R" + rtl + ".png"; sx = sbn + rtl + ".png"
	exi = os.path.isfile(sx); newsize = filesize(dieter + "/16_9/" + spr)
	nameopen = open("/home/pi/Retail/name.md"); storejson = json.loads(nameopen.read()); nameopen.close()
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 1:
		reload(sys); sys.setdefaultencoding('utf-8')
		pushRaw = "零售店图册 - Apple " + storejson[0][rtl] + " 刚刚获得了更新，店号 R" + rtl + "，图片大小 " + str(newsize / 1024) + " KB，访问 Apple 官网了解更多。"
		if exi: os.system("mv -n " + sbn + rtl + ".png " + rpath.replace("Pictures/", "") + "Other/previous/"); exi = False
		if not exi: os.system("wget -t 2 -c -P " + rpath + " " + dieter + "/16_9/" + spr)
		os.system('curl -X POST -H "Content-Type: application/json" -d' + "'" + '{"value1":"' + pushRaw + '"}'
			   + "' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x"); print
		os.system('curl -X POST -H "Content-Type: application/json" -d' + "'" + '{"value1":"' + pushRaw + '"}' 
			   + "' https://maker.ifttt.com/trigger/raw/with/key/bOGI8iEAyvjh782UYFKbRa"); print
		# GitHub users please notice: IFTTT key only uses for private.
	else: print "Checked R" + rtl +" has no update, ignore."
rpath = "/home/pi/Retail/Pictures/"; sbn = rpath + "R"
dieter = "https://rtlimages.apple.com/cmc/dieter/store"
sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
while True:
	os.system("clear")
	for j in range(90, 706): down("%03d" % j)
	print "Sleeping, interval will be 1 hr."; time.sleep(3600)
print "\nStarted: " + sTime + "\nEnded:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())