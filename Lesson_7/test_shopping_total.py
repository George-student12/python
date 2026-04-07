from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.authorisation import Authorisation


def test_shopping_total():
    driver = (webdriver.Firefox
              (service=FirefoxService(GeckoDriverManager().install())))

    try:
        login_page = Authorisation(driver)
        inventory_page = (login_page.open().login
                          ("standard_user", "secret_sauce"))

        inventory_page.wait_for_inventory_loaded()

        items = [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie"
        ]
        inventory_page.add_items(items)

        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()

        (checkout_page
         .fill_customer_info("Егор", "Морозов", "101010")
         .click_continue()
         .verify_total("Total: $58.29"))

        print("Тест пройден: Стоимость товаров соответствует 58.29$.")

    except Exception as e:
        print(f"Тест упал с ошибкой: {e}")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_total()
