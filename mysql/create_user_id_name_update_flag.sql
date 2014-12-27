create table if not exists lol.user_id_name_update_flag (
	area_id_name varchar(128) not null comment '大区名',
	user_id_name varchar(128) not null comment '用户id名',
	primary key(area_id_name, user_id_name),
	chg_status varchar(128) not null comment '变化状态'
) CHARACTER SET utf8;
