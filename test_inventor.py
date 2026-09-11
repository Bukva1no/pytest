from playwright.sync_api import Page, expect
from conftest import login, InventoryPage

import pytest


def test_inventory_page_has_six_products(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    count = inventory_page.get_product_count()
    assert count == 6