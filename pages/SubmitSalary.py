from playwright.sync_api import Page
from playwright.sync_api import expect
from locators.submit_salary_locators import SubmitSalaryLocators
from pages.BasePage import BasePage


class SubmitSalary(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def test_elements_presence(self):
        super().test_elements_presence()
        expect(self.page.locator(SubmitSalaryLocators.COMPANY_LOCATION)).to_be_visible()
        expect(self.page.locator(SubmitSalaryLocators.COMPANY_NAME)).to_be_visible()
        expect(self.page.locator(SubmitSalaryLocators.POSITION)).to_be_visible()
        expect(self.page.locator(SubmitSalaryLocators.SENIORITY)).to_be_visible()
        expect(self.page.locator(SubmitSalaryLocators.NET_PAY)).to_be_visible()
        expect(self.page.locator(SubmitSalaryLocators.GROSS_PAY)).to_be_visible()
        expect(self.page.locator(SubmitSalaryLocators.SUBMIT_BTN)).to_be_visible()

    def submit_button_click(self):
        self.page.locator(SubmitSalaryLocators.SUBMIT_BTN).click()

    def submit_salary(self, company, location, position, seniority, net, gross):
        company = company
        location = location
        position = position
        seniority = seniority
        net = net
        gross = gross
        self.page.locator(SubmitSalaryLocators.COMPANY_NAME).select_option(company)
        self.page.locator(SubmitSalaryLocators.COMPANY_LOCATION).select_option(location)
        self.page.locator(SubmitSalaryLocators.POSITION).select_option(position)
        self.page.locator(SubmitSalaryLocators.SENIORITY).select_option(seniority)
        self.page.locator(SubmitSalaryLocators.NET_PAY).click()
        self.page.locator(SubmitSalaryLocators.NET_PAY).fill(net)
        self.page.locator(SubmitSalaryLocators.GROSS_PAY).click()
        self.page.locator(SubmitSalaryLocators.GROSS_PAY).fill(gross)
        self.submit_button_click()
        print(f"Salary is submitted via form.")
