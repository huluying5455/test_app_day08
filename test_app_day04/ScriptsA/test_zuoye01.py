from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

class Test_log_exit:
    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 测试平台 ios android
        desired_caps['platformName'] = 'Android'
        # 版本
        desired_caps['platformVersion'] = '5.1'
        # 设备名字
        desired_caps['deviceName'] = 'sanxingqweqw'
        # app包名
        desired_caps['appPackage'] = 'io.manong.developerdaily'
        # app启动名
        desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'

        # 声明手机驱动对象 自启动启动参数中指定的app post接口 创建session
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def teardown_class(self):
        self.driver.quit()

    """所有定位方法依赖显示等待"""
    def wait_time(self, ty, ty_value):
        """
        显示等待
        :param ty:  定位类型 id class xpath属性值
        :param ty_value:  id属性值 class属性值 xpath属性值
        :return: 返回定位对象
        """
        if ty == "id":
            return WebDriverWait(self.driver, 15, 1).until(lambda x: x.find_element_by_id(ty_value))
        if ty == "xpath":
            return WebDriverWait(self.driver, 15, 1).until(lambda x: x.find_element_by_xpath(ty_value))

    def test_log(self):
        # 定位 '我的 '按钮 class  需要多个
        xpath_text = "//*[contains(@text,'我的') and contains(@resource-id,'io.manong.developerdaily:id/tv_tab_title')]"
        self.wait_time("xpath", xpath_text).click()

        # id定位登录
        self.wait_time('id', 'io.manong.developerdaily:id/login_btn').click()
        # xpath 定位密码输入
        xpath_text = "//*[contains(@text,'密码登录')]"
        self.wait_time("xpath", xpath_text).click()

        # id定位用户名密码,登录
        self.wait_time("id", "io.manong.developerdaily:id/edt_phone").send_keys("17521065652")
        self.wait_time("id", "io.manong.developerdaily:id/edt_password").send_keys('123456')
        self.wait_time("id", "io.manong.developerdaily:id/btn_login").click()

        # 获取文本信息
        ele = self.driver.find_element_by_id("io.manong.developerdaily:id/nav_btn_coin_total").text
        # if "我的IO币" in ele:
        #     print("登录成功")
        # else:
        #     print("登录失败")
        assert "我的IO币" in ele

    def test_exit(self):
        # 滑动
        end = self.driver.find_element_by_id("io.manong.developerdaily:id/user_name_layout")
        start = self.driver.find_element_by_id("io.manong.developerdaily:id/nav_btn_subscribe")
        self.driver.scroll(start, end)
        time.sleep(2)
        # 点击设置
        # driver.find_element_by_xpath("//*[contains(@text,'设置')]").click()
        self.wait_time("xpath", "//*[contains(@text,'设置')]").click()
        # 点击退出当前账号
        # driver.find_element_by_xpath("//*[contains(@text,'退出当前账户')]").click()
        self.wait_time("xpath", "//*[contains(@text,'退出当前账户')]").click()
        # 点击确定退出
        # driver.find_element_by_id("io.manong.developerdaily:id/md_buttonDefaultPositive").click()
        self.wait_time("id", "io.manong.developerdaily:id/md_buttonDefaultPositive").click()
        # 滑动  昨日收益 --> 合作申请
        start = self.driver.find_element_by_xpath("//*[contains(@text,'昨日收益')]")
        end = self.driver.find_element_by_xpath("//*[contains(@text,'合作申请')]")
        self.driver.drag_and_drop(start, end)
        time.sleep(2)

        # 定位登录/注册
        log = self.driver.find_element_by_id("io.manong.developerdaily:id/login_btn")
        # 判断退出成功
        # if "登录/注册" in log.text:
        #     print("退出成功")
        # else:
        #     print("退出失败")
        assert "登录/注册" in log.text
