from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path="C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome(path)

driver.get('http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php')


rolno_search=driver.find_element_by_id('regno')
rolno_search.send_keys('')

dob_search=driver.find_element_by_id('dob')
dob_search.send_keys('')


sumbit_search=driver.find_element_by_id('btnLogin')
sumbit_search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

# table_data=driver.find_element_by_class_name('stuinfo')
# try:
#     td_data=table_data.find_elements_by_tag_name('td')
#     for i in range(2):
#         ind=str(td_data[i].text).find(':')
#         print((td_data[i].text)[ind+2:])

# finally:


# td_data=tbody_data.find_elements_by_tag_name('td')
# for i in range(0,len(td_data)):
#     print(td_data[1].text)
#     if(i%9==0):
#         print("\n")


table_search=driver.find_element_by_id('tblDisplay')
tbody_data=table_search.find_element_by_tag_name('tbody')
td_data=tbody_data.find_elements_by_tag_name('td')
i=0
lis=list()
lis1=list()
for data in td_data:
    lis.append(data.text)
    i+=1
    if(i==8):
        lis1.append(lis)
        i=0
        lis=[]
print((td_data[0]).text)

print(lis1)
driver.close()


