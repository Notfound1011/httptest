#coding=utf-8
import sys
import unittest
from common import commonAw
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
from common import configDB
from apiparam.GothamApiParam import busUserlogin,common

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()

class BusUserlogin(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)        
        '''初始化参数'''
        self.case_name=busUserlogin.case_name
        self.headers=common.headers
        self.token = ''
        self.result = ''
        self.data = ''
        self.response = None
        self.info = None
        
        '''接口预期返回的参数'''
        #账号密码正确
        self.status_code1 = 200
        self.errorno1 = '0000'
        self.msg1=""
        self.loginName="admin"
        #输入不存在账号
        self.status_code2 = 200
        self.errorno2 = '1002'
        self.msg2="账号不存在"
        #输入存在的但是没有权限的账号
        self.status_code3 = 200
        self.errorno3 = '1002' 
        self.msg3="您没有权限登录"
        #输入错误密码
        self.status_code4 = 200
        self.errorno4 = '1004'
        self.msg4="密码错误"

    def setUp(self):
        """
        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        # set url
        self.url = commonAw.get_url_from_xml('busUserlogin')
        localConfigHttp.set_url(self.url)
        
        # set header
        localConfigHttp.set_headers(self.headers)
        
    def testLoginWithRightPasswd(self):
        """
        the 1st testcase
        账号存在，密码正确--->登陆
        :return:
        """
        # set body 
        localConfigHttp.set_data(busUserlogin.body1)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code1)
        self.assertEqual(self.info['code'], self.errorno1)
        self.assertEqual(self.info['msg'], self.msg1)
        self.assertEqual(self.info['data']['loginName'], self.loginName)
        localReadConfig.set_headers('token', self.info['data']['token'])
        #write_log
        self.log.build_case_code(sys._getframe().f_code.co_name, str(self.status_code1))
        self.log.build_case_response(self.response.text)
        
    def testLoginWithAccountNotExist(self):
        """
        the 2rd testcase
        账号不存在--->登陆
        :return:
        """
        # set body 
        localConfigHttp.set_data(busUserlogin.body2)
        # post http
        self.response = localConfigHttp.post()

        # check result of response
        self.info = self.response.json()
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code2)
        self.assertEqual(self.info['code'], self.errorno2)
        self.assertEqual(self.info['msg'], self.msg2)
        
        #write_log
        self.log.build_case_code(sys._getframe().f_code.co_name, str(self.status_code2))
        self.log.build_case_response(self.response.text)
        
    def testLoginWithAccountNoPermission(self):
        """
        the 3rd testcase
        账号存在但没有权限--->登陆
        :return:
        """
        # set body 
        localConfigHttp.set_data(busUserlogin.body3)
        # post http
        self.response = localConfigHttp.post()
        self.info = self.response.json()

        # check result of response
        self.info = self.response.json()
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code3)
        self.assertEqual(self.info['code'], self.errorno3)
        self.assertEqual(self.info['msg'], self.msg3)
        
        #write_log
        self.log.build_case_code(sys._getframe().f_code.co_name, str(self.status_code3))
        self.log.build_case_response(self.response.text)
        
    def testLoginWithWrongPasswd(self):
        """
        the 4th testcase
        账号存在，密码错误--->登陆
        :return:
        """
        # set body 
        localConfigHttp.set_data(busUserlogin.body4)
        # post http
        self.response = localConfigHttp.post()
        self.info = self.response.json()
        # check result of response
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.response.status_code, self.status_code4)
        self.assertEqual(self.info['code'], self.errorno4)
        self.assertEqual(self.info['msg'], self.msg4)
        #write_log
        self.log.build_case_code(sys._getframe().f_code.co_name, str(self.status_code4))
        self.log.build_case_response(self.response.text)

    def tearDown(self):
        """

        :return:
        """
