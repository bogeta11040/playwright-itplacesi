import unittest

import pytest
from playwright.sync_api import Page

from pages.IndexPage import IndexPage
from pages.AuthPage import AuthPage
from pages.SalariesPage import SalariesPage
from pages.SubmitSalary import SubmitSalary


class Testiranje(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.index_page = IndexPage(page)
        self.auth_page = AuthPage(page)
        self.salaries_page = SalariesPage(page)
        self.submit_salary_page = SubmitSalary(page)

    @pytest.mark.smoke
    def test_index_proper_design(self):
        self.page.goto('/')
        self.index_page.test_elements_presence()
        self.index_page.test_navbar_links()

    @pytest.mark.smoke
    def test_salaries_page_proper_design(self):
        self.page.goto('./place.php')
        self.salaries_page.test_elements_presence()
        self.salaries_page.test_navbar_links()

    @pytest.mark.smoke
    def test_companies_page_proper_design(self):
        self.page.goto('./podjetja.php')
        self.index_page.test_elements_presence()
        self.index_page.test_navbar_links()

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
        self.submit_salary_page.test_elements_presence()
        self.submit_salary_page.test_navbar_links()

    @pytest.mark.smoke
    def test_submit_button(self):
        self.auth_page.auth_with_github()
        self.submit_salary_page.submit_button_click()

    @pytest.mark.smoke
    @pytest.mark.submit
    def test_fill_data_and_submit_form(self):
        self.auth_page.auth_with_github()
        self.submit_salary_page.submit_salary("Endava", "Ljubljana", "Android Developer", "Junior", "1300", "1800")

    @pytest.mark.smoke
    @pytest.mark.salary
    @pytest.mark.skip(reason="unfinished")
    def test_average_salary(self):
        self.salaries_page.check_avg_salary()
