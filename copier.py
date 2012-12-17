"""
Script to copy contents of a local file to a DOM element in the browser.

# Motivation

Using this tool will allow people to user their favorite text editor and
command line tools to edit code, while still being able to share it with an
interviewer.

This is particularly useful because it means a person can test his or her code,
rather than having to simulate the program in his or her head.

# Method

Uses Selenium to drive the browser and easywatch to monitor changes. Selenium
is perhaps not the best tool here as javascript in general should suffice.

"""
import sys

import easywatch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def collabedit(driver):
    """Build a copier for collabedit.

    Collabedit has an annoying alert to get the person's name.
    I just dismiss it.

    There is a problem with exclamation marks when it is copied.
    Unclear what the problem is exactly.
    """
    # kill the alert
    print "killing alert..."
    driver.switch_to_alert().dismiss()

    # grab the iframe
    driver.switch_to_frame("frame_the_input")

    elem = driver.find_element_by_css_selector("textarea")

    def handler(contents):
        elem.send_keys(Keys.COMMAND, 'a')
        elem.send_keys(Keys.BACK_SPACE)

        elem.send_keys(contents)
    return handler


def stypi(driver):
    """Build a copier for stypi.

    Stypi doesn't seem to usage a regular text area. They have a very
    tiny one that when you click the div that looks like the textarea puts
    your cursor there. Setting the text of the text area does nothing--
    Stypi watches for keystrokes I think. Also, since the textarea is just
    a dummy, there is no way to clear it with javascript. I resort to
    CMD+A to clear.

    Note, the copier only partially works.

    - If the language is not plain text, stypi will autoindent.
    - Selenium seems to have special codes with it does the send keys
        - Exclamation point will truncate every before
        - Left parents won't show
        - More?
    """
    elem = driver.find_element_by_css_selector("#editor textarea")

    def handler(contents):
        elem.send_keys(Keys.COMMAND, 'a')
        elem.send_keys(Keys.BACK_SPACE)

        elem.send_keys(contents)
    return handler


def get_handler(driver, domain):
    if "stypi" in domain:
        print "handling stypi..."
        return stypi(driver)
    elif "collabedit" in domain:
        print "handling collabedit..."
        return collabedit(driver)


# For whatever reason, Chrome cannot open collabedit, so we use Firefox
def get_driver(domain):
    """Get the appropriate driver for a website."""
    if "collabedit" in domain:
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()


def main(args):
    try:
        url = args[1]
        filename = args[2]
    except IndexError:
        raise ValueError("usage: python copier `url` `filename`")
    try:
        driver = get_driver(url)

        print "loading %s..." % url
        driver.execute_script('window.onbeforeunload = function() {}')
        driver.get(url)
        print "getting handler..."
        h = get_handler(driver, url)
        print "loaded %s..." % driver.current_url

        def handler(event_type, src_path):
            # TODO: filename in src_path might be a little insecure
            if event_type == "modified" and filename in src_path:
                with open(src_path) as f:
                    contents = f.read()
                    h(contents)
                    print contents
        print "watching for changes..."
        easywatch.watch(".", handler)
    finally:
        driver.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
