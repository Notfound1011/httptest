#coding=utf-8
import sys
import unittest
from common import commonAw
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
from common import configDB
from apiparam.GothamApiParam import common, companyList

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()

class BusUserlogin(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)        
        '''初始化参数'''
        self.case_name=companyList.case_name
        self.headers=common.headers
        self.token = ''
        self.result = ''
        self.data = ''
        self.response = None
        self.info = None
        
        '''接口预期返回的参数'''
        #携带token查询companylist
        self.status_code1 = 200
        self.errorno1 = '0000'
        self.msg1=""
        #不携带token查询companylist
        self.status_code2 = 500
        self.errorno2 = 'Internal Server Error'
        self.msg2="token为空"

    def setUp(self):
        """
        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        '''登陆获取token'''
        # set url
        self.url = commonAw.get_url_from_xml('companylist')
        localConfigHttp.set_url(self.url)
        # set header
        localConfigHttp.set_headers(self.headers)
        
        
    def testCompanyListWithtoken(self):
        """
        the 1st testcase
        携带token查询--->公司列表
        :return:
        """
        # set body 
        localConfigHttp.set_data(companyList.body1)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code1)
        self.assertEqual(self.info['code'], self.errorno1)
        self.assertEqual(self.info['msg'], self.msg1)
        
        #write_log
        self.log.build_case_code(sys._getframe().f_code.co_name, str(self.status_code1))
        self.log.build_case_response(self.response.text)
        
    def testLoginWithAccountNotExist(self):
        """
        the 2rd testcase
        不携带token查询--->公司列表
        :return:
        """
        # set body 
        localConfigHttp.set_data(companyList.body2)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code2)
        self.assertEqual(self.info['error'], self.errorno2)
        self.assertEqual(self.info['message'], self.msg2)
        
        #write_log
        self.log.build_case_code(sys._getframe().f_code.co_name, str(self.status_code2))
        self.log.build_case_response(self.response.text)

    def tearDown(self):
        """

        :return:
        """
