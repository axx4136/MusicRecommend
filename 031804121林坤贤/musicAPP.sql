drop database if exists musicAPP;
create database musicAPP;
use musicAPP;
create table msg(
	mid varchar(32) primary key,   -- 歌曲号
	mname varchar(20) NOT NULL,    -- 歌名
    singer varchar(20) NOT NULL,   -- 歌手
	mtype varchar(20) NOT NULL,    -- 歌曲风格类型
	mpath varchar(100) NOT NULL    -- 文件路径
);