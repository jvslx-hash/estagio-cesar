from selenium.webdriver.common.by import By
import time

def test_fill_text_box_form_and_validate(driver):
    driver.get("https://demoqa.com/text-box")

    full_name_input = driver.find_element(By.ID, "userName")
    email_input = driver.find_element(By.ID, "userEmail")
    current_address_input = driver.find_element(By.ID, "currentAddress")
    permanent_address_input = driver.find_element(By.ID, "permanentAddress")
    submit_button = driver.find_element(By.ID, "submit")

    full_name = "jose vitu"
    email = "jvslx@gmail.com"
    current_address = "rua 1"
    permanent_address = "do lado da rua 2" 

    full_name_input.send_keys(full_name)
    email_input.send_keys(email)    
    current_address_input.send_keys(current_address)
    permanent_address_input.send_keys(permanent_address)  
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    

    output_name = driver.find_element(By.ID, "name")
    output_email = driver.find_element(By.ID, "email")
    output_current_address = driver.find_element(By.CSS_SELECTOR, "p#currentAddress")
    output_permanent_address = driver.find_element(By.CSS_SELECTOR, "p#permanentAddress")

    assert full_name in output_name.text
    assert email in output_email.text
    assert current_address in output_current_address.text
    assert permanent_address in output_permanent_address.text
    time.sleep(3)


    
    
