#coding=utf-8
import unittest
from common import commonAw
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
from common import configDB
from apiparam.JokerApiParam import userinfo

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()


class UserInfo(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param goods_id:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.case_name = userinfo.case_name
        self.method = userinfo.method
        self.token = ''
        self.headers = userinfo.headers
        self.body = userinfo.body
        self.result = ''
        self.errorno = ''
        self.data = ''
        self.response = None
        self.info = None

    def description(self):
        """

        :return:
        """
        self.case_name
    def setUp(self):
        """
        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        
        # set url
        self.url = commonAw.get_url_from_xml('userlogin')
        localConfigHttp.set_url(self.url)
        
        # set headers&body 
        localConfigHttp.set_data(self.body)
        localConfigHttp.set_headers(self.headers)
        # post http
        self.response = localConfigHttp.post()
        self.info = self.response.json() 
        self.token = self.info['data']['token']
        
    def testUserInfo(self):
        """
        test body
        :return:
        """
        # set url
        self.url = commonAw.get_url_from_xml('userinfo')
        localConfigHttp.set_url(self.url)
        
        # set headers
        headers = {'clientVersion': '4.0.0','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

        token ='8f5212edcb034d4aae41b6efa23b919d'
        body = 'channel_id=0&sid=8993a8dcf7424b9d89b292b62f881fb0&game_id=1024&token='+token+'&'
        print(body)
        localConfigHttp.set_data(body)
        localConfigHttp.set_headers(headers)
        # post http
        self.response = localConfigHttp.post()
        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        self.log.build_case_code(self.case_name, str(self.errorno), str(self.info['data']))
        self.log.build_case_response(self.response.text)

    def checkResult(self):
        self.info = self.response.json()
        commonAw.show_return_msg(self.response)
        self.assertEqual(self.info['errorno'], self.errorno)
        self.assertEqual(self.info['data']['account'], 'shiyuyu')
#         sql = commonAw.get_sql()
        localConfigDB.executeSQL('select * from g_login_record where id =356881')
        localConfigDB.closeDB()