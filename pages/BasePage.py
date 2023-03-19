from playwright.sync_api import Page
from playwright.sync_api import expect

from locators.base_page_locators import BasePageLocators

class BasePage:
    def test_elements_presence(self):
        expect(self.page.locator(BasePageLocators.NAVBAR)).to_be_visible()
        expect(self.page.locator(BasePageLocators.HOME)).to_be_visible()
        expect(self.page.locator(BasePageLocators.SALARIES)).to_be_visible()
        expect(self.page.locator(BasePageLocators.REVIEWS)).to_be_visible()
        expect(self.page.locator(BasePageLocators.COMPANIES)).to_be_visible()
        expect(self.page.locator(BasePageLocators.FOOTER)).to_be_visible()

    def test_navbar_links(self):
        expect(self.page.locator(BasePageLocators.HOME)).to_have_attribute("href", "./index.php")
        expect(self.page.locator(BasePageLocators.SALARIES)).to_have_attribute("href", "./place.php")
        expect(self.page.locator(BasePageLocators.REVIEWS)).to_have_attribute("href", "#")
        expect(self.page.locator(BasePageLocators.COMPANIES)).to_have_attribute("href", "./podjetja.php")