# -*- coding=utf-8 -*-

import urllib

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


	#获取比赛信息
	match_profile = {}
	match_profile["match_id"] = match_id

	#获取基本信息
	win_match = doc.find('tr.c333:first')

	win_match_list = win_match.text().split(' ')
	match_profile["match_mode_name"] = win_match_list[1]
	match_profile["match_alive_time"] = win_match_list[2]
	match_profile["match_end_time"] = win_match_list[3]

	lose_match = doc.find('tr.c333:last')
	lose_match_list = lose_match.text().replace(u'：', ' ').split(' ')
	match_profile["match_kill_ratio"] = lose_match_list[2]
	match_profile["match_money_ratio"] = lose_match_list[4]
	# print match_profile


	#获取每个人的信息
	profile_dict = {
			u"比赛id":"match_id",
			u"大区名":"area_id_name",
			u"用户id名":"user_id_name",
			u"英雄名":"hero_name",
			u"比赛输赢":"win_or_lose",
			u"杀敌":"kill_num",
			u"死亡":"dead_num",
			u"助攻":"assist_num",
			u"补兵":"last_hit",
			u"推塔":"topping_towers",
			u"金钱":"money",
			u"控制敌方":"control_enemy_time",
			u"最大连杀":"the_daian_kill",
			u"最大多杀":"most_of_the_killing",
			u"最大暴击":"the_largest_crit",
			u"兵营":"camp",
			u"总治疗":"total_treatment",
			u"杀我方野怪":"kill_our_creeps",
			u"杀敌方野怪":"kill_the_creeps",
			u"放眼数":"place_wards",
			u"排眼数":"exclude_wards",
			u"输出伤害":"dps",
			u"承受伤害":"tankiness",
			u"给对方英雄造成总伤害":"dps_on_other_heros",
			u"给对方英雄的物理伤害":"ad_on_other_heros",
			u"给对方英雄的魔法伤害":"ap_on_other_heros",
			u"给对方英雄的真实伤害":"td_on_other_heros"
			}

	match_persion_list = []
	persion_cts = doc('.tips-a')
	for i in persion_cts.find('.mod-tips-content'):
		#print pyq(i)

		user_id_name = pyq(i).find('.player-name').text()

		liDetail = pyq(i).find('li').text()
		#print liDetail

		#单个人的属性
		persion_profile = {}
		person_detail = liDetail.split(' ')
		for item in person_detail:
			key_val = item.split(u'：')
			#print ''.join(key_val)
			key = key_val[0]
			val = key_val[1]

			#print user_id_name, key, val, profile_dict[key]
			persion_profile[ profile_dict[key] ] = urllib.unquote(val)

		#向列表添加item
		persion_profile["user_id_name"] = user_id_name
		persion_profile["match_id"] = match_id
		# print json.dumps(persion_profile, encoding="UTF-8", ensure_ascii=False)
		match_persion_list.append(persion_profile)

	total_user_count = len(match_persion_list)
	persion_index = 0
	for item in match_persion_list:
		if (persion_index < total_user_count/2):
			item["win_or_lose"] = 1
		else:
			item["win_or_lose"] = 0
		persion_index = persion_index + 1

	#print user_profile_list
	# print json.dumps(match_persion_list, encoding="UTF-8", ensure_ascii=False)

	#输出mysql
	import MySQLdb

	# 打开数据库连接
	db = MySQLdb.connect(host="localhost", user="root", passwd="111111", db="lol", charset="utf8")
	cursor = db.cursor()

    #写入比赛流水信息
	for item in match_persion_list:
		placeholders = ', '.join(['%s'] * len(item))
		columns = ', '.join(item.keys())

		sql = "INSERT into %s ( %s ) VALUES ( %s )" % ('match_ex_info', columns, placeholders)
		# print sql

		try:
			# 执行sql语句
			cursor.execute(sql, item.values())
			# 提交到数据库执行
			db.commit()
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			# Rollback in case there is any error
			db.rollback()

	#写入比赛基本信息
	placeholders = ', '.join(['%s'] * len(match_profile))
	columns = ', '.join(match_profile.keys())
	sql = "INSERT into %s ( %s ) VALUES ( %s )" % ('match_base_info', columns, placeholders)
	print sql

	try:
		# 执行sql语句
		# cursor.execute(sql, [i.decode('utf-8') for i in match_profile.values()])
		cursor.execute(sql, match_profile.values())
		# 提交到数据库执行
		db.commit()
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		# Rollback in case there is any error
		db.rollback()

	# 关闭数据库连接
	db.close()

	# #输出csv文件
	# import csv

	# #输出比赛详细信息
	# writer = csv.writer(file('match_ex_info.csv', 'a'))
	# #写入csv头
	# # fieldnames = list(match_persion_list[0].keys())
	# # print json.dumps(fieldnames, encoding="UTF-8", ensure_ascii=False)
	# # writer.writerow([unicode(s).encode("utf-8") for s in fieldnames])
	# for item in match_persion_list:
		# # print json.dumps(item.values(), encoding="UTF-8", ensure_ascii=False)
		# writer.writerow([unicode(s).encode("utf-8") for s in item.keys()])
		# writer.writerow([unicode(s).encode("utf-8") for s in item.values()])

	# #输出比赛基本信息
	# writer = csv.writer(file('match_base_info.csv', 'a'))
	# writer.writerow([unicode(s).encode("utf-8") for s in match_profile.keys()])
	# writer.writerow([unicode(s).encode("utf-8") for s in match_profile.values()])

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
	match_id = quote(options['match_id'].strip())
	user_id_name = quote(options['user_id_name'])
	# print area_id_name, match_id, user_id_name
	get_match_detail(area_id_name, match_id, user_id_name)

if __name__ == "__main__":
	main()
