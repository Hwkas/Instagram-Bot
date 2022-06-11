from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaFollowerBot:
    def __init__(self, driver_path, url):
        # setting up selenium
        service_obj = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.get(url=url)

    def login(self, email, pasw):
        # logging in
        # getting hold of input fields
        # getting hold of the email field
        sleep(2)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(
            email)
        # getting hold of password field
        pasw_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
            pasw, Keys.ENTER)
        sleep(7)
        try:
            # getting hold of not now btn from save login
            notnow_l_btn = self.driver.find_element(By.XPATH,
                                                    '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        except:
            pass

        try:
            # getting hold of notnow btn from notification promt
            notnow_i_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()

        except:
            pass

    def find_followers(self, account):
        sleep(1)
        self.driver.get(url=account)
        sleep(1)
        followers_btn = self.driver.find_element(By.CSS_SELECTOR, "._aa_5 a").click()
        # use this while to if you want list of all the followers but as instagram has a day limit of number of people
        # you can follow in a single day, that why i am using for loop, to save time from unnecessary scrolling.
        # while True:
                for n in range(0, 4):
            sleep(2)
            try:
                # here '//a' helps in scrolling, '//a' is extra it's not a part of XPATH.
                for_scroll = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div//a').send_keys(
                    Keys.END)
            except:
                break
        getting_user_names = self.driver.find_elements(By.CSS_SELECTOR, "li a span")
        for name in getting_user_names:
            self.username_list.append(name.text)
            print(name.text)

    def follow(self):
        follow_btn = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for n in range(len(follow_btn)):
            try:
                follow_btn[n].click()
                with open(file="./follow_list.txt", mode="a") as data:
                    data.write(f"{self.username_list[n+2]}\n")

            except:
                try:
                    cancel_btn = self.driver.find_element(By.XPATH,
                                                          '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
                except:
                    follow_limit_reached = self.driver.find_element(By.XPATH,
                                                                    '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/h3').text
                    if follow_limit_reached == "Try again later":
                        sleep(5)
                        self.driver.quit()
