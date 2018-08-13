import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
from common import HTMLTestReportCN
from common.configEmail import MyEmail

'''加载对应环境的配置文件 '''
localReadConfig = readConfig.ReadConfig()

class AllTest:
    def __init__(self):
        '''初始化'''
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        on_off = localReadConfig.get_email("on_off")
        self.caseListFile = os.path.join(readConfig.proDir, "gotham_caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        # self.caseFile = None
        self.caseList = []
        self.email = MyEmail.get_email()
        '''定义接口测试报告的title'''
        MyEmail.get_email().subject="gotham接口测试报告" + " " + MyEmail.get_email().date
    def set_case_list(self):
        """
        set case list
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))   #也可以用 data.strip()
        fb.close()

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        
        for case in self.caseList:
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        
        return test_suite
        
    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='Test Report', description='RRTV Project_Game Interface Test')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
