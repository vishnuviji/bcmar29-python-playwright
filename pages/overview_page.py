from playwright.sync_api import Page

class OverviewPage:
    def __init__(self, page: Page):
        self.page = page

    def finish(self):
        self.page.locator('[data-test="finish"]').click()