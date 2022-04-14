from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime

options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox()
browser.get('https://www.cotps.com/#/pages/login/login?originSource=transaction')


def print_hi():

    time.sleep(10)
    ghs = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text/span")
    print(ghs.text)
    if(ghs.text=="Ghana +233"):

        login()

    else:
        #browser.find_element(By.textboxLocator).sendKeys("\uE035")
        browser.get(browser.current_url)
        login()

        print("hi")

def login():
    countrybutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text")
    countrybutton.click()
    time.sleep(3)
    elements = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[80]"))
    )
    selectcountrybutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[80]")
    selectcountrybutton.click()
    time.sleep(1)
    username = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input")
    username.send_keys('0546848386')
    password = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input")
    password.send_keys('enoch123')
    browser.implicitly_wait(120)
    # print(ghs.text)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "login")
    button.click()
    time.sleep(5)
    elements = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]"))
    )
    transactionsbutton = browser.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[3]/div")
    transactionsbutton.click()
    trading()

def trading():
    while True:
        browser.refresh()
        time.sleep(5)
        elements = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]"))
        )
        time.sleep(5)
        intransactions = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]")
        print(intransactions.text)
        walletbalance = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]")
        intransaction = float(intransactions.text)
        walletbalances = float(walletbalance.text)
        if(intransaction==0.000):

            while walletbalances > 5.000:
                tradingbutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button")
                tradingbutton.click()
                time.sleep(5)
                sell = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]"))
                )
                time.sleep(5)
                sellbutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]")
                sellbutton.click()
                time.sleep(5)
                comfim = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]"))
                )
                time.sleep(5)
                comfimbutton= browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button")
                comfimbutton.click()
                time.sleep(5)
                walletbalance = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]")
                walletbalances = float(walletbalance.text)
                print(walletbalances)
            print("ho")
            
        elif(walletbalances < 5.000):
            #minebutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[2]")
            #minebutton.click()
            browser.refresh()
            time.sleep(5)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        time.sleep(7800)
def loop():
    while True:
        browser.refresh()
        time.sleep(5)
        trading()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        time.sleep(7800)
    #    tradingbutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button")
    #    tradingbutton.click()
    #    elementss = WebDriverWait(browser, 10).until(
    #        EC.presence_of_element_located((By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]"))
    #    )
    #    sellbutton = browser.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]")
     #   sellbutton.click()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
