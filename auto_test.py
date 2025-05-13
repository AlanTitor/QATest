from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Работа с браузером Chrome
driver = webdriver.Chrome()

# Переход по заданному URL
driver.get("https://example.com/")

# Есть ли строка Example в названии сайта
assert "Example" in driver.title

# Поиск нужного эллемента и клик на него
driver.find_element(By.CSS_SELECTOR, "a[href]").click()

# Ожидание перехода на другую страницу (3 секунды)
WebDriverWait(driver, 3).until(EC.url_to_be("https://www.iana.org/help/example-domains"))

# Проверка нужного сайта (Опцианально, можно убрать. Можно заменить кодом выше)
assert "https://www.iana.org/help/example-domains" ==  driver.current_url

# Завершение сессии
driver.quit()
