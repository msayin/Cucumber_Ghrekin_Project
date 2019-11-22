
from behave import given, when, then
from BDDCommon.CommonFuncs import webcommon

# start of step definitions

@given('I go to the site "{url}"')
def go_to_url(context, url):
    """
    Step definition to go to the specified url.
    :param context:
    :param url:
    """
    print("Navigating to the site: {}".format(url))
    # import pdb; pdb.set_trace()
    context.driver = webcommon.go_to(url)

#========================================================================================#
@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies the home page title is as expected.
    :param context:
    :param expected_title:
    :return:
    """

    webcommon.assert_page_title(context, expected_title)

#========================================================================================#
@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    """
    Verifies the current uls is as expected_url
    :param context:
    :param expected_url:
    """

    webcommon.assert_current_url(context, expected_url)