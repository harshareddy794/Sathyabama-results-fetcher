# Importing all selenium components for automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing all XLRD to get data in a excal sheet
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1') 

# This is the path for chrome web driver it can be diffrent for your system
path="C:\Program Files (x86)\chromedriver.exe"

#Initializing driver for chrome 
driver=webdriver.Chrome(path)

# Getting necssary details from user such as register number and date of birth
reg_no_input=input("Enter register number ")
dob_input=input("Enter data of birth ")

# Driver wait for input of data
driver.implicitly_wait(15)

# This will open the web page for Sathyabama results
driver.get('http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php')

# Searching for id called regno and sending our input register number to field
rolno_search=driver.find_element_by_id('regno')
rolno_search.send_keys(reg_no_input)

# Searching for id called dob and sending our input data of birth to field
dob_search=driver.find_element_by_id('dob')
dob_search.send_keys(dob_input)

# Searching for submit button and clicking on it
sumbit_search=driver.find_element_by_id('btnLogin')
sumbit_search.send_keys(Keys.RETURN)
try:
    # Waiting for 5 secounds to get page to loadup
    driver.implicitly_wait(5)

    # Searching for class name stuinfo and td in that stuinfo
    table_data=driver.find_element_by_class_name('stuinfo')
    td_data=table_data.find_elements_by_tag_name('td')

    # Using loop to get register number and name of the student
    for i in range(2):
        ind=str(td_data[i].text).find(':')
        sheet1.write(0,i,((td_data[i].text)[ind+2:]))
        if(i==0):
            regno_for_name=(td_data[i].text)[ind+2:]


    # Then searching for id tblDisplay to get table and searching for tbody and then finding all td in that tablebody
    table_search=driver.find_element_by_id('tblDisplay')
    tbody_data=table_search.find_element_by_tag_name('tbody')
    td_data=tbody_data.find_elements_by_tag_name('td')

    # All the raw data which is in web component format is converted into text and stored saparatly into a list object
    i=0
    lis=list()
    lis1=list()
    for data in td_data:
        lis.append(data.text)
        i+=1
        if(i==9):
            lis1.append(lis)
            i=0
            lis=[]

    # List that contains all the data is transversed and stored into a excel sheet work book
    for i in range(0,len(lis1)):
        for j in range(0,len(lis1[i])):
            sheet1.write(i+1,j,lis1[i][j])

    #function which converts marks into gpa
    def GPA(m):                        
        if(m>=90):
            return 10
        elif(m>=80 and m<90):
            return 9
        elif(m>=70 and m<80):
            return 8
        elif(m>=60 and m<70):
            return 7
        elif(m>=50 and m<60):
            return 6
        else:
            return 0

    #calculating SGPA and writing it into excel sheet
    sum=0
    for i in lis1:
        sum=sum+GPA(int(i[6]))
    avg=sum/8
    sheet1.write(10,0,'GRADE: '+str(avg))

    # Saving the excal sheet with the register number of student
    wb.save(regno_for_name+'.xls')
    print('Done writing data')

finally:
     # Closing the chrome web driver  
    driver.close()

