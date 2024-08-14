from selenium.webdriver.common.by import By
import time
from components.form_data import FormData
from components.ui_controls import UIControls
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Controller:
    def __init__(self, driver):
        self.driver = driver
        self.UIcontrols = UIControls(self.driver)
        ## Days
        self.tuesday = FormData("Tuesday", "04:00", "09:00", "Computer systems, data structures, data management in C")
        self.wednesday = FormData("Wednesday","04:00", "09:00", "Computer systems, data structures, data management in C")
        self.thursday = FormData("Thursday","04:00", "09:00", "Foundations of embedded networks, IIOT and Security")
        self.friday = FormData("Friday","04:00", "09:00", "Introduction to embedded systems")
        
        ## Login identifiers
        self.username_field_id = "Username"
        self.password_field_id = "Password"
        self.continue_btn_class = "btn.btn-block.btn-primary"
        self.add_btn_class = "btn.btn-primary.pull-right"
        
        ## Form identifiers
        self.activity_date_field_id = "Date"
        self.activity_type_field_id = "ParentActivityId"
        self.course_field_id = "UnitId"
        self.unit_field_id = "ParentModuleId"
        self.otj_field_id = "OnTheJob"
        self.time_spent_field_id = 'TimeValue'
        self.start_time_field_id = "ActivityStartTimeValue"
        self.comments_field_id = "Comments"
        ## Submit button class

    ## Retrieve user credentials in the console
    def get_user_credentials(self):
        self.username = input("Enter your smart assessor username: ")
        self.password = input("Enter your smart assessor password: ")
        
        
        if self.username and self.password:
            return True
        return False
        
        
    ## Log user in before executing script: Logged In: True | Fail: False
    def login(self):
        ...
        ## Check if already logged in - function will return null / false
        try:
            self.driver.find_element(By.ID, self.username_field_id)
        except:
            return True

        # Input username details
        self.UIcontrols.write_text_by_id(self.username, self.username_field_id)
        
        # Click continue
        self.UIcontrols.btn_click_by_class(self.continue_btn_class)
        
        # Input password
        self.UIcontrols.write_text_by_id(self.password, self.password_field_id)
        
        # Click Log In
        self.UIcontrols.btn_click_by_class(self.continue_btn_class)
        
        time.sleep(1)
        
        ## Check if we are still on the login screen
        try:
            self.driver.find_element(By.ID, self.username_field_id)
            return False
        except:
            return True
    
    ## Redirecting to the OTJ page
    def move_to_logp(self):
        self.driver.get('https://www.smartassessor.co.uk/ETimeSheet')
        
    def clear_username_field(self):
        username_field = self.driver.find_element(By.ID, self.username_field_id)
        username_field.clear()
        
    def start(self):
        ## Ensure any pre-loaded or pre-failed text is cleared
        self.clear_username_field()
        if self.get_user_credentials():
            if self.login():
                return self.move_to_logp()
            else:
                print("The login details were invalid. Let's try again...\n")
                return self.start()
        else:
            print("You have missing credentials...\n")
        
        ## Enters the data into the form iterating through all the dates
    def enter_data(self):

        days = [self.tuesday, self.wednesday, self.thursday, self.friday]
        completed = 0
        for day in days:
            dates = day.generate_dates()
            total_num = len(days) * len(dates)
            for date in dates:
                
        
                ## 1. Start new form - click add OTJ button
                self.UIcontrols.btn_click_by_class(self.add_btn_class)
                time.sleep(0.2)
                
                ## 1.1.  Switch the driver to an iFrame
                
                inner_iframe = self.driver.find_element(By.XPATH, '//*[@id="formModalFrame"]')
                self.driver.switch_to.frame(inner_iframe)
                print("Frame switched to iFrame \n")
                
                
                ## 2. Input date into the text field (convert datetime object to string in form day-month-year)
                self.UIcontrols.write_text_by_id(date.strftime("%dd/%mm/%Y"), self.activity_date_field_id)
                ## 3. Click the Activity type drop down menu and select correct option
                self.UIcontrols.access_dd(day.activity_type, self.activity_type_field_id)
                ## 4. Click the course drop down menu and select correct option
                self.UIcontrols.access_dd(day.course, self.course_field_id)
                time.sleep(1)
                ## 5. Click unit drop down menu and select correct option
                self.UIcontrols.access_dd(day.unit, self.unit_field_id)
                
                ## 6. Click OTJ drop down menu and select correct option
                self.UIcontrols.access_dd(day.otj, self.otj_field_id)
                
                ## 7. Input time spent into the text field
                self.UIcontrols.write_text_by_id(day.time_spent, self.time_spent_field_id)
            
                ## 8. Input activity start time into the text field
                self.UIcontrols.write_text_by_id(day.start_time, self.start_time_field_id)
                
                ## 9. Input the impact on learning into the text field
                self.UIcontrols.write_text_by_id(day.impact_on_learning, self.comments_field_id)
                
                
                 ## 10. Click the submit button - later - for now click 'close'
                self.UIcontrols.btn_click_by_class("btn.btn-primary")  
                      
                
                ## 11. switch back to main frame
                self.driver.switch_to.default_content()
                print("Frame switched to default")

                completed += 1
                print(f'Completing...{(completed / total_num) * 100}%')
                
                ## Testing
                time.sleep(0.5)
    
    
    def exec(self):
        ...
        ## Iterate through each day of the week and execute the enter date function
        
