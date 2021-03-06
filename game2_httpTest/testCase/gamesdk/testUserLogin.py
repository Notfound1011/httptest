#coding=utf-8
import unittest
from common import commonAw
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
from common import configDB

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localConfigDB = configDB.MyDB()
from apiparam.JokerApiParam import userlogin

class UserLogin(unittest.TestCase):
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
        self.case_name = userlogin.case_name
        self.method = userlogin.method
        self.token = ''
        self.headers = userlogin.headers
        self.body = userlogin.body
        self.result = ''
        self.errorno = 200
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
#         print(*productInfo_xls)
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        
    def testUserLogin(self):
        """
        test body
        :return:
        """
        # set url
        self.url = commonAw.get_url_from_xml('userlogin')
        localConfigHttp.set_url(self.url)
        
        # set headers
        localConfigHttp.set_data(self.body)
        localConfigHttp.set_headers(self.headers)
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
        print(self.info['data']['token'])
#         sql = commonAw.get_sql()
        localConfigDB.executeSQL('select * from g_login_record where id =356881')
        localConfigDB.closeDB()