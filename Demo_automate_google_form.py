
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
import time



class form_google():
    
    def landing_page(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)  
        self.driver.implicitly_wait(3)
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeRD7T3BBRWwLQVHV91wH_YGyEvcBsop7y8xN_qIou61D0zPQ/viewform")
        self.driver.maximize_window()
        time.sleep(3)

    def answer_invitation(self,ussername, member_count,allergy,email_member):
        index_number = 4
        inputs = self.driver.find_elements(By.XPATH,"//input[@class='whsOnd zHQkBf']") 
        

        input_array = [
            ussername,member_count,allergy,email_member
        ]

        for i in range(len(inputs)):
            # inputs[i].clear()
            inputs[i].send_keys(input_array[i])
        

        self.driver.implicitly_wait(3)
        attend_option = self.driver.find_elements(By.XPATH,"//div[@role='radio']")

        for radio_option in attend_option:
            if radio_option == attend_option[1]:
                pass
            else:
                radio_option.click()


        checkBox_list =self.driver.find_elements(By.XPATH,"//div[@role='checkbox']")
        self.driver.implicitly_wait(3)

        for checkbox in checkBox_list:
            if checkbox == checkBox_list[2]:
                pass
            elif checkbox == checkBox_list[5]:
                pass
            else:
                checkbox.click()
                # input_other = self.driver.find_element(By.XPATH,"//input[@class='Hvn9fb zHQkBf']").send_keys("lala")
            

        self.driver.implicitly_wait(3)
        selected_list = self.driver.find_element(By.XPATH,'//span[@class="vRMGwf oJeWuf"]')
        selected_list.click()

        for _ in range(index_number):
            pyautogui.keyDown('down')
        pyautogui.keyDown('enter')

        button_sand = self.driver.find_element(By.XPATH,"//span[@class='NPEfkd RveJvd snByac']").click()
        
        
member = form_google()
member.landing_page()
member.answer_invitation("Wang Yi Bo tester","1","Tidak","berhasil@gmail.com")