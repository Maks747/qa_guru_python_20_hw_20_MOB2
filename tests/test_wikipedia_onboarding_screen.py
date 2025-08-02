from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure
from allure import step


@allure.story('Search')
@allure.tag('Mobile')
@allure.feature('Поиск в википедии текста "Appium"')
def test_search_wikipedia_appium():
    with step('Type search in Wikipedia'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.story('Search')
@allure.tag('Mobile')
@allure.feature('Поиск в википедии текста "Cars')
def test_search_wikipedia_car():
    with step('Type search in Wikipedia'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Car')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Car'))

    with step('Click an item'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

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