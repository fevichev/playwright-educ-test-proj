import pytest
from playwright.sync_api import sync_playwright
from page_object.application import App
import settings
from page_object.challenging_dom import Dom
from page_object.context_menu import ContextMenu
import page_object.dropdown
from page_object.dynamic_control import DynamicControl
from page_object.dynamic_loading import DynamicLoading
from page_object.entry_ad import EntryAd
from page_object.popup_alerts import PopUpAlerts
from page_object.drug_drop import DrugDrop


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


#
# @fixture
# def work_browser(get_playwright):
#     base_class = BaseClass(get_playwright, base_url=settings.BASE_URL)
#     yield base_class


@pytest.fixture
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    yield app
    app.close()


@pytest.fixture
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto('/login')
    app.login('alice', 'Qamania123')
    yield app


@pytest.fixture
def dom_page(get_playwright):
    dom = Dom(get_playwright, base_url=settings.BASE_URL)
    yield dom
    dom.close()


@pytest.fixture
def context_menu_page(get_playwright):
    context_menu = ContextMenu(get_playwright, base_url=settings.BASE_URL)
    yield context_menu
    context_menu.close()


@pytest.fixture
def popup_alerts(get_playwright):
    popup_alerts = PopUpAlerts(get_playwright, base_url=settings.BASE_URL)
    yield popup_alerts
    popup_alerts.close()


@pytest.fixture
def drug_drop(get_playwright):
    drug_drop = DrugDrop(get_playwright, base_url=settings.BASE_URL)
    yield drug_drop
    drug_drop.close()


@pytest.fixture
def dropdown(get_playwright):
    dropdown = page_object.dropdown.Dropdown(get_playwright, base_url=settings.BASE_URL)
    yield dropdown
    dropdown.close()


@pytest.fixture
def dynamic_control(get_playwright):
    dynamic_control = DynamicControl(get_playwright, base_url=settings.BASE_URL)
    yield dynamic_control
    dynamic_control.close()


@pytest.fixture
def dynamic_loading(get_playwright):
    dynamic_loading = DynamicLoading(get_playwright, base_url=settings.BASE_URL)
    yield dynamic_loading
    dynamic_loading.close()


@pytest.fixture
def entry_ad(get_playwright):
    entry_ad = EntryAd(get_playwright, base_url=settings.BASE_URL)
    yield entry_ad
    entry_ad.close()
