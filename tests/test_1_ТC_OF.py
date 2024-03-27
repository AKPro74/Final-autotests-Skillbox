from time import sleep

import allure
import pytest
from playwright.sync_api import Page, expect


url = 'https://pizzeria.skillbox.cc/'
pizza_4in1 = 'Пицца «4 в 1»'
pizza_grandma = 'Пицца «Как у бабушки»'
pizza_heaven = 'Пицца «Рай»'
pizza_hamMush = 'Пицца «Ветчина и грибы»'
pizza_pepperoni = 'Пицца «Пепперони»'
list_pizza = [
    'Пицца "4 в 1"',
    'Пицца "Рай"',
    'Пицца "Пепперони"',
    'Пицца "Ветчина и грибы"',
    'Пицца "Как у бабушки"',
]


@allure.feature('Основной флоу')
@allure.title('Тест Кейс №1')
def test_case_001(page: Page):
    page.goto(url)

    assert page.title() == 'Pizzeria — Пиццерия'

    expect(page).to_have_title("Pizzeria — Пиццерия")


@allure.title('Тест Кейс №2')
def test_case_002(page: Page):
    page.goto(url)

    expect(
        page.get_by_text(
            "Пицца В корзину Пицца «Как у бабушки» 480,00₽ В корзину Пицца «Рай» 515,00"
        )
    ).to_be_visible()


@allure.title('Тест Кейс №3')
def test_case_003(page: Page):
    page.goto(url)
    expect(page.locator("#accesspress_store_product-5")).to_contain_text("В корзину")


