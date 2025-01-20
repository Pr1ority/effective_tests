from pages.main_page import MainPage
from playwright.sync_api import expect
import allure
import pytest


@pytest.mark.parametrize('link_text,anchor', [
    ('[ О нас ]', '#about'),
    ('[ Услуги ]', '#moreinfo'),
    ('[ Проекты ]', '#cases'),
    ('[ Отзывы ]', '#Reviews'),
    ('[ Контакты ]', '#contacts'),
    ('Выбрать специалиста', '#specialists')
])
@allure.feature('Навигация по сайту')
def test_navigation(page, link_text, anchor):

    # Инициализация главной страницы
    main_page = MainPage(page)

    # Открытие главной страницы
    main_page.open_main_page()

    with allure.step(f'Проверяем, что ссылка "{link_text}" существует'):
        selector = f'text={link_text}'
        # Проверяем, что ссылка доступна для клика
        expect(page.locator(selector)).to_be_visible()

    with allure.step(f'Кликаем по ссылке: {link_text}'):
        main_page.click_link(link_text)

    with allure.step(f'Проверяем, что URL изменился на: {anchor}'):
        expected_url = f'https://effective-mobile.ru/{anchor}'
        expect(page).to_have_url(expected_url)


@allure.feature('Навигация на секцию #main')
def test_logo_navigation(page):
    main_page = MainPage(page)
    main_page.open_main_page()

    with allure.step('Кликаем на логотип'):
        main_page.click_logo()

    with allure.step('Проверяем URL'):
        expect(page).to_have_url('https://effective-mobile.ru/#main')
