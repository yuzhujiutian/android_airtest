# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)

def authApp():
    wait(Template(r"tpl1586150637555.png", record_pos=(0.041, 0.866), resolution=(1080, 2340)))


    while poco(text="允许"):
        poco(text="允许").click()
        sleep(0.5)
        


#选择app标签
def selectTab(tab_name):
    wait(Template(r"tpl1582528391192.png", record_pos=(-0.004, 0.893), resolution=(1080, 2340)))
    if tab_name == '关注':
        touch(Template(r"tpl1582711598967.png", record_pos=(-0.368, 0.935), resolution=(1080, 2340)))
    if tab_name == '工作台':
        touch(Template(r"tpl1582710603868.png", record_pos=(-0.11, 0.939), resolution=(1080, 2340)))
    if tab_name == '通知':
        touch(Template(r"tpl1582710570373.png", record_pos=(0.129, 0.939), resolution=(1080, 2340)))
    if tab_name == '我':
        touch(Template(r"tpl1582711633971.png", record_pos=(0.374, 0.939), resolution=(1080, 2340)))


#来到‘我’tab选择应用页展示方式式，并回到工作台
def selectMode(mode):
    '''
    mode    0：组织架构聚合    1:平铺
    '''
    assert_exists(Template(r"tpl1582528391192.png", record_pos=(-0.004, 0.893), resolution=(1080, 2340)), "处于app首页")
    '''
    if mode == 0:
        mode_text = '组织架构聚合'
    elif mode == 1:
            mode_text = '平铺'
    else:
        print ("模式参数错误")
        return 0
    '''
    #进入“我”工作栏
    selectTab('我')
    
    poco(text=mode).click()
    sleep(1)
    selectTab('工作台')

#组织架构模式选择组织层级(集团、公司、项目),输入名称搜索并进入
def selectOrg_0(org_name):
    wait(Template(r"tpl1582708076951.png", record_pos=(-0.225, -0.92), resolution=(1080, 2340)))
    touch(Template(r"tpl1582708076951.png", record_pos=(-0.225, -0.92), resolution=(1080, 2340)))
    
    poco(text='输入关键词搜索所有公司/项目').click()
    text(org_name,enter=False)
    sleep(1)
    poco(text=org_name,type='android.widget.TextView').click()


#组织架构模式选择app
def selectApp(app_name):
    
    print(poco.wait_for_any(poco(text='更多')))
    
    
    #检测首页是否有该模块，有则点击进入，否则返回异常，捕捉后进入更多应用选择
    try: 
        poco.wait_for_any(poco(text=app_name,type='android.widget.ImageView'))#之所以用imageview是因为统计导航栏的影响
        poco(text=app_name,type='android.widget.TextView').click()
    except PocoNoSuchNodeException:
        poco(text='更多').click()
        sleep(1)
        poco.wait_for_any(poco(text='排序'))
        
    try:
        poco.wait_for_any(poco(text=app_name,type='android.widget.ImageView'))
        poco(text=app_name,type='android.widget.TextView').click()
    except PocoNoSuchNodeException:
        swipe((500,1500),(500,700),duration=2) #从下到上画横线1秒
        poco(text=app_name).click()
        

#拍照，number为照片数        
def take_pic(number=2):
    for i in range(number):
        touch(Template(r"tpl1583141919455.png", record_pos=(-0.181, -0.749), resolution=(1080, 2340)))
        wait(Template(r"tpl1583142037699.png", record_pos=(0.002, 0.729), resolution=(1080, 2340)))
        sleep(1)
        touch(Template(r"tpl1583142037699.png", record_pos=(0.002, 0.729), resolution=(1080, 2340)))
        sleep(2)
        swipe((200,1000),(1000,1000),duration=1) #从左到右画横线1秒
        sleep(1)
        swipe((500,700),(500,1500),duration=1) #从上到下画横线1秒
        
        touch(Template(r"tpl1583142649056.png", record_pos=(0.439, -0.946), resolution=(1080, 2340)))
        sleep(1)

        

        
        
'''      
selectMode('组织架构聚合')
selectTab('工作台')
selectOrg_0(org_name='kentest项目10')
'''
    
'''

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("com.tencent.mm:id/dlh").setattr('checkable',True)

'''
