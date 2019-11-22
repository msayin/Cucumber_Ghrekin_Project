"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""

from selenium import webdriver


def go_to(url, browser_type=None):
    """
    Function to start instance of the specified browser and navigate to the specified url.

    :param url: the url to navigate to
    :param browser_type: the type of browser to start (Default is Firefox)

    :return: driver: browser instance
    """
    if not browser_type:
        # create instance of Firefox driver the browser type is not specified
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        # create instance of the Chrome driver
        driver = webdriver.Chrome()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to the url
    url = url.strip()
    url = 'https://' + url
    driver.get(url)

    return driver


def assert_page_title(context, expected_title):
    """
    Function to assert title of current page.
    :param expected_title:
    :param context:
    """

    actual_title = context.driver.title

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected.")


def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context:
    :param expected_url:
    """

    # get the current url
    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print("The page url is as expected.")
