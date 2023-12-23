from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
driver = webdriver.Chrome()
#隐式等待
# driver.implicitly_wait(5)
driver.get('https://www.feishu.cn/')  #打开飞书页
driver.maximize_window()  #窗口最大化
sleep(1)  #等待网站加载完成
#将弹窗进行关闭
driver.find_element(By.XPATH,'//*[@class="hc_Popup-content"]//*[@data-elem-id="bfDkmelK7d"]').click()
#点击登录
driver.find_element(By.XPATH,'//*[@id="app"]//a[text()="登录"]').click()
#切换登录方式（不使用扫码登录）
driver.find_element(By.XPATH,'//*[@id="root"]//span[@class="universe-icon switch-icon"]').click()

sleep(1)
#输入手机号
driver.find_element(By.XPATH,'//*[@id="root"]//input[@name="mobile_input"]').send_keys('15817444832')
#勾选协议
driver.find_element(By.XPATH,'//*[@id="root"]//input[@role="checkbox"]').click()
#执行下一步
driver.find_element(By.XPATH,'//*[@id="root"]//button[text()="下一步"]').click()
sleep(1)
#输入密码
driver.find_element(By.XPATH,'//input[@name="password_input"]').send_keys('@asdf1234')
#执行下一步
driver.find_element(By.XPATH,'//div[@class="step-box__footer"]/button[text()="下一步"]').click()
sleep(3)
#定位多选框
driver.find_element(By.XPATH,'//span[@class="universe-icon _pp-product-icon"]').click()
#选定消息
driver.find_element(By.XPATH,'//div[@title="消息"]').click()
#获取所有窗口
whindowHandls=driver.window_handles
#切换到消息窗口
driver.switch_to.window(whindowHandls[1])
sleep(5)
#获取所有联系人
lists=driver.find_elements(By.XPATH,'//div[@class="larkc-badge"]')
lists[0].click()
#定义联系人名称
sendname="审批"
#点击联系人
driver.find_element(By.XPATH,f'//*[@id="root-messenger-nav-application"]//div[@class="list_items"]//div[@aria-label="{sendname}"]').click()

# sleep(10)
#获取发送消息输入框
el = WebDriverWait(driver,10,0.5,ignored_exceptions=None).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root-messenger-nav-application"]//pre[@data-text="发送给 审批"]')),message='未发现')
#输入内容
el.send_keys('lsakjdfalkjdflsdflassdfld')
#输入完成，回车发送
el.send_keys(Keys.ENTER)
sleep(5)
driver.close()
driver.quit()



