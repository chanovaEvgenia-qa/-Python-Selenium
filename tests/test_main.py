"""
Test smoke
"""
from selenium.webdriver.common.by import By

URL = "https://postcard.qa.studio/"


def test_smoke(browser):
    """
    SMK-1. Smoke test
    """
    browser.get(URL)
    element = browser.find_element(by=By.ID, value="send")

    assert element.text == "Отправить", "Unexpected text on button"

def test_emply_click_send(browser):# проверка, что цвет текста меняется на красный и приходит ошибка при незаполненной форме
    """
    SMK-2. Smoke test
    """
    browser.get(URL)# команда браузеру открыть УРЛ
    email_el = browser.find_element(by=By.CSS_SELECTOR, value="div.email h2")# нашли элемент div.email h2
    email_text = email_el.get_attribute("class")# запрос значение атрибута class
    assert email_text == "requered", "Unexpected class for email label" # проверка, что этот атрибут requered

    element = browser.find_element(by=By.ID, value="send")# нашли элемент кнопки
    element.click()# кликнули по нему

    email_text = email_el.get_attribute("class")# проверили атрибут лейбла
    assert email_text == "requered error", "Unexpected class for email label"# убедились, что изменился на requered error


def test_send_postcard(browser):#
    """
    SMK-3. Positive case
    """
    browser.get(URL)# 
    email_input = browser.find_element(by=By.ID, value="email")# находим инпут ID
    email_input.click()# клик по нему
    email_input.send_keys("evgenia.chanova@gmail.com")# ввод текста

    cards = browser.find_elements(by=By.CSS_SELECTOR, value='[class="photo-input__photo-parent"]')# нашли несколько элементов и обратились к одному
    cards[0].click()# кликнули по нему

    message_input = browser.find_element(by=By.ID, value="textarea")#нашли сообщение в инпуте textarea-id элемента
    message_input.click()# кликнули по нему
    message_input.send_keys("Hello, world!")# написали Hello, world

    button = browser.find_element(by=By.ID, value="send")#нашли элемент кнопку, button "Отправить"
    button.click()#кликнула

    modal = browser.find_element(by=By.ID, value="modal")#нашли модальное окно, id modal

    assert modal.text == "Открытка успешно отправлена!", "Unexpected modal message"# убедились, текст в modal верный,  что изменился на requered error