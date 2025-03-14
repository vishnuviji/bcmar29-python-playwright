from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def add_two_to_cart(self):
        self.add_to_cart()
        self.page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    def go_to_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()