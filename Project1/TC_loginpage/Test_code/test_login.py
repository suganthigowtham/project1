import time
import pytest

from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginPage:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.Webdata().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        yield
        self.driver.quit()

    def enterText(self, locator, textvalue):
        self.wait = WebDriverWait(self.driver, 15)
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(textvalue)

    def clickButton(self, locator):
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def test_login(self, boot):
        try:
            # Username = 2
            # Password = 3
            # Test Results = 4
            # Row = 2 to End

            for row in range(2, data.Webdata().rowCount() + 1):
                username = data.Webdata().readData(row, 2)
                password = data.Webdata().readData(row, 3)
                self.enterText(locator.Weblocator().usernameLocator, username)
                self.enterText(locator.Weblocator().passwordLocator, password)
                self.clickButton(locator.Weblocator().loginLocator)
                if self.driver.current_url == data.Webdata().dashboardURL:
                    print("Logged in Successfully")
                    data.Webdata().writeData(row, 4, "Logged in Successfully")
                    self.clickButton(locator.Weblocator().dropdownLocator)
                    self.clickButton(locator.Weblocator().logoutLocator)
                else:
                    print(" Login Unsuccessful")
                    data.Webdata().writeData(row, 4, "Invalid Credentials")

        except NoSuchElementException as e:
            print(e)


       #pim test case
       
    #@pytest.mark.order1
    def test_addEmployee(self,boot):
        try:
            # This code is used to find the path and fill the username
            self.enterText(locator.Weblocator().usernameLocator, data.Webdata().username)
            # This code is used to find the path and fill the password
            self.enterText(locator.Weblocator().passwordLocator, data.Webdata().password)
            # This code is used to find the path and click the login button
            self.clickButton(locator.Weblocator().loginLocator)
            # This code is used to find the path and click PIM
            self.clickButton(locator.Weblocator().pimModuleLocator)
            # This code is used to find the path and click the add button
            self.clickButton(locator.Weblocator().addLocator)
            # This code is used to find the path and fill the firstname
            self.enterText(locator.Weblocator().fNameLocator, data.Webdata().firstname)
            # This code is used to find the path and fill the middlename
            self.enterText(locator.Weblocator().mNameLocator, data.Webdata().middlename)
            # This code is used to find the path and fill the lastname
            self.enterText(locator.Weblocator().lNameLocator, data.Webdata().lastname)
            # This code is used to find the path and click the save button
            self.clickButton(locator.Weblocator().saveLocator)
            time.sleep(10)

            print("Successfully added")
        except NoSuchElementException as e:
            print(e)

    #@pytest.mark.order2
    def test_editEmployee(self, boot):
        try:
            # This code is used to find the path and fill the username
            self.enterText(locator.Weblocator().usernameLocator, data.Webdata().username)
            # This code is used to find the path and fill the password
            self.enterText(locator.Weblocator().passwordLocator, data.Webdata().password)
            # This code is used to find the path and click the login button
            self.clickButton(locator.Weblocator().loginLocator)
            # This code is used to find the path and click PIM
            self.clickButton(locator.Weblocator().pimModuleLocator)
            # This code is used to find the path and fill the first name
            self.enterText(locator.Weblocator().employeeName, data.Webdata().firstname)
            # This code is used to find the path and click the search button
            self.clickButton(locator.Weblocator().searchLocator)
            # This code is used find the path  and click edit option
            self.clickButton(locator.Weblocator().editLocator)
            # This code is used to enter details for editing
            self.enterText(locator.Weblocator().dobLocator, data.Webdata().dateofbirth)
            # This code is used to find the path and click the save button
            self.clickButton(locator.Weblocator().saveLocator1)
            time.sleep(10)
            
            print("Successful Employee details addition")

        except NoSuchElementException as e:
            print(e)

    #@pytest.mark.order3
    def test_deleteEmployee(self, boot):
        try:
            # This code is used to find the path and fill the username
            self.enterText(locator.Weblocator().usernameLocator, data.Webdata().username)
            # This code is used to find the path and fill the password
            self.enterText(locator.Weblocator().passwordLocator, data.Webdata().password)
            # This code is used to find the path of click button
            self.clickButton(locator.Weblocator().loginLocator)
            # This code is used to find the path and click the PIM
            self.clickButton(locator.Weblocator().pimModuleLocator)
            # This code is used to search from the saved employee list
            self.enterText(locator.Weblocator().employeeName, data.Webdata().firstname)
            self.clickButton(locator.Weblocator().searchLocator)
            # This code is used to find the path and click the delete button
            self.clickButton(locator.Weblocator().deleteLocator)
            time.sleep(10)
            print("Successful deletion")
        except NoSuchElementException as e:
            print(e)     

