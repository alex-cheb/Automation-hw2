# -*- coding: utf-8 -*-

# have Geckodriver of Chrome driver predifined in path

from selenium import webdriver
page = "https://anotepad.com"
note = {"title":"My First Note", "content": "Lorem ipsum \n dolor sit amet"}
note_created = "You have saved your note as a Guest User. You can come back at anytime to continue editing"
note_deleted = "No note here."
driver = webdriver.Firefox()
driver.get(page)


def check_creation(text):
    element = driver.find_element_by_xpath("//p[@class = 'alert alert-warning']").text
    assert text in element

def check_delete(text):
    element = driver.find_element_by_xpath("//ul[@id ='savedNotes']/div").text
    assert text in element

def create_note(data):
    #global note_link
    driver.find_element_by_id("edit_title").send_keys(data["title"])
    driver.find_element_by_id("edit_textarea").send_keys(data["content"])
    driver.find_element_by_id('btnSaveNote').click()
    wait = WebDriverWait(driver, 10)
    check_creation(note_created)
    print("Passed")
    #note_link = driver.current_url
    #return note_link

def delete_note():
    #driver.get(link)
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver.find_element_by_xpath("//a[@class = 'delete']").click()
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    driver.get(page)
    check_delete(note_deleted)
    print("Passed")
    
create_note(note)
delete_note()