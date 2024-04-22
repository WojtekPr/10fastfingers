from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class openapp():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def opnen_site(self):
        self.driver.get('https://10fastfingers.com/typing-test/polish')   
        
        sleep(1)

        cookies = self.driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
        cookies.click()

        bot.write_words()
        
    def write_words(self):
        inputfield = self.driver.find_element(By.ID,'inputfield')
        # test = 1
        # word = self.driver.find_element(By.XPATH,f'/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[{test}]')
        # print(word.text)
        i = 1
        while True:
            try:
                # path = f'/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[{i}]'
                word = self.driver.find_element(By.XPATH,f'/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[{i}]')
                print(word.text)
                inputfield.click()
                inputfield.send_keys(word.text)
                inputfield.send_keys(Keys.SPACE)
                if not word:
                    print("koniec elementow")
                    time.sleep(20)  # Przerwij pętlę, jeśli lista elementów jest pusta
                # Tutaj możesz wykonać dowolne działania na znalezionych elementach, np. kliknięcie, pobranie tekstu, itp.
                i += 1
            except:
                print("KONIEC")
                time.sleep(40)
        
        # inputfield.click()
        # inputfield.send_keys(word.text)
        # inputfield.send_keys(Keys.SPACE)


        time.sleep(10)




    def exit(self):
        input("Naciśnij dowolny klawisz, aby zakończyć...")
        self.driver.quit()


bot = openapp()
bot.opnen_site()
# bot.exit()