@allure.title('Тест Кейс №4')
def test_case_004(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    page.get_by_role("link", name="Add “Пицца \"Рай\"” to your cart").click()
    page.get_by_role("link", name=" [ 950,00₽ ]").click()
    expect(page.locator("#post-20")).to_contain_text("Пицца \"4 в 1\"")
    expect(page.locator("#post-20")).to_contain_text("Пицца \"Рай\"")


@allure.title('Тест Кейс №5')
def test_case_005(page: Page):
    page.goto(url)

    page.mouse.move(600, 600)
    page.get_by_label("next").click()
    page.get_by_label("previous").click()
    page.get_by_label("previous").click()
    page.get_by_label("previous").click()
    expect(page.get_by_label("next")).to_be_visible()
    expect(page.get_by_label("previous")).to_be_visible()


@allure.title('Тест Кейс №6')
def test_case_006(page: Page):
    page.goto(url)
    page.get_by_role("link", name=pizza_grandma, exact=True).click()

    assert page.title() == 'Пицца «Как у бабушки» — Pizzeria'

    expect(page).to_have_title("Пицца «Как у бабушки» — Pizzeria")


@allure.title('Тест Кейс №7')
def test_case_007(page: Page):
    page.goto(url)
    page.get_by_role("link", name=pizza_grandma, exact=True).click()
    page.get_by_label("Выбор борта для пиццы *").select_option("65.00")
    page.get_by_role("button", name="В корзину").click()
    page.get_by_role("link", name=" [ 545,00₽ ]").click()

    expect(page.get_by_role("definition")).to_contain_text("Колбасный борт")


@allure.title('Тест Кейс №8')
def test_case_008(page: Page):
    page.goto(url)
    page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()

    assert page.title() == 'Корзина — Pizzeria'

    expect(page).to_have_title("Корзина — Pizzeria")


@allure.title('Тест Кейс №9')
def test_case_009(page: Page):
    page.goto(url)
    page.get_by_role("link", name=" [ 0,00₽ ]").click()

    assert page.title() == 'Корзина — Pizzeria'

    expect(page).to_have_title("Корзина — Pizzeria")


@allure.title('Тест Кейс №10')
def test_case_010(page: Page):
    page.goto(url)
    page.locator("#pages-2").get_by_role("link", name="Корзина").click()

    assert page.title() == 'Корзина — Pizzeria'

    expect(page).to_have_title("Корзина — Pizzeria")


@allure.title('Тест Кейс №11')
def test_case_011(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    page.get_by_role("link", name="Add “Пицца \"Рай\"” to your cart").click()
    page.get_by_label("next").click()
    page.get_by_role("link", name="Add “Пицца \"Пепперони\"” to").click()
    page.get_by_role(
        "link", name="Add “Пицца \"Ветчина и грибы\"” to your cart"
    ).click()
    page.get_by_role("link", name="Пицца «Как у бабушки»", exact=True).click()
    page.get_by_label("Выбор борта для пиццы *").select_option("65.00")
    page.get_by_role("button", name="В корзину").click()
    page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()

    for i in range(0, len(list_pizza)):
        assert page.locator(f"//tr[{i + 1}]/td[3]/a").text_content() == list_pizza[i]


@allure.title('Тест Кейс №12')
def test_case_012(page: Page):
    page.goto(url)
    page.mouse.move(600, 600)
    page.get_by_label("next").click()
    page.get_by_role("link", name="Add “Пицца \"Пепперони\"” to").click()
    page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()
    page.get_by_label("Пицца \"Пепперони\" quantity").click()
    page.get_by_label("Пицца \"Пепперони\" quantity").fill("5")
    page.get_by_role("button", name="Обновить корзину").click()

    expect(page.get_by_label("Пицца \"Пепперони\" quantity")).to_have_value("5")


@allure.title('Тест Кейс №13')
def test_case_013(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Add “Пицца \"Как у бабушки\"”").click()
    page.get_by_role("link", name=" [ 480,00₽ ]").click()
    page.get_by_label("Remove this item").click()

    expect(page.locator("#post-20")).to_contain_text("Корзина пуста.")

    expect(page.get_by_role("alert")).to_contain_text(
        "“Пицца \"Как у бабушки\"” удален. Вернуть?"
    )


@allure.title('Тест Кейс №14')
def test_case_014(page: Page):
    page.goto(url)
    page.locator("#menu-item-389").hover()
    page.get_by_role("link", name="Десерты").click()

    assert page.title() == 'Десерты — Pizzeria'

    expect(page).to_have_title("Десерты — Pizzeria")


# @pytest.mark.skip(reason="Не знаю как сместить ползунок")


@allure.title('Тест Кейс №15')
def test_case_015(page: Page):
    page.goto(url)
    page.locator("#menu-item-389").hover()
    page.get_by_role("link", name="Десерты").click()
    page.locator('(//div[1]/span[2])[1]').hover()
    page.mouse.down()
    page.mouse.move(-0, 0)
    page.mouse.up()

    page.screenshot(path='screenshot/1_TC_OF_015_AFP-3.png', full_page=True)

    page.get_by_role("button", name="Применить").click()


@pytest.mark.skip(reason="Не знаю как сместить ползунок")
@allure.title('Тест Кейс №16')
def test_case_016(page: Page):
    page.goto(url)
    page.locator("#menu-item-389").hover()
    page.get_by_role("link", name="Десерты").click()
    page.locator('(//div[1]/span[2])[1]').hover()
    page.mouse.down()
    page.mouse.move(-0, 0)
    page.mouse.up()
    page.get_by_role("button", name="Применить").click()
    page.get_by_label("Add “Десерт \"Морковный каприз\"” to your cart").click()
    page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()

    expect(page.locator("#post-20")).to_contain_text("Десерт \"Морковный каприз\"")


@allure.title('Тест Кейс №17')
def test_case_017(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    page.get_by_role("link", name="Add “Пицца \"Рай\"” to your cart").click()
    page.get_by_label("next").click()
    page.get_by_role("link", name="Add “Пицца \"Пепперони\"” to").click()
    page.get_by_role(
        "link", name="Add “Пицца \"Ветчина и грибы\"” to your cart"
    ).click()
    page.locator("#menu-item-389").hover()
    page.get_by_role("link", name="Десерты").click()
    page.get_by_label("Add “Десерт \"Морковный каприз\"” to your cart").click()
    page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()
    page.get_by_label("Пицца \"Пепперони\" quantity").click()
    page.get_by_label("Пицца \"Пепперони\" quantity").fill("5")
    page.get_by_role("button", name="Обновить корзину").click()
    page.get_by_role("link", name="ПЕРЕЙТИ К ОПЛАТЕ").click()

    assert page.title() == 'Оформление заказа — Pizzeria'

    expect(page).to_have_title("Оформление заказа — Pizzeria")


@allure.title('Тест Кейс №18')
def test_case_018(page: Page):
    page.goto(url)
    page.locator("#menu-item-31").get_by_role("link", name="Оформление заказа").click()
    page.get_by_role("link", name="Назад в магазин").click()
    page.get_by_label("Add “Айс латте” to your cart").click()
    page.get_by_label("Add “Десерт \"Морковный каприз\"” to your cart").click()
    page.locator("#menu-item-31").get_by_role("link", name="Оформление заказа").click()
    page.screenshot(path='screenshot/1_TC_OF_018_AFP-4.png', full_page=True)


@allure.title('Тест Кейс №19')
def test_case_019(page: Page):
    page.goto(url)
    page.locator("#menu-item-30").get_by_role("link", name="Мой аккаунт").click()
    page.get_by_role("button", name="Зарегистрироваться").click()
    page.get_by_label("Имя пользователя *").fill('Mirage31')
    page.get_by_label("Адрес почты *").fill('mirage2031@mail.com')
    page.get_by_label("Пароль *").fill('Mir0102age2031')
    page.screenshot(path='screenshot/1_TC_OF_019_AFP-5.png', full_page=True)
    page.get_by_role("button", name="Зарегистрироваться").click()

    assert page.title() == 'Регистрация — Pizzeria'

    expect(page).to_have_title("Регистрация — Pizzeria")


@allure.title('Тест Кейс №20')
def test_case_020(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Add “Пицца \"4 в 1\"” to your").click()
    page.get_by_role("link", name="Add “Пицца \"Рай\"” to your cart").click()
    page.get_by_label("next").click()
    page.get_by_role("link", name="Add “Пицца \"Пепперони\"” to").click()
    page.get_by_role(
        "link", name="Add “Пицца \"Ветчина и грибы\"” to your cart"
    ).click()
    page.locator("#menu-item-389").hover()
    page.get_by_role("link", name="Десерты").click()
    page.get_by_label("Add “Десерт \"Морковный каприз\"” to your cart").click()
    page.locator("#menu-item-29").get_by_role("link", name="Корзина").click()
    page.get_by_label("Пицца \"Пепперони\" quantity").click()
    page.get_by_label("Пицца \"Пепперони\" quantity").fill("5")
    page.get_by_role("button", name="Обновить корзину").click()
    page.get_by_role("link", name="ПЕРЕЙТИ К ОПЛАТЕ").click()
    page.get_by_role("link", name="Авторизуйтесь").click()
    page.get_by_label("Имя пользователя или почта *").click()
    page.get_by_label("Имя пользователя или почта *").fill("Mirage26")
    page.get_by_label("Пароль *").click()
    page.get_by_label("Пароль *").fill("Mir0102age2026")
    page.get_by_role("button", name="Войти").click()

    assert page.title() == 'Оформление заказа — Pizzeria'

    expect(page).to_have_title("Оформление заказа — Pizzeria")

    page.get_by_label("Имя *").fill("Мира")
    page.get_by_label("Фамилия *").fill("Агге")
    page.get_by_label("Russia").click()
    page.get_by_role("option", name="Russia").click()
    page.get_by_placeholder("Улица и номер дома").fill("ул. Строителей, д.135, кв. 24")
    page.get_by_label("Город / Населенный пункт *").fill("Махачкала")
    page.get_by_label("Область *").fill("Турецкая")
    page.get_by_label("Почтовый индекс *").fill("122024")

    page.get_by_label("Телефон *").fill("89998887766")
    page.screenshot(path='screenshot/1_TC_OF_020_AFP-7.png', full_page=True)

    page.get_by_label("Дата заказа (дополнительно)").fill("2024-03-11")
    page.screenshot(path='screenshot/1_TC_OF_020_AFP-6.png', full_page=True)

    page.get_by_label("Дата заказа (дополнительно)").fill("2024-03-20")
    page.get_by_placeholder("Здесь вы можете оставить комментарии к заказу").fill(
        "Привет от трудящихся"
    )

    page.get_by_role("button", name="Оформить заказ").click()
    sleep(2)
    page.screenshot(path='screenshot/1_TC_OF_020_AFP-8.png', full_page=True)

    page.get_by_label("I have read and agree to the").check()
    sleep(2)
    page.get_by_role("button", name="Оформить заказ").click()

    expect(page.locator("#post-24")).to_contain_text("Заказ получен")
