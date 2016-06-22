#! /usr/bin/python
#-*- coding:utf-8 -*-

import datetime
import time
"""
时间格式化参数：
    %a 星期几的简写
    %A 星期几的全称
    %b 月分的简写
    %B 月份的全称
    %c 标准的日期的时间串
    %C 年份的后两位数字
    %d 十进制表示的每月的第几天
    %D 月/天/年
    %e 在两字符域中，十进制表示的每月的第几天
    %F 年-月-日
    %g 年份的后两位数字，使用基于周的年
    %G 年分，使用基于周的年
    %h 简写的月份名
    %H 24小时制的小时
    %I 12小时制的小时
    %j 十进制表示的每年的第几天
    %m 十进制表示的月份
    %M 十时制表示的分钟数
    %n 新行符
    %p 本地的AM或PM的等价显示
    %r 12小时的时间t
    %R 显示小时和分钟：hh:mm
    %S 十进制的秒数
    %t 水平制表符
    %T 显示时分秒：hh:mm:ss
    %u 每周的第几天，星期一为第一天 （值从0到6，星期一为0）
    %U 第年的第几周，把星期日做为第一天（值从0到53）
    %V 每年的第几周，使用基于周的年
    %w 十进制表示的星期几（值从0到6，星期天为0）
    %W 每年的第几周，把星期一做为第一天（值从0到53）
    %x 标准的日期串
    %X 标准的时间串
    %y 不带世纪的十进制年份（值从0到99）
    %Y 带世纪部分的十制年份
    %z，%Z 时区名称，如果不能得到时区名称则返回空字符。
    %% 百分号
"""
#获取日期
def get_date(num=0):
    today =  datetime.date.today()
    date = today - datetime.timedelta(days=num)                         #2016-04-22格式时间日期
    return date

#获取当前时间戳
def get_timestamp(time_format):
    #timestamp =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    timestamp = time.strftime(time_format)                              #2016-04-22 13:53:02格式时间
    return timestamp

#获取13位数字格式时间
def get_13_seconds():
    seconds = int(time.time())*1000
    return seconds

#获取10位数字格式时间
def get_10_seconds():
    seconds = int(time.time())
    return seconds

#数字格式转化为时间格式
def number2time(seconds,time_format):
    struct_time = time.localtime(seconds)                           #把数字转化为本地时间格式
    format_time =  time.strftime(time_format,struct_time)           #本地时间格式转化为时间格式
    return format_time


#时间格式转化为数字格式
def time2number(str_time,time_format):
    struct_time =  time.strptime(str_time,time_format,)
    seconds = int(time.mktime(struct_time))                         #10位数的秒格式
    #seconds = int(time.mktime(struct_time))*1000                    #13位数的秒格式
    return seconds

#转换格式
def convert_format(str_time,current_format ,target_format):
    struct_time =  time.strptime(str_time,current_format)           #把当前格式转化为元组格式
    result_time = time.strftime(target_format,struct_time)          #把元组格式转化为目标格式
    return result_time



if __name__ == '__main__':
     # get_date()
     # get_timestamp('%Y-%m-%d %H:%M:%S')
     # get_13_seconds()
     # get_10_seconds()
     number2time(int(str(1465651800000)[0:-3]),'%Y-%m-%d %H:%M:%S')
     # time2number("2016-04-20",'%Y-%m-%d')
     # convert_format("2016.04.05",'%Y.%m.%d','%Y-%m-%d')