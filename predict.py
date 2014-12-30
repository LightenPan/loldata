# -*- coding=utf-8 -*-

import mysql_helper


def num_table_index(match_id):
	return int(match_id)%100


def name_table_index(val):
	import binascii
	num = binascii.crc32(val) & 0xffffffff
	return (num%100)


def get_kda(area_id_name, user_id_name, limit_num):
	db = mysql_helper.MySQL('127.0.0.1', 'root', '111111', 3306)
	db.selectDb('lol')
	query_sql = "select * from match_ex_info_%s where area_id_name = '%s' and user_id_name = '%s' limit %s" % (name_table_index(user_id_name), area_id_name, user_id_name, limit_num)
	db.query(query_sql)

	rows = db.fetchAll()
	# print rows

	if len(rows) < int(limit_num):
		print "not enough limit num, len: %s, limit_num: %s" % (len(rows), limit_num)
		return


	kda = 0.0
	for row in rows:
		kill_num = int(row['kill_num'])
		dead_num = int(row['dead_num'])
		assist_num = int(row['assist_num'])

		if dead_num == 0:
			dead_num = 1

		kda = kda + (kill_num + assist_num)/dead_num

	if len(rows) > 0:
		kda = kda/len(rows)

	return kda


def get_money(area_id_name, user_id_name, limit_num):
	db = mysql_helper.MySQL('127.0.0.1', 'root', '111111', 3306)
	db.selectDb('lol')
	query_sql = "select * from match_ex_info_%s where area_id_name = '%s' and user_id_name = '%s' limit %s" % (name_table_index(user_id_name), area_id_name, user_id_name, limit_num)
	db.query(query_sql)

	rows = db.fetchAll()

	if len(rows) < int(limit_num):
		print "not enough limit num, len: %s, limit_num: %s" % (len(rows), limit_num)
		return

	money = 0
	for row in rows:
		money = money + int(row['money'])

	if len(rows) > 0:
		money = money/len(rows)
	return money


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

def get_match_detail(match_id, limit_num):
	db = mysql_helper.MySQL('127.0.0.1', 'root', '111111', 3306)
	db.selectDb('lol')
	query_sql = "select * from match_ex_info_%s where match_id = %s" % (num_table_index(match_id), match_id)
	db.query(query_sql)

	rows = db.fetchAll()
	# print rows

	win_kda = 0.0
	lose_kda = 0.0
	win_money = 0
	lose_money = 0
	for item in rows:
		item['avg_kda'] = get_kda(item['area_id_name'], item['user_id_name'], limit_num)
		item['avg_money'] = get_money(item['area_id_name'], item['user_id_name'], limit_num)

		if item['win_or_lose'] == '1':
			win_kda = win_kda + item['avg_kda']
			win_money = win_money + item['avg_money']
		else:
			lose_kda = lose_kda + item['avg_kda']
			lose_money = lose_money + item['avg_money']

	first_item = rows[0]
	if first_item['win_or_lose'] == '1':
		if win_kda > lose_kda:
			first_item['predict_ret_by_kda'] = 1
		else:
			first_item['predict_ret_by_kda'] = 0

		if win_money > lose_money:
			first_item['predict_ret_by_money'] = 1
		else:
			first_item['predict_ret_by_money'] = 0

	else:
		if win_kda > lose_kda:
			first_item['predict_ret_by_kda'] = 0
		else:
			first_item['predict_ret_by_kda'] = 1

		if win_money > lose_money:
			first_item['predict_ret_by_money'] = 0
		else:
			first_item['predict_ret_by_money'] = 1

	return [first_item['match_id'], first_item['avg_kda'], first_item['avg_money'], first_item['win_or_lose'], first_item['predict_ret_by_kda'], first_item['predict_ret_by_money']]


def get_match_id_list(table_index, total_count):
	db = mysql_helper.MySQL('127.0.0.1', 'root', '111111', 3306)
	db.selectDb('lol')
	query_sql = "select distinct(match_id) from match_ex_info_%s limit %s" % (table_index, total_count)
	print query_sql

	db.query(query_sql)
	rows = db.fetchAll()
	return rows


def main():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--total_count", dest="total_count", help=u"总记录数")
	parser.add_argument("--limit_num", dest="limit_num", help=u"单人历史场数")
	parser.add_argument("--table_index", dest="table_index", help=u"数据库下标")
	args = parser.parse_args()
	# print args

	options = vars(args)
	for i in options:
		if (None == options[i]):
			parser.error("plase input " + i)

	#写入csv头
	import csv
	writer = csv.writer(file('predict_ret.csv', 'a'))
	headers = ['赛事id', '平均kda', '平均金钱', '输赢', 'kda预测', '金钱预测']
	writer.writerow(headers)

	rows = get_match_id_list(options['table_index'], options['total_count'])
	for item in rows:
		match_id = item['match_id']
		limit_num = options['limit_num']
		val_list = get_match_detail(match_id, limit_num)

		if None == val_list:
			continue

		writer.writerow(val_list)


if __name__ == "__main__":
	main()
