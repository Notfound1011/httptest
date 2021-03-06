# -*- coding:utf-8 -*-
import os
import codecs
import configparser
'''
__FILE__   --->  当前文件的绝对路径
dirname(__file__)  --->  当前文件所在的目录
realpath(__file__)  --->  当前文件的绝对路径 或 相对根目录的路径
''' 
proDir = os.path.dirname(__file__)  #比下一行代码表达好
# proDir = os.path.split(os.path.realpath(__file__))[0]


class ReadConfig(object):
    '''
    读取配置文件内的值
    自带的文件处理功能，加上configparser模块来读取配置文件
    '''
    def __init__(self,configname='config.ini'):
        configPath = os.path.join(proDir,configname)
        fd = open(configPath)
        data = fd.read()
        self.configPath =configPath
        #  remove BOM
        '''
            为什么要下面这一段呢？？
    某些软件，如notepad，在保存一个以UTF-8编码的文件时，会在文件开始的地方插入三个不可见的字符
   （0xEF 0xBB 0xBF，即BOM）。因此我们在读取时需要自己去掉这些字符，python中的codecs module定义了这个常量：
        '''
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
    
    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(self.configPath, 'w+') as f:
            self.cf.write(f)

    def set_http(self, name, value):
        self.cf.set("HTTP", name, value)
        with open(self.configPath, 'w+') as f:
            self.cf.write(f)
            
    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value