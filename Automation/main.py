
import time
from components.control import Controller
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
        
## ------------------------------------------------- RUNNING CODE ------------------------------------------------- ##
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Define the wait time for elements to load
wait = WebDriverWait(driver, 10)

# Open Smart Assessor login page
driver.get('https://www.smartassessor.co.uk/Account')
time.sleep(1)

print('''
         ___      __    __  .___________.  ______                 ______   .___________.      __                          
    /   \    |  |  |  | |           | /  __  \               /  __  \  |           |     |  |                         
   /  ^  \   |  |  |  | `---|  |----`|  |  |  |             |  |  |  | `---|  |----`     |  |                         
  /  /_\  \  |  |  |  |     |  |     |  |  |  |             |  |  |  |     |  |    .--.  |  |                         
 /  _____  \ |  `--'  |     |  |     |  `--'  |             |  `--'  |     |  |    |  `--'  |                         
/__/     \__\ \______/      |__|      \______/               \______/      |__|     \______/                          
                                                                                                                      
.______   ____    ____    .___  ___.  __  .______       __    ______  __       _______  _______   ___________    ____ 
|   _  \  \   \  /   /    |   \/   | |  | |   _  \     |  |  /      ||  |     |   ____||       \ |   ____\   \  /   / 
|  |_)  |  \   \/   /     |  \  /  | |  | |  |_)  |    |  | |  ,----'|  |     |  |__   |  .--.  ||  |__   \   \/   /  
|   _  <    \_    _/      |  |\/|  | |  | |      /     |  | |  |     |  |     |   __|  |  |  |  ||   __|   \      /   
|  |_)  |     |  |        |  |  |  | |  | |  |\  \----.|  | |  `----.|  `----.|  |____ |  '--'  ||  |____   \    /    
|______/      |__|        |__|  |__| |__| | _| `._____||__|  \______||_______||_______||_______/ |_______|   \__/     
                                                                                                                                                                                                                                                                      
      ''')

if __name__ == '__main__':
      c = Controller(driver)
      c.start()
      c.enter_data()
      time.sleep(5)