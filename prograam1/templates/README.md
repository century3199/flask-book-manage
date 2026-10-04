# Flask 图书管理系统
简易网页版图书管理demo，使用 Python Flask + MySQL 实现。
支持图书新增、查看列表、删除图书功能，解决MySQL中文存储乱码问题，数据库采用utf8mb4字符集。

## 技术栈
- Python 3
- Flask：Web框架
- pymysql：MySQL数据库连接
- HTML 简单前端页面

## 项目结构
├── app.py          # 主程序
├── templates/      # html 网页模板文件夹
└── README.md       # 项目说明

## 环境准备
1. 安装依赖包
```bash
pip install flask pymysql

2.MySQL 数据库准备
运行下面 SQL 创建数据库和数据表：
DROP DATABASE IF EXISTS book_manage;
CREATE DATABASE book_manage 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE book_manage;
CREATE TABLE book(
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL
);

3.修改数据库配置
打开 app.py，修改 mysql 账号密码：

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="你的mysql密码",
    database="book_manage",
    charset="utf8mb4"
)
