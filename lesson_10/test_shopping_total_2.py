import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.authorisation import Authorisation


@allure.title("Покупка товаров")
@allure.description("Проверка общей стоимости купленных товаров")
@allure.feature("Покупка")
@allure.severity(allure.severity_level.BLOCKER)
def test_shopping_total():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    try:
        with allure.step("Авторизоваться"):
            login_page = Authorisation(driver)
            inventory_page = (
                login_page.open()
                .login("standard_user")
            )

        with allure.step("Дождаться загрузки главной страницы"):
            inventory_page.wait_for_inventory_loaded()

        with allure.step(
            "Подготовить список товаров и добавить их в корзину"
        ):
            items = [
                "sauce-labs-backpack",
                "sauce-labs-bolt-t-shirt",
                "sauce-labs-onesie"
            ]
            inventory_page.add_items(items)

        with allure.step("Перейти в корзину"):
            cart_page = inventory_page.go_to_cart()

        with allure.step("Нажать кнопку 'Оформить заказ'"):
            checkout_page = cart_page.proceed_to_checkout()

        with allure.step("Заполнить информацию о покупателе"):
            (
                checkout_page
                .fill_customer_info("Егор", "Морозов", "101010")
                .click_continue()
                .verify_total("Total: $58.29")
            )

        print("Тест пройден: Стоимость товаров соответствует 58.29$.")

    except Exception as e:
        print(f"Тест упал с ошибкой: {e}")
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_total()
