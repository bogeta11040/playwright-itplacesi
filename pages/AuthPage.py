import pytest

import credentials

from playwright.sync_api import Page

class AuthPage:
    def __init__(self, page: Page):
        self.page = page

    def auth_with_github(self):
        if credentials.githubuser == "" or credentials.githubpass == "":
          pytest.xfail("CONFIGURATION ISSUE: No credentials added to credentials.py file.")
        self.page.goto("./vnos.php")
        self.page.get_by_role("link", name=" | Prijavite se s GitHub računom").click()
        self.page.get_by_label("Username").click()
        self.page.get_by_label("Username").fill(credentials.githubuser)
        self.page.get_by_label("Password").click()
        self.page.get_by_label("Password").fill(credentials.githubpass)
        self.page.get_by_role("button", name="Sign in").click()
        self.page.wait_for_url("./vnos.php")
        print(f"Authorized with GitHub.")

    def auth_with_linkedin(self):
        if credentials.linkedinuser == "" or credentials.linkedinpass == "":
          pytest.xfail("CONFIGURATION ISSUE: No credentials added to credentials.py file.")
        self.page.goto("./vnos.php")
        self.page.get_by_role("link", name=" | Prijavite se s LinkedIn računom").click()
        self.page.get_by_label("Email or Phone").click()
        self.page.get_by_label("Email or Phone").fill(credentials.linkedinuser)
        self.page.get_by_label("Password").click()
        self.page.get_by_label("Password").fill(credentials.linkedinpass)
        self.page.get_by_role("button", name="Sign in").click()
        self.page.wait_for_url("./vnos.php")
        print(f"Authorized with LinkedIn.")