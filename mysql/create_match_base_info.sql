create table if not exists lol.match_base_info (
	match_id bigint(20) default 0 comment '比赛id',
	area_id_name varchar(128) default NULL comment '大区名',
	primary key(match_id, area_id_name),
	match_mode_name varchar(128) default NULL comment '比赛模式',
	match_kill_ratio varchar(128) default NULL comment '击杀比',
	match_money_ratio varchar(128) default NULL comment '金钱比',
	match_alive_time varchar(128) default NULL comment '比赛时长',
	match_end_time varchar(128) default NULL comment '比赛结束时间'
) CHARACTER SET utf8;
