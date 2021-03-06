import os
import readConfig as readConfig
import logging
from datetime import datetime
import threading

localReadConfig = readConfig.ReadConfig()   #加载配置文件
s=0  #计数用

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger(name='rrtv_testgroup')
        self.logger.setLevel(logging.INFO)

        # defined handler   设置编码格式为utf8,防止中文乱码
        handler = logging.FileHandler(os.path.join(logPath, "output.log"),encoding='utf-8')
        # defined formatter  日志格式化
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")
        
    def build_case_body(self,case_name, body):
        """
        write test case line
        :param case_name:
        :param body:
        :return:
        """
        global s #引用全局变量
        s = s+1
        self.logger.info('----------   LOG NO.%s ------------'%s)
        self.logger.info("Casename: "+case_name+"Body: "+body)
        print("Casename: "+case_name+'\n'+"Body: "+body)
        return s
    
    def build_case_code(self, code):
        """
        write test case line
        :param code:
        :return:
        """
        self.logger.info("StatusCode:"+code)
        print("StatusCode: "+code)
        
    def build_case_response(self, result):
        """
        write test case line
        :param result:
        :return:
        """
        self.logger.info("Response: "+result)
        print("Response: "+result)
        
    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """
        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "result.txt")
        fb = open(result_path, "a+",encoding='utf-8')
        try:
            fb.write("Response: "+result+'\n')
        except FileNotFoundError as ex:
            self.logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
            
        return MyLog.log