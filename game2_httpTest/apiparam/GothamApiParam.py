'''
Created on 2018年8月7日

@author: Admin
'''
'''
gotham api param
'''
import readConfig
localReadConfig = readConfig.ReadConfig()

class common():
    headers = {'clientType':'web','clientVersion': '0.1.0','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    global token
    token=localReadConfig.get_headers('token')
class busUserlogin():
    '''
    主渠道后台登陆接口
    '''
    case_name = 'busUserlogin_interface'
    '''账号密码正确'''
    body1='loginName=admin&pwd=e10adc3949ba59abbe56e057f20f883e&type=BUSINESS'
    '''账号不存在'''
    body2='loginName=AccountNotExist&pwd=e10adc3949ba59abbe56e057f20f883e&type=BUSINESS'
    '''账号存在但没有权限'''
    body3='loginName=test&pwd=202cb962ac59075b964b07152d234b70&type=BUSINESS'
    '''账号存在，密码错误'''
    body4='loginName=admin&pwd=202cb962ac59075b964b07152d234b70&type=BUSINESS'
class companyList():
    '''
    主渠道后台登陆接口
    '''
    case_name = 'companyList_interface'
    '''携带token'''
    body1='keyword=&page=1&rows=15&token=%s'%token
    '''不携带token'''
    body2='keyword=&page=1&rows=15&token='