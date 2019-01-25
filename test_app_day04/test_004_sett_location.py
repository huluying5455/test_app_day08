from appium import webdriver
import time
class Test_set:
    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.quit()

    def test_a(self):
        # 定位存储  更多
        start = self.driver.find_element_by_xpath("//*[contains(@text,'存储')]")
        end = self.driver.find_element_by_xpath("//*[contains(@text,'更多')]")
        # 存储滑动到更多
        self.driver.drag_and_drop(start,end)
        # 点击位置信息
        self.driver.find_element_by_xpath("//*[contains(@text,'位置信息')]").click()
        # 点击模式
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@text,'模式')]").click()
        # 点击准确度高
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@text,'使用GPS、')]").click()
        # 点击返回按钮
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # 获取当前模式结果  断言
        # result = self.driver.find_element_by_id("android:id/summary")
        # 1. 单个值断言
        # assert "准确度高" in result.text
        # # 2. 判断元素是否存在断言 --> 不推荐
        # try:
        #     # 定位元素
        #     self.driver.find_element_by_xpath("//*[contains(@text,'准确度高')]")
        #     assert True
        # except:
        #     assert False
        # 3. 判断值 在列表中断言
        result = self.driver.find_elements_by_id("android:id/summary")
        assert "准确度高" in [i.text for i in result]