create table if not exists lol.user_id_name_update_flag (
	area_id_name varchar(128) default NULL comment '大区名',
	user_id_name varchar(128) default NULL comment '用户id名',
	primary key(area_id_name, user_id_name),
	chg_num integer(11) default 0 comment '变化次数'
) CHARACTER SET utf8;
