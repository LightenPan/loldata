create table if not exists lol.match_ex_info (
	match_id bigint(20) default 0 comment '比赛id',
	area_id_name varchar(128) default NULL comment '大区名',
	user_id_name varchar(128) default NULL comment '用户id名',
	primary key(match_id, area_id_name, user_id_name),
	kill_num integer(11) default 0 comment '杀敌数',
	dead_num integer(11) default 0 comment '死亡数',
	assist_num integer(11) default 0 comment '助攻数',
	money integer(11) default 0 comment '金钱',
	last_hit integer default 0 comment '补兵',
	topping_towers integer(11) default 0 comment '推塔',
	place_wards integer(11) default 0 comment '放眼数',
	exclude_wards integer(11) default 0 comment '排眼数',
	kill_our_creeps integer(11) default 0 comment '杀我方野怪',
	kill_the_creeps integer(11) default 0 comment '杀敌方野怪',
	most_of_the_killing integer(11) default 0 comment '最大多杀',
	the_largest_crit integer(11) default 0 comment '最大暴击',
	the_daian_kill integer(11) default 0 comment '最大连杀',
	dps integer(11) default 0 comment '输出伤害',
	control_enemy_time varchar(128) default NULL comment '控制敌方',
	camp integer(11) default 0 comment '兵营',
	total_treatment integer(11) default 0 comment '总治疗',
	tankiness integer(11) default 0 comment '承受伤害',
	dps_on_other_heros integer(11) default 0 comment '给对方英雄造成总伤害',
	ad_on_other_heros integer(11) default 0 comment '给对方英雄的物理伤害',
	ap_on_other_heros integer(11) default 0 comment '给对方英雄的魔法伤害',
	td_on_other_heros integer(11) default 0 comment '给对方英雄的真实伤害',
	hero_name varchar(128) default NULL comment '英雄名',
	win_or_lose integer(11) default 0 comment '比赛输赢'
) CHARACTER SET utf8;
