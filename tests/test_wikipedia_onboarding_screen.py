from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure
from allure import step

@allure.story('Search')
@allure.severity(allure.severity_level.NORMAL)
@allure.tag('Mobile')
def test_skip_pages():
    with step('Проверка первой страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages'))
    with step('Проверка второй страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
    with step('Проверка третьей страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
    with step('Проверка четвёртой страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))