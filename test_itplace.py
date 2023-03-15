import unittest

import pytest
from playwright.sync_api import Page

from pages.IndexPage import BasePage
from pages.AuthPage import AuthPage
from pages.SubmitSalary import SubmitSalary


class Testiranje(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.auth_page = AuthPage(page)
        self.submit_salary_page = SubmitSalary(page)

    @pytest.mark.smoke
    def test_index_proper_design(self):
        self.page.goto('/')
        self.base_page.test_elements_presence()
        self.base_page.test_navbar_links()

    @pytest.mark.smoke
    def test_salaries_page_proper_design(self):
        self.page.goto('./place.php')
        self.base_page.test_elements_presence()
        self.base_page.test_navbar_links()

    @pytest.mark.smoke
    def test_companies_page_proper_design(self):
        self.page.goto('./podjetja.php')
        self.base_page.test_elements_presence()
        self.base_page.test_navbar_links()

    @pytest.mark.smoke
    @pytest.mark.authorization
    def test_github_authorization(self):
        self.auth_page.auth_with_github()

    @pytest.mark.smoke
    @pytest.mark.authorization
    def test_linkedin_authorization(self):
        self.auth_page.auth_with_linkedin()

    @pytest.mark.smoke
    def test_submit_salary_page_proper_design(self):
        self.auth_page.auth_with_github()
        self.base_page.test_elements_presence()
        self.base_page.test_navbar_links()
        self.submit_salary_page.test_elements_presence()

    @pytest.mark.smoke
    def test_submit_button(self):
        self.auth_page.auth_with_github()
        self.submit_salary_page.submit_button_click()

    @pytest.mark.smoke
    @pytest.mark.submit
    def test_fill_data_and_submit_form(self):
        self.auth_page.auth_with_github()
        self.submit_salary_page.submit_salary("Endava", "Ljubljana", "Android Developer", "Junior", "1300", "1800")


