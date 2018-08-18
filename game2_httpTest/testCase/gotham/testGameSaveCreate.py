#coding=utf-8
import sys
import unittest
from common import commonAw
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
from common import configDB
from apiparam.GothamApiParam import common, gameSaveCreate

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()

class gameSaveCreateCreate(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)        
        '''初始化参数'''
        self.case_name=gameSaveCreate.case_name
        self.headers=common.headers
        self.token = ''
        self.result = ''
        self.data = ''
        self.response = None
        self.info = None
        
        '''接口预期返回的参数'''
        #使用英文更新游戏
        self.status_code1 = 200
        self.errorcode1 = '0000'
        self.msg1=""
        self.name1=gameSaveCreate.name1
        self.deliveryUrl1=gameSaveCreate.deliveryUrl1
        #使用中文更新游戏
        self.status_code2 = 200
        self.errorcode2 = '0000'
        self.msg2=""
        self.name2=gameSaveCreate.name2
        self.deliveryUrl2=gameSaveCreate.deliveryUrl2
        #使用空值更新游戏
        self.status_code3 = 200
        self.errorcode3 = '0000'
        self.msg3=""
        self.name3=gameSaveCreate.name3
        self.deliveryUrl3=gameSaveCreate.deliveryUrl3
    def setUp(self):
        """
        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        '''登陆获取token'''
        # set url
        self.url = commonAw.get_url_from_xml('gamesave')
        localConfigHttp.set_url(self.url)
        # set header
        localConfigHttp.set_headers(self.headers)
        
        
    def testgameSaveCreateUpdateUseEn(self):
        """
        the 1st testcase
        使用英文--> 更新游戏
        :return:
        """
        # set body
        self.body=gameSaveCreate.body1
        localConfigHttp.set_data(self.body)
        # post http
        self.response = localConfigHttp.post()
        
        # check result of response
        self.info = self.response.json()
#         commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code1)
        self.assertEqual(self.info['code'], self.errorcode1)
        self.assertEqual(self.info['msg'], self.msg1)
        self.assertEqual(self.info['data']['name'], self.name1)
        self.assertEqual(self.info['data']['deliveryUrl'], self.deliveryUrl1)
        #check datebase
        cursor=localConfigDB.executeSQL('select count(*) from g_game where name="%s"'% self.name1)
        a=localConfigDB.get_one(cursor)
        self.assertEqual(a, 1) 
        cursor=localConfigDB.executeSQL('select * from g_game where name="%s"'% self.name1)
        b=localConfigDB.get_one(cursor)
        self.assertIn(self.deliveryUrl1, b)
        #write_log
        self.log.build_case_body(sys._getframe().f_code.co_name, self.body)
        self.log.build_case_code(str(self.status_code1))
        self.log.build_case_response(self.response.text)
        
    def testgameSaveCreateUpdateUseCn(self):
        """
        the 1st testcase
               使用中文 --> 更新游戏
        :return:
        """
        # set body 
        self.body=gameSaveCreate.body2
        localConfigHttp.set_data(self.body)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
#         commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code2)
        self.assertEqual(self.info['code'], self.errorcode2)
        self.assertEqual(self.info['msg'], self.msg2)
        self.assertEqual(self.info['data']['name'], self.name2)
        self.assertEqual(self.info['data']['deliveryUrl'], self.deliveryUrl2)
        #write_log
        self.log.build_case_body(sys._getframe().f_code.co_name, self.body)
        self.log.build_case_code(str(self.status_code2))
        self.log.build_case_response(self.response.text)

    def testgameSaveCreateUpdateUseNull(self):
        """
        the 1st testcase
               使用空值--> 更新游戏
        :return:
        """
        # set body 
        self.body=gameSaveCreate.body3
        localConfigHttp.set_data(self.body)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
#         commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code3)
        self.assertEqual(self.info['code'], self.errorcode3)
        self.assertEqual(self.info['msg'], self.msg3)
        self.assertEqual(self.info['data']['name'], self.name3)
        self.assertEqual(self.info['data']['deliveryUrl'], self.deliveryUrl3)
        #write_log
        self.log.build_case_body(sys._getframe().f_code.co_name,self.body)
        self.log.build_case_code(str(self.status_code3))
        self.log.build_case_response(self.response.text)

    def tearDown(self):
        """

        :return:
        """
#         localConfigDB.executeSQL('delete from g_game where id =max(id)')
#         localConfigDB.closeDB()