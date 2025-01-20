from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.links = {
            '[ О нас ]': '#about',
            '[ Услуги ]': '#moreinfo',
            '[ Проекты ]': '#cases',
            '[ Отзывы ]': '#Reviews',
            '[ Контакты ]': '#contacts',
            'Выбрать специалиста': '#specialists'
        }

    def open_main_page(self):
        """Открывает главную страницу сайта"""
        self.page.goto('https://effective-mobile.ru/')

    def click_link(self, link_name):
        """Кликает по ссылке на указанную секцию."""
        if link_name in self.links:
            selector = f'text={link_name}'  # Используем текстовый селектор
            # Прокручиваем в область видимости
            self.page.locator(selector).scroll_into_view_if_needed()
            self.page.locator(selector).click()  # Кликаем по ссылке

    def click_logo(self):
        """Кликает по логотипу."""
        self.page.locator('#rec573054532').get_by_role(
            'link', name='Effective Mobile'
            ).click()
