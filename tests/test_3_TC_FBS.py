from time import sleep

import allure
import logging
from playwright.sync_api import Page, expect

url = 'https://pizzeria.skillbox.cc/'


@allure.feature('Флоу с бонусной системой')
@allure.title('Тест Кейс №1')
def test_case_001(page: Page):
    with allure.step('Переход на страницу по ссылке'):
        logging.info('Переход на страницу по ссылке')
        page.goto(url)
    with allure.step('Переход в бонусную программу'):
        page.locator("#menu-item-363").get_by_role(
            "link", name="Бонусная программа"
        ).click()
    with allure.step('Ввод данных для бонусной программы'):
        page.locator("#bonus_username").fill("9+)ЬЮбж+%RWsf0")
        page.screenshot(path='screenshot/3_TC_FBS_001_AFP-12.png', full_page=True)
        page.locator("#bonus_username").fill("Mirage")

        page.locator("#bonus_phone").fill("79998887766")
        page.screenshot(path='screenshot/3_TC_FBS_001_AFP-13.png', full_page=True)
        page.locator("#bonus_phone").fill("+79998887766")
        page.screenshot(path='screenshot/3_TC_FBS_001_AFP-14.png', full_page=True)
    with allure.step('Клик на кнопку оформления в бонусной программе'):
        page.get_by_role("button", name="Оформить карту").click()
    with allure.step('Проверка оформления в бонусной программе'):
        sleep(7)
        expect(page.locator("h3")).to_contain_text("Ваша карта оформлена!")
        page.screenshot(path='screenshot/3_TC_FBS_001_AFP-16.png', full_page=True)
    with allure.step('Повторная регистрация'):
        page.locator("#menu-item-363").get_by_role(
            "link", name="Бонусная программа"
        ).click()
        page.locator("#bonus_username").fill("Mirage")
        page.locator("#bonus_phone").fill("+79998887766")
        page.screenshot(path='screenshot/3_TC_FBS_001_AFP-15.png', full_page=True)
        page.get_by_role("button", name="Оформить карту").click()
        sleep(7)
        expect(page.locator("h3")).to_contain_text("Ваша карта оформлена!")
