# -*- coding:utf-8 -*-
import requests
import readConfig as readConfig
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common import configHttp as configHttp
from common.Log import MyLog as Log
import json

localReadConfig = readConfig.ReadConfig()
proDir = readConfig.proDir
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


def get_visitor_token():
    """
    create a token for visitor
    :return:
    """
    host = localReadConfig.get_http("BASEURL")
    response = requests.get(host+"/v2/User/Token/generate")
    info = response.json()
    token = info.get("info")
    logger.debug("Create token:%s" % (token))
    return token


def set_visitor_token_to_config():
    """
    set token that created for visitor to config
    :return:
    """
    token_v = get_visitor_token()
    localReadConfig.set_headers("TOKEN_V", token_v)


def get_value_from_return_json(json, name1, name2):
    """
    get value by key
    :param json:
    :param name1:
    :param name2:
    :return:
    """
    info = json['info']
    group = info[name1]
    value = group[name2]
    return value


def show_return_msg(response):
    """
    show msg detail
    :param response:
    :return:
    """
    url = response.url
    msg = response.text
    print("\n请求的url是： "+url)
    
    print("\n响应的status_code是： "+str(response.status_code))
    # 
    print("\n响应的body是： "+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))

# ****************************** read testCase excel ********************************
def get_xls(xls_name, sheet_name):
    """
      将数据放在xlsx里，通过读取xls加载数据
    get interface data from xls file
    :return:
    """
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# ****************************** read SQL xml ********************************
'''
     下面三个函数实现的是读取xml文件中的数据；   根据xml的树状层级，读取文件中的sql语句
    函数逐层被下一个调用
'''
database = {}
def set_xml():
    """
    set sql xml
    :return:
    """
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                # print(tb[0].text)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text  #最后一层的Element可以用 .text方法来获取到值
                table[table_name] = sql
            database[db_name] = table
            # print(database)
####嵌套了三层字典#######

def get_xml_dict(database_name, table_name):
    """
    Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
    get()方法语法：dict.get(key, default=None)
    get db dict by given name
    :param database_name:
    :param table_name:
    :return:
    """
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict


def get_sql(database_name, table_name, sql_id):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    # sql = sql.strip()   ### .strip()去掉字符串前后的空格
    return sql


# ****************************** read interfaceURL xml ********************************

def get_url_from_xml(name):
    """
    By name get url from interfaceURL.xml
    :param name: interface's url name
    :return: url
    """
    url_list = []
    url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')
    tree = ElementTree.parse(url_path)
    for u in tree.findall('url'):
        url_name = u.get('name')
        if url_name == name:
            for c in u.getchildren():
                url_list.append(c.text)
    url = '/'.join(url_list)  # '/'.jion(list)  用/把列表里的字符串拼接起来
    return url
    
if __name__ == "__main__":
#     print(get_xls("userCase.xlsx","login"))
#     set_visitor_token_to_config()
    a=get_sql('test', 'testtable2', 'select_user')
    print(a)
    b=get_url_from_xml('busUserlogin')
    print(b)