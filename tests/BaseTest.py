from pages.BasePage import BasePage


class Test:
    def test(self, page):
        p = BasePage(page=page, url="https://www.google.com/")
        p.open()
        print('\n')
        print(p.get_page_title())
        print(p.get_page_url())
        print(p.get_element_attribute('(//textarea)[1]', "name"))
        print(p.get_elements_count("//div"))
        p.wait(1)
        p.refresh_page()
        p.fill_input("//*[@name='q']","123")
        p.wait(1)
        p.fill_input("//*[@name='q']","1234")
        p.click_element('//a[@aria-label="Войти"]')
        p.wait(1)
