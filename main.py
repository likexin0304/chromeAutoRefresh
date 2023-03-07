import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置刷新时间间隔
refresh_interval = 3  # 单位为秒

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开网页
driver.get("https://www.baidu.com")

# 循环刷新页面
while True:
    try:
        # 等待指定时间
        time.sleep(refresh_interval)

        # 刷新页面
        driver.refresh()

        # 等待页面刷新完成
        WebDriverWait(driver, 60).until(EC.staleness_of(driver.find_element(By.TAG_NAME, 'body')))
    except KeyboardInterrupt:
        # 捕获Ctrl+C按键事件，手动取消刷新
        print("刷新已取消")
        break

# 关闭浏览器
driver.quit()
