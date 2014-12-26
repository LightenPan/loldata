# -*- coding=utf-8 -*-

def get_user_zdl(area_id_name, user_id_name):
	import urllib2
	utf8_user_id_name = urllib2.quote(user_id_name.encode('utf8'))
	query_url = r'http://lolbox.duowan.com/ajaxPlayerInfo.php?callback=jQuery16202311935480684042_1419262146302&playerName=%s&serverName=%s' % (utf8_user_id_name, area_id_name)
	print query_url

	opener = urllib2.build_opener()
	conn = opener.open(query_url)
	content = unicode(conn.read(), "utf-8")
	dict_zdl = eval(content.split('(')[1].split(')')[0])

	return dict_zdl['lolcombat']

def get_match_detail(area_id_name, match_id, user_id_name):
	from pyquery import PyQuery as pyq
	import json
	import urllib2

	referer_url = u'http://lolbox.duowan.com/matchList.php?serverName=%s&playerName=%s&page=0' % (area_id_name, user_id_name)
	print referer_url

	query_url = u'http://lolbox.duowan.com/ajaxMatchDetail.php?matchId=%s&queueType=NORMAL&serverName=%s&playerName=%s' % (match_id, area_id_name, user_id_name)
	print query_url

	opener = urllib2.build_opener()
	opener.addheaders = [('X-Requested-With:', 'XMLHttpRequest')]
	opener.addheaders = [('Referer', referer_url)]
	conn = opener.open(query_url)

	content = unicode(conn.read(), "utf-8")
	#content = conn.read()

	doc=pyq(content)

	#print doc

	match_persion_list = []
	persion_cts = doc('.tips-a')
	for i in persion_cts.find('.mod-tips-content'):
		#print pyq(i)

		user_id_name = pyq(i).find('.player-name').text()

		user_profile = {}
		user_profile['user_id_name'] = user_id_name
		user_profile['area_id_name'] = area_id_name
		user_profile['zdl'] = get_user_zdl(area_id_name, user_id_name)
		match_persion_list.append(user_profile)

		# print user_profile

	user_count = len(match_persion_list)
	# print user_count

	win_zdl = 0
	lose_zdl = 0
	for i in range(0, user_count):
		user_profile = match_persion_list[i]
		if (i < user_count/2):
			win_zdl = win_zdl + int(user_profile['zdl'])
		else:
			lose_zdl = lose_zdl + int(user_profile['zdl'])

	# print win_zdl, lose_zdl

	#输出csv文件
	import csv

	writer = csv.writer(file('zdl.csv', 'a'))
	#写入csv头
	# fieldnames = list(match_persion_list[0].keys())
	# print json.dumps(fieldnames, encoding="UTF-8", ensure_ascii=False)
	# writer.writerow([unicode(s).encode("utf-8") for s in fieldnames])
	for item in match_persion_list:
		# print json.dumps(item.values(), encoding="utf-8", ensure_ascii=false)
	    writer.writerow([unicode(s).encode("utf-8") for s in item.values()])
	writer.writerow([win_zdl, lose_zdl])



def main():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--area_id_name", dest="area_id_name", help=u"lol大区名")
	parser.add_argument("--match_id", dest="match_id", help=u"lol比赛id")
	parser.add_argument("--user_id_name", dest="user_id_name", help=u"lol游戏角色名")
	args = parser.parse_args()
	# print args

	# get_match_detail(u'%E7%94%B5%E4%BF%A1%E4%B8%80', 10525178168, u'%E6%A5%BC%E5%85%B0%E7%A0%B4')

	options = vars(args)
	for i in options:
		if (None == options[i]):
			parser.error("plase input " + i)

	from urllib import quote
	area_id_name = quote(options['area_id_name'])
	match_id = quote(options['match_id'])
	user_id_name = quote(options['user_id_name'])
	get_match_detail(area_id_name, match_id, user_id_name)

if __name__ == "__main__":
	main()
