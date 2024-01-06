from time import sleep

import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = f"{url}"

    @allure.step("Open the page")
    def open(self):
        self.page.goto(url=self.url)
        self.page.wait_for_selector('body')

    @allure.step("Get page title")
    def get_page_title(self):
        return self.page.title()

    @allure.step("Get page url")
    def get_page_url(self):
        return self.page.url

    @allure.step("Find element")
    def get_element(self, locator):
        return self.page.locator(selector=locator)

    @allure.step("Get element attribute")
    def get_element_attribute(self, locator, attr):
        return self.get_element(locator).get_attribute(attr)

    @allure.step("Count elements")
    def get_elements_count(self, locator):
        return self.get_element(locator).count()

    # @allure.step("Implicit wait")
    # def wait_for(self, event):
    #     self.page.expect_event()

    @allure.step("Explicit wait")
    def wait(self, time: float):
        return sleep(time)

    @allure.step("Click on the element")
    def click_element(self, locator):
        self.get_element(locator).click()

    @allure.step("Input text")
    def fill_input(self, locator, value):
        self.page.fill(selector=locator, value=value)

    @allure.step("Refresh page")
    def refresh_page(self):
        self.page.reload()
