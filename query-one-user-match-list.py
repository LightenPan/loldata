# -*- coding=utf-8 -*-

def read_and_query():
	#输出mysql
	import MySQLdb
	import MySQLdb.cursors

	# 打开数据库连接
	db = MySQLdb.connect(host="localhost", user="root", passwd="111111", db="lol", charset="utf8", cursorclass = MySQLdb.cursors.DictCursor)
	cursor = db.cursor()

	cursor.execute('select * from user_id_name_update_flag where chg_num = 0 limit 1')
	rs = cursor.fetchall()
	print rs

	if len(rs) < 1:
		return

	row = rs[0]
	print row

	import subprocess
	shell_cmd = 'python user-match-list.py --area_id_name=%s --user_id_name=%s' % (row['area_id_name'], row['user_id_name'])
	print shell_cmd
	subprocess.call(shell_cmd, shell=True)

import argparse
def main():
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
	# print args

	options = vars(args)
	# print options
	for i in options:
		if (None == options[i]):
			parser.error("plase input " + i)

	read_and_query()

if __name__ == "__main__":
	main()
