create table if not exists lol.user_match_list_info (
	match_id bigint(20) default 0 comment '比赛id',
	area_id_name varchar(128) default NULL comment '大区名',
	user_id_name varchar(128) default NULL comment '用户id名',
	primary key(match_id, area_id_name, user_id_name),
	match_mode varchar(128) default NULL comment '比赛模式',
	match_mode_name varchar(128) default NULL comment '比赛模式名',
	hero_name varchar(128) default NULL comment '英雄名',
	result_name varchar(128) default NULL comment '比赛结果名',
	match_date varchar(128) default NULL comment '比赛日期'
) CHARACTER SET utf8;
