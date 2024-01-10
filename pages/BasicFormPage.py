import allure

from pages.BasePage import BasePage


class BasicFormPageLocators:
    USERNAME_INPUT = '//input[@name="username"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    COMMENT_INPUT = '//textarea[@name="comments"]'
    FILE_INPUT = '//input[@name="filename"]'
    CHECKBOXES_GROUP = ('//input[@value="cb1"]',
                        '//input[@value="cb2"]',
                        '//input[@value="cb3"]')
    RADIO_BTNS = ('//input[@value="rd1"]',
                  '//input[@value="rd2"]',
                  '//input[@value="rd3"]')
    SUBMIT_BTN = '//input[@value="submit"]'
    MAIN_SELECT = '//select[@name="multipleselect[]"]'
    DROPDOW_SELECT = '//select[@name="dropdown"]'


class BasicFormPage(BasePage):

    @allure.step('Submitting the form')
    def submit_form(self):
        self.click_element(locator=BasicFormPageLocators.SUBMIT_BTN)

    @allure.step('Filling the username input')
    def fill_username(self, value):
        self.fill_input(locator=BasicFormPageLocators.USERNAME_INPUT, value=value)

    @allure.step('Filling the password input')
    def fill_password(self, value):
        self.fill_input(locator=BasicFormPageLocators.PASSWORD_INPUT, value=value)

    @allure.step('Filling the comment textarea')
    def fill_comment(self, value):
        self.fill_input(locator=BasicFormPageLocators.COMMENT_INPUT, value=value)

    @allure.step('Uploading the file')
    def upload_file(self, path):
        self.get_element(locator=BasicFormPageLocators.FILE_INPUT). \
            set_input_files(files=path)

    @allure.step('Checking the box')
    def check_checkbox_by_number(self, checkbox_number):
        for checkbox in BasicFormPageLocators.CHECKBOXES_GROUP:
            if str(checkbox_number) in checkbox:
                if self.get_element_attribute(checkbox, 'checked') is None:
                    self.click_element(checkbox)

    @allure.step('Unchecking the box')
    def uncheck_all_checkboxes(self):
        for checkbox in BasicFormPageLocators.CHECKBOXES_GROUP:
            if self.get_element_attribute(checkbox, 'checked') == 'checked':
                self.click_element(checkbox)

    @allure.step('Selecting the radio button')
    def click_radio_button(self, button_number):
        for button in BasicFormPageLocators.RADIO_BTNS:
            if str(button_number) in button:
                self.click_element(button)

    @allure.step('Selecting the option')
    def select_option(self, value):
        self.get_element(locator=BasicFormPageLocators.MAIN_SELECT).select_option(value=value)

    @allure.step('Selecting the option from the dropdown list')
    def select_dropdown_option(self, value):
        self.get_element(locator=BasicFormPageLocators.DROPDOW_SELECT).select_option(value=value)

    @allure.step('Verifying all output data')
    def verify_all_data(self, username, password, comments, filename, hiddenField, checkboxes,
                        radioval, multipleselect, dropdown, submitbutton):
        self.assert_text_in_element('//li[@id="_valueusername"]', username)
        self.assert_text_in_element('//li[@id="_valuepassword"]', password)
        self.assert_text_in_element('//li[@id="_valuecomments"]', comments)
        self.assert_text_in_element('//li[@id="_valuefilename"]', filename.split('/')[-1])
        self.assert_text_in_element('//li[@id="_valuehiddenField"]', hiddenField)
        self.assert_text_in_element('//li[@id="_valuecheckboxes0"]', str(checkboxes))
        self.assert_text_in_element('//li[@id="_valueradioval"]', str(radioval))
        self.assert_text_in_element('//li[@id="_valuemultipleselect0"]', multipleselect)
        self.assert_text_in_element('//li[@id="_valuedropdown"]', dropdown)
        self.assert_text_in_element('//li[@id="_valuesubmitbutton"]', submitbutton)
