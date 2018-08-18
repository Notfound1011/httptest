#coding=utf-8
import sys
import unittest
from common import commonAw
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
from common import configDB
from apiparam.GothamApiParam import common, gameList

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()

class GameList(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)        
        '''初始化参数'''
        self.case_name=gameList.case_name
        self.headers=common.headers
        self.token = ''
        self.result = ''
        self.data = ''
        self.response = None
        self.info = None
        
        '''接口预期返回的参数'''
        #携带token，查询全部游戏
        self.status_code1 = 200
        self.errorcode1 = '0000'
        self.msg1=""
        #不携带token查询companylist
        self.status_code2 = 500
        self.errorcode2 = 'Internal Server Error'
        self.msg2="token为空"
        #查询单个游戏
        self.status_code3 = 200
        self.errorcode3 = '0000'
        self.msg3=""
        self.recordsTota3=1
        self.keyword=gameList.keyword
    def setUp(self):
        """
        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        '''登陆获取token'''
        # set url
        self.url = commonAw.get_url_from_xml('gamelist')
        localConfigHttp.set_url(self.url)
        # set header
        localConfigHttp.set_headers(self.headers)
        
        
    def testGameListWithToken(self):
        """
        the 1st testcase
        携带token查询---> 全部游戏列表
        :return:
        """
        # set body 
        self.body=gameList.body1
        localConfigHttp.set_data(self.body)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
#         commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code1)
        self.assertEqual(self.info['code'], self.errorcode1)
        self.assertEqual(self.info['msg'], self.msg1)
        self.assertEqual(len(self.info['data']), 15)
        #write_log
        self.log.build_case_body(sys._getframe().f_code.co_name,self.body)
        self.log.build_case_code(str(self.status_code1))
        self.log.build_case_response(self.response.text)
        
    def testGameListWithoutToken(self):
        """
        the 2nd testcase
        不携带token查询--->游戏列表
        :return:
        """
        # set body 
        self.body=gameList.body2
        localConfigHttp.set_data(self.body)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
#         commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code2)
        self.assertEqual(self.info['error'], self.errorcode2)
        self.assertEqual(self.info['message'], self.msg2)
        
        #write_log
        self.log.build_case_body(sys._getframe().f_code.co_name,self.body)
        self.log.build_case_code(str(self.status_code2))
        self.log.build_case_response(self.response.text)
    def testSearchGameListByOne(self):
        """
        the 3rd testcase
        查询--->单个游戏
        :return:
        """
        # set body 
        self.body=gameList.body3
        localConfigHttp.set_data(self.body)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
#         commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code3)
        self.assertEqual(self.info['code'], self.errorcode3)
        self.assertEqual(self.info['msg'], self.msg3)
        self.assertEqual(self.info['recordsTotal'], self.recordsTota3)
        self.assertEqual(self.info['data'][0]['name'], self.keyword)
        #write_log
        self.log.build_case_body(sys._getframe().f_code.co_name,self.body)
        self.log.build_case_code(str(self.status_code3))
        self.log.build_case_response(self.response.text)


    def tearDown(self):
        """

        :return:
        """
