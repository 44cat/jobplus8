# jobplus8
LouPlus Team 8 https://www.shiyanlou.com/louplus/python

# 招聘网站项目

## Contributors

* [louplus](https://github.com/louplus)
* [晓风灿月](https://github.com/chencancool)
* [猫猫猫](https://github.com/44cat)
* [liyangworld](https://github.com/liyangworld)
* [lucyzzz](https://github.com/lucyzzz)

## 开发环境准备
0.克隆后进入jobplus8主目录下
```
git clone https://www.shiyanlou.com/LouPlus/jobplus8.git
```

1.进入jobplus8主目录后,添加并修改/etc/mysql/my.cnf(添加在对应底部即可),将mysql编码设置为utf8:
$ sudo vim /etc/mysql/my.cnf
```
[client]
default-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8
```
2.启动并进入MySQL数据库
```
$ sudo service mysql start
$ mysql -uroot
```
3.创建jobplus8数据库待用
```
mysql>create database jobplus8;
```
4.安装项目依赖软件包

$ sudo pip3 install -r requirements.txt

5.设置项目应用环境变量,并处于调试模式
```
$ export FLASK_APP=manage.py
$ export FLASK_DEBUG=1
```
6.使用 flask-migrate 初始化数据库
```
$ flask db init
$ flask db migrate -m "init database"
数据库数据更新：$ flask db upgrade
```
7.启动应用，并打开链接即可

$ flask run
