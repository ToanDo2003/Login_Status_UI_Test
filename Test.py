
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np



def get_senarios(name_csv):
    test_senarios = pd.read_csv(name_csv)
    test_senarios = np.array(test_senarios)
    return test_senarios

def open_site(browser):
    #Argument: type of browser drive
    #Function: Open the url of the website
    browser.maximize_window()
    browser.get("https://leetcode.com/accounts/login/")
    time.sleep(2)
    return
   
def input_login(username, password):
    #Arguments: the username and the password of the site
    #Function: Log in to the account for the user
    driver.find_element(By.NAME,'login').send_keys(username)
    driver.find_element(By.NAME,'password').send_keys(password)
    driver.find_element(By.ID,'signin_btn').click()
    time.sleep(3)

def check_status() ->bool:
    #Function: Check if in the account page after logged in
    return driver.find_elements(By.ID,'navbar-root')

    
    

name_csv = "Testing Accounts - Sheet1.csv"
test_senarios = get_senarios(name_csv)
mp = {}
for i in range(len(test_senarios)):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    open_site(driver)
    username = str(test_senarios[i][1])
    password = str(test_senarios[i][2])
    input_login(username, password)
    status = check_status()
    if status:
        mp[test_senarios[i][0]] = "Pass"
    else:
        mp[test_senarios[i][0]] = "Failed"       
    driver.quit()
    
print(mp)


