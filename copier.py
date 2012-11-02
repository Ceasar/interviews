"""
Script to copy contents of a local file to a DOM element in the browser.

# Motivation

Using this tool will allow people to user their favorite text editor and command
line tools to edit code, while still being able to share it with an interviewer.
This is particularly useful because it means a person can test his or her code,
rather than having to simulate the program in his or her head.

# Method

Uses Selenium to drive the browser and easywatch to monitor changes. Selenium is
perhaps not the best tool here as javascript in general should suffice.

# Progress

Currently tested with collabedit. Doesn't work particularly well as collabedit
autoindents text which screws up the driver as it types in the contents of a
file for you. It doesn't help much either that collabedit uses an iframe as
their textarea.

"""
import re
import time

import easywatch
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


def main():
    try:
        driver = webdriver.Firefox()
        driver.get("http://collabedit.com/fsbee")
        alert = driver.switch_to_alert()
        alert.accept()
        print "loaded %s..." % driver.current_url
        time.sleep(2)
        driver.switch_to_frame("frame_the_input")
        elem = driver.find_element_by_css_selector("textarea")

        def handler(event_type, src_path):
            if event_type == "modified":
                elem.clear()
                time.sleep(1)
                with open(src_path) as f:
                    contents = f.read()
                    # collabedit screws this up with automatic indentation
                    # possible solution is to copy paste?
                    # collabedit uses an iframe, so javascript probably won't work
                    # elem.send_keys(contents)
                    driver.execute_script("$('textarea').text(%s)" %
                                          re.escape(contents))
                    print contents
        easywatch.watch(".", handler)
    finally:
        driver.close()

if __name__ == "__main__":
    main()
