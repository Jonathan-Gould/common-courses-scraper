from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import pickle


def find_people(driver):
    s = set()
    for i in driver.find_elements_by_tag_name("option"):
        p = True
        for j in ["site", "Normal", "Low", "High", "Role"]:
            if j in i.text:
                p = False
                break
        if p:
            s.add(i.text)
    return s


def get_classmates(netid="", password=""):
    """
    This does the whole scraping process.
    You can pass your netid and password if you don't want to type them.
    However, the 2FA has to be manual.
    """
    driver = webdriver.Firefox()
    driver.get("https://newclasses.nyu.edu/portal/site/")
    if netid:
        driver.find_element_by_id("netid").send_keys(netid)
    if password:
        driver.find_element_by_id("password").send_keys(password)
    if netid and password:
        driver.find_element_by_name("_eventId_proceed").click()
    input("Press enter here when you've completed the 2-factor authentication")
    d = {}
    for i in range(len(driver.find_elements_by_css_selector(".fav-sites-entry"))):
        print(i)
        driver.find_element_by_css_selector(".all-sites-label").click()
        e = driver.find_elements_by_css_selector(".fav-sites-entry")[i]
        course_title = e.text
        e.click()
        try:
            WebDriverWait(driver, 0.25).until(
                expected_conditions.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = driver.switch_to.alert
            alert.dismiss()
            print("alert accepted")
        except TimeoutException:
            pass
        try:
            e = driver.find_element_by_css_selector(".icon-sakai--sakai-messages")
        except:
            continue
        e.click()
        driver.find_element_by_css_selector(".firstToolBarItem").click()
        d[course_title] = find_people(driver)
    return d


def main():
    d = get_classmates()
    with open("classmates.pickle", "wb") as fhan:
        pickle.dump(d, fhan)


if __name__ == "__main__":
    main()
