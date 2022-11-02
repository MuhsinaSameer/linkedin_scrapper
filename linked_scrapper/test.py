from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

#Specifies the location of the web driver
driver = webdriver.Chrome("C:\users\Muhsina\chromedriver.exe")
#The driver.get() method will navigate to the given URL Address
driver.get('https://www.linkedin.com')
#Applying a delay for the web page to load
driver.implicitly_wait(1)

#Locating the email field on the Linkedin login page
username = driver.find_element('//*[@type="text"]')
#Entering in an email address 
username.send_keys(Email)
#Locating the password field on the Linkedin login page
password = driver.find_element('//*[@type="password"]')
#Entering in a password
password.send_keys(Password)
#Locating the Login button on the Linkedin login page
log_in_button= driver.find_element('//*[@class="sign-in-form__submit-button"]')
#Clicking on the Login button
log_in_button.click()
#Applying a delay for the web page to load
driver.implicitly_wait(1)


headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
           }

company_link = 'https://www.linkedin.com/voyager/api/entities/companies/2652230'

with requests.session() as s:
    s.cookies['AQEDATp67EUBpq32AAABhDj72twAAAGEXQhe3FYAMgjMPYgCmyLejmbvvAMF8_cGa1gyVBq-ZkoXZw2TcWUeeOKUuzbzrIyOYtz1Q1QFDhtxMfqNtiHEfHikcF05pJV1ZzxaGrutJ2ubNQQSZvXonLPQ'] = "your li_at cookie"
    s.cookies["JSESSIONID"] = "ajax:3593733563814573248"
    s.headers = headers
    s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
    response = s.get(company_link)
    response_dict = response.json()
    print(response_dict)