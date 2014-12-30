# -*- coding=utf-8 -*-

def num_table_index(match_id):
	return int(match_id)%100


def name_table_index(val):
	import binascii
	num = binascii.crc32(val) & 0xffffffff
	return (num%100)


def check_is_finish():
	#输出mysql
	import MySQLdb
	import MySQLdb.cursors

	# 打开数据库连接
	db = MySQLdb.connect(host="localhost", user="root", passwd="111111", db="lol", charset="utf8", cursorclass = MySQLdb.cursors.DictCursor)
	cursor = db.cursor()

	cursor.execute("select * from user_id_name_update_flag where chg_status='0' limit 1")
	rs = cursor.fetchall()
	# print rs

	if len(rs) < 1:
		db.close()
		return True
	else:
		db.close()
		return False


def read_and_query():
	#输出mysql
	import MySQLdb
	import MySQLdb.cursors

	# 打开数据库连接
	db = MySQLdb.connect(host="localhost", user="root", passwd="111111", db="lol", charset="utf8", cursorclass = MySQLdb.cursors.DictCursor)
	cursor = db.cursor()

	import uuid
	chg_status = uuid.uuid1()
	try:
		update_sql = "update user_id_name_update_flag set chg_status='%s' where chg_status='0' limit 1;" % chg_status
		cursor.execute(update_sql)
		db.commit()
	except MySQLdb.Error, e:
		db.rollback()
		db.close()

	select_sql = "select * from user_id_name_update_flag where chg_status='%s';" % chg_status
	cursor.execute(select_sql)
	rs = cursor.fetchall()
	# print rs
	db.close()

	if len(rs) < 1:
		return

	row = rs[0]
	# print row

	import subprocess
	shell_cmd = 'python user-match-list.py --area_id_name=%s --user_id_name=%s --chg_status=%s' % (row['area_id_name'], row['user_id_name'], chg_status)
	# print shell_cmd
	subprocess.call(shell_cmd, shell=True)


def main():
	import argparse
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
	# print args

	options = vars(args)
	# print options
	for i in options:
		if (None == options[i]):
			parser.error("plase input " + i)

	import time
	print time.time()*1000
	while check_is_finish() != True:
		read_and_query()

if __name__ == "__main__":
	main()
