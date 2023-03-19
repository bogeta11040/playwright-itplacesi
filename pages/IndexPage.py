from playwright.sync_api import Page
from playwright.sync_api import expect

from locators.index_page_locators import IndexPageLocators
from pages.BasePage import BasePage


class IndexPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def test_elements_presence(self):
        super().test_elements_presence()
        expect(self.page.locator(IndexPageLocators.BANNER)).to_be_visible()
        expect(self.page.locator(IndexPageLocators.BANNER)).to_contain_text("Raziščite plače v industriji IT")
        expect(self.page.locator(IndexPageLocators.DROPDOWN)).to_be_visible()
        expect(self.page.locator(IndexPageLocators.BTN)).to_be_visible()



