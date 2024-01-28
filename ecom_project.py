from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import winsound
import time
import os
from dotenv import load_dotenv

load_dotenv()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)


# driver.get('https://www.flipkart.com/search?q=laptops')
driver.get('https://www.amazon.in/')
driver.maximize_window()

# open = driver.find_element(By.XPATH,'Sign in]')
# open.click()

signin = driver.find_element(By.XPATH,'//span[text()="Hello, sign in"]')
signin.click()


input_text_email = driver.find_element(By.ID, 'ap_email')
input_text_email.send_keys(os.getenv('MY_EMAIL'))

continues = driver.find_element(By.ID, 'continue')
continues.click()

input_text_pass = driver.find_element(By.ID, 'ap_password')
input_text_pass.send_keys(os.getenv('MY_PASSWORD'))

passwords = driver.find_element(By.ID,'signInSubmit')
passwords.click()


phones = driver.find_element(By.XPATH,'//a[text()="Mobiles"]')
phones.click()



oneplus = driver.find_element(By.XPATH,'//span[text()="OnePlus Nord CE 3 Lite 5G (Chromatic Gray, 8GB RAM, 128GB Storage)"]')

ActionChains(driver).move_to_element(oneplus).perform()

time.sleep(5) 
oneplus.click()
# time.sleep(20)

# driver.get('https://www.amazon.in/OnePlus-Nord-Chromatic-128GB-Storage/dp/B0BY8MCQ9S/ref=lp_1389401031_1_1?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=SXJCH2R72MQ0G58FYEMB&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D')
# driver.get(driver.current_url)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

driver.find_element(By.ID,"buy-now-button").click();
driver.get('https://www.amazon.in/gp/cart/view.html?ref_=nav_cart')
# addtocart = driver.find_element(By.ID,'add-to-cart-button')
# # addtocart = driver.find_element(By.ID,'submit.buy-now-announce')
# # addtocart = driver.find_element(By.ID,'buy-now-button.a-button-input')
# addtocart.submit()


# WebElement avc =  wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("writeherethenameofbutton")))
# Addtocart=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div[5]/div[1]/div[4]/div/div/div[1]/div/div/div[1]/div/div[2]/div/form/div/div/div[15]/div[1]/span/span/span/input")
# Addtocart = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div[4]/div[4]/div/form/div/div[1]/span/span/span/input")
# Addtocart = driver.find_element(By.ID,"add-to-cart-button")
# Addtocart = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[41]/div/div/span/span/input") 
# Addtocart.click()

# driver.find_element(By.XPATH, '//*[text()=" Buy Now "]').click()


# driver.find_element(By.ID,"buy-now-button").click();
# ActionChains(driver).move_to_element(buynow).perform()
# buynow.click()

# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
# driver.implicitly_wait(20)
# addtocart = driver.find_element(By.XPATH,'//input[@id="buy-now-button"]')
# WebElement myDynamicElement = (new WebDriverWait(driver, 10)).until(ExpectedConditions.presenceOfElementLocated(By.id("usrUTils")));
# addtocart.submit()
# proceedtoBuy = driver.find_element(By.ID,'sc-buy-box-ptc-button')
# proceedtoBuy.click()

# try:
#     addCart = driver.find_element(By.CLASS_NAME,"a-button-stack")
#     ActionChains(driver).moveToElement(addCart);
#     addCart.submit()

#     frequency = 2500
#     duration = 50
#     winsound.Beep(frequency, duration)
#     time.sleep(2)
#     completeTheShopping = driver.find_element(By.CLASS_NAME,"a-button-inner")
#     completeTheShopping.click()
#     time.sleep(2)
#     buyNow = driver.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]/span/input')
#     buyNow.click()


#     print("Item found")

# except NoSuchElementException:
#     print("Item doesnt exist")