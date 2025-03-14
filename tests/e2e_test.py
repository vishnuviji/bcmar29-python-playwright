import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.confirmation_page import ConfirmationPage

@pytest.mark.parametrize("username, password, first_name, last_name, postal_code", [
    ("standard_user", "secret_sauce", "John", "Doe", "45678")
])
def test_order_single_product(page: Page, username: str, password: str, first_name: str, last_name: str, postal_code: str):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    confirmation_page = ConfirmationPage(page)

    login_page.open()
    login_page.login(username, password)
    products_page.add_to_cart()
    products_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_details(first_name, last_name, postal_code)
    overview_page.finish()
    confirmation_page.verify_order_completion()

@pytest.mark.parametrize("username, password, first_name, last_name, postal_code", [
    ("standard_user", "secret_sauce", "John", "Doe", "45678")
])
def test_order_two_products(page: Page, username: str, password: str, first_name: str, last_name: str, postal_code: str):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    confirmation_page = ConfirmationPage(page)

    login_page.open()
    login_page.login(username, password)
    products_page.add_two_to_cart()
    products_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_details(first_name, last_name, postal_code)
    overview_page.finish()
    confirmation_page.verify_order_completion()