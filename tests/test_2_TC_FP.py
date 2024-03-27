import logging
from time import sleep

import allure
from playwright.sync_api import Page, expect

url = 'http://pizzeria.skillbox.cc/'


@allure.feature('Флоу с промокодом')
@allure.title('Тест Кейс №1')
def test_case_001(page: Page):
    with allure.step('Переход на страницу по ссылке'):
        logging.info('Переход на страницу по ссылке')
        page.goto(url)
    with allure.step('Добавляем пиццу в корзину'):
        page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    with allure.step('Переходим в корзину'):
        page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()
    with allure.step('Применяем купон на скидку'):
        page.get_by_placeholder("Введите код купона").fill("GIVEMEHALYAVA")
        page.get_by_role("button", name="Применить купон").click()
    with allure.step('Скриншот результата тест-кейса'):
        page.screenshot(path='screenshot/2_TC_FP_001_AFP-10.png', full_page=True)
    with allure.step('Проверка применения купона на скидку'):
        inner_text = float(
            page.locator('//td[4]/span/bdi')
            .inner_text()
            .replace("₽", "")
            .replace(",", ".")
        )
        discount = float(
            page.locator('//tr[2]/td/span')
            .inner_text()
            .replace("₽", "")
            .replace(",", ".")
        )
        summ = float(
            page.locator('//strong/span/bdi')
            .inner_text()
            .replace("₽", "")
            .replace(",", ".")
        )
        assert inner_text - discount == summ

        expect(page.locator('(//td/span/bdi)[1]')).to_contain_text('435,00₽')


@allure.title('Тест Кейс №2')
def test_case_002(page: Page):
    with allure.step('Переход на страницу по ссылке'):
        page.goto(url)
    with allure.step('Добавляем пиццу в корзину'):
        page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    with allure.step('Авторизуемся в личном кабинете'):
        page.locator("#menu-item-30").get_by_role("link", name="Мой аккаунт").click()
        page.get_by_label("Имя пользователя или почта *").fill("Mirage26")
        page.get_by_label("Пароль *").fill("Mir0102age2026")
        page.get_by_role("button", name="Войти").click()
    with allure.step('Переходим в корзину'):
        page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()
    with allure.step('Применяем купон на скидку'):
        page.get_by_placeholder("Введите код купона").fill("DC120")
        page.get_by_role("button", name="Применить купон").click()
    with allure.step('Проверка применения купона'):
        expect(page.locator('//*[@id="post-20"]')).to_contain_text('Неверный купон.')


@allure.title('Тест Кейс №3')
def test_case_003(page: Page):
    with allure.step('Переход на страницу по ссылке'):
        page.goto(url)
    with allure.step('Добавляем пиццу в корзину'):
        page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    with allure.step('Авторизуемся в личном кабинете'):
        page.locator("#menu-item-30").get_by_role("link", name="Мой аккаунт").click()
        page.get_by_label("Имя пользователя или почта *").fill("Mirage26")
        page.get_by_label("Пароль *").fill("Mir0102age2026")
        page.get_by_role("button", name="Войти").click()
    with allure.step('Переходим в корзину'):
        page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()
    with allure.step('Блокировка ссылки на активацию промо-кода'):
        page.route("**/?wc-ajax=apply_coupon", lambda route: route.abort())
    with allure.step('Применяем купон на скидку'):
        page.get_by_placeholder("Введите код купона").fill("GIVEMEHALYAVA")
        page.get_by_role("button", name="Применить купон").click()
    with allure.step('Скриншот результата тест-кейса'):
        page.screenshot(path='screenshot/2_TC_FP_003_AFP-11.png', full_page=True)
