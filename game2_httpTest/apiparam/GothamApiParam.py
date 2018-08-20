'''
Created on 2018年8月7日

@author: Admin
'''
'''
gotham api param
'''
from urllib import parse
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
    查询公司列表接口
    '''
    case_name = 'companyList_interface'
    '''携带token'''
    body1='keyword=&page=1&rows=15&token=%s'%token
    '''不携带token'''
    body2='keyword=&page=1&rows=15&token='
    '''使用厂商名查询'''
    keyword3='才宝'
    keyword_quote3=parse.quote(keyword3)
    body3='keyword=%s&page=1&rows=15&token=%s'%(keyword_quote3,token)
    '''使用公司名查询'''
    keyword4='上海才宝网络科技有限公司'
    keyword_quote4=parse.quote(keyword4)
    body4='keyword=%s&page=1&rows=15&token=%s'%(keyword_quote4,token)
    
class gameList():
    '''
    查询游戏列表接口
    '''
    case_name = 'gameList_interface'
    '''携带token，查询所有'''
    body1='keyword=&page=1&rows=15&token=%s'%token
    '''不携带token'''
    body2='keyword=&page=1&rows=15&token='
    '''查询单个游戏'''
    keyword='西游诀'
    keyword_quote=parse.quote(keyword)
    body3='keyword=%s&page=1&rows=15&token=%s'%(keyword_quote,token)

class gameSaveUpdate():
    '''
    新增/更新游戏的接口
    '''
    case_name = 'gameSave_interface'
    name='西游诀'
    name_quote=parse.quote(name)
    body='companyId=1&deliveryUrl=http://sync.1sdk.cn/cb/renrenshipin/BED427096E2870F0/sync.html&id=1001&name=%s&secretKey=123456&token=%s'%(name_quote,token)
    '''更新游戏---测试英文'''
    name1='testupdateEn'
    deliveryUrl1='testupdate'
    body1='companyId=1&deliveryUrl=%s&id=1001&name=%s&secretKey=123456&token=%s'%(deliveryUrl1,name1,token)
    '''更新游戏---测试中文'''
    name2='测试中文'
    deliveryUrl2='测试中文'
    name_quote2=parse.quote(name2)
    deliveryUrl_quote2=parse.quote(deliveryUrl2)
    body2='companyId=1&deliveryUrl=%s&id=1001&name=%s&secretKey=123456&token=%s'%(deliveryUrl_quote2,name_quote2,token)
    '''更新游戏---测试空值'''
    name3=''
    deliveryUrl3=''
    body3='companyId=1&deliveryUrl=%s&id=1001&name=%s&secretKey=123456&token=%s'%(deliveryUrl3,name3,token)

class gameSaveCreate():
    '''
    新增/更新游戏的接口
    '''
    case_name = 'gameSave_interface'
    '''新增游戏---测试英文'''
    name1='testupdateEn'
    deliveryUrl1='testupdate'
    body1='companyId=1&deliveryUrl=%s&id=1001&name=%s&secretKey=123456&token=%s'%(deliveryUrl1,name1,token)
    '''新增游戏---测试中文'''
    name2='测试中文'
    deliveryUrl2='测试中文'
    name_quote2=parse.quote(name2)
    deliveryUrl_quote2=parse.quote(deliveryUrl2)
    body2='companyId=1&deliveryUrl=%s&id=1001&name=%s&secretKey=123456&token=%s'%(deliveryUrl_quote2,name_quote2,token)
    '''新增游戏---测试空值'''
    name3=''
    deliveryUrl3=''
    body3='companyId=1&deliveryUrl=%s&id=1001&name=%s&secretKey=123456&token=%s'%(deliveryUrl3,name3,token)

if __name__=='__main__':
    print()
    