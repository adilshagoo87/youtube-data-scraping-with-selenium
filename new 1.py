import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
df = pd.DataFrame(columns=['links', 'title', 'description','category'])
def get_links(l):
	PROXY = "23.237.173.102:3128"
	chrome_options= webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=%s' % PROXY)
	chrome_path="C:\\Users\\Adil Shagoo\\Desktop\\youtube project\\chromedriver.exe"
	driver=webdriver.Chrome(chrome_path,options=chrome_options)
	for j in range(len(l)):
		driver.get("https://www.youtube.com/results?search_query=%23"+l[j])
		time.sleep(3)
		for i in range(1):
			driver.execute_script("window.scrollTo(0,(window.pageYOffset+2040))")
			time.sleep(3)
		user_data=driver.find_elements_by_xpath("//*[@id='video-title']")
		links = []
		for i in user_data:
			links.append(i.get_attribute('href'))
		links = [x for x in links if x is not None]
		links = links[:100]
		wait = WebDriverWait(driver, 10)
		v_category = l[j] 
		for x in links:     
			driver.get(str(x))
			v_id = x.strip('https://www.youtube.com/watch?v=')
			v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
			v_description =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
			df.loc[len(df)] = [v_id, v_title, v_description, v_category]
catu = ['travel','science and technology','food','manufacturing','history','art and music']
get_links(catu)
df.to_csv('youtube.csv',index=False)