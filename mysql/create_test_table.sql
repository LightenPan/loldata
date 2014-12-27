create table if not exists lol.test_table(
	id bigint(20) not null auto_increment comment 'id',
	area_id_name varchar(128) default NULL comment '大区名',
	user_id_name varchar(128) default NULL comment '用户id名',
	primary key(id, area_id_name, user_id_name),
	chg_num integer(11) default 0 comment '变化次数',
	lock_status integer(11) default 0 comment '锁定状态'
) CHARACTER SET utf8;
