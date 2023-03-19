from playwright.sync_api import Page
from playwright.sync_api import expect
from locators.salaries_page_locators import SalariesPageLocators
from pages.BasePage import BasePage

class SalariesPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def check_avg_salary(self):
        self.page.goto("./place.php?podjetje=Povio%20Labs")
        all_salaries = self.page.query_selector_all("td[name*='EUR']")
        for salary in all_salaries:
            # I'll deal with this later
            pass
