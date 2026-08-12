from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # ВАЖНО: Замените значения name и value на реальные cookie из ваших аккаунтов.
    # Обычно нужная cookie называется "session", "sessionid" или "auth".
    COOKIES_USER_1 = [
        {
            "name": "session",
            "value": "user1_cookie_value_from_browser",
            "domain": ".gitflic.ru",
            "path": "/"
        }
    ]

    COOKIES_USER_2 = [
        {
            "name": "session",
            "value": "user2_cookie_value_from_browser",
            "domain": ".gitflic.ru",
            "path": "/"
        }
    ]

    # Укажите реальные ссылки на профили пользователей
    PROFILE_URL_1 = "https://gitflic.ru/user/your_username1"
    PROFILE_URL_2 = "https://gitflic.ru/user/your_username2"

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # 2. Установите cookie пользователя 1
    for cookie in COOKIES_USER_1:
        driver.add_cookie(cookie)

    # 3. Обновите страницу
    driver.refresh()

    # 4. Перейдите на страницу пользователя 1
    driver.get(PROFILE_URL_1)

    # 5. Сохраните текущий URL
    url_user1 = driver.current_url

    # 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # 7. Установите cookie пользователя 2
    for cookie in COOKIES_USER_2:
        driver.add_cookie(cookie)

    # 8. Обновите страницу
    driver.refresh()

    # 9. Перейдите на страницу пользователя 2
    driver.get(PROFILE_URL_2)

    # 10. Сохраните текущий URL
    url_user2 = driver.current_url

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user1 != url_user2

    driver.quit()