from playwright.sync_api import Page, expect

class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_order_completion(self):
        expect(self.page.locator('[data-test="complete-header"]')).to_contain_text("Thank you for your order!")