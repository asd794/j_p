# 載入selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 建立Chrome Driver的執行檔路徑
options=Options()
options.chrome_executable_path="D:\practice\python\selenium-start\chromedriver.exe"
# 建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
driver.maximize_window() # 視窗最大化
driver.get('https://www.ntu.edu.tw/')
driver.save_screenshot("截圖.png") # 做網頁截圖
driver.close()