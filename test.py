#..............Fuad Garibli................
#..............Yazılım Testi Ödevi 2.......
#..............G201210558..................
#..............Selenium Testleri...........
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome() 
wait = WebDriverWait(driver, 6)


def test_incorrect_login():  # yanlış logini test eder
    driver.get("http://127.0.0.1:3000")
    login_button_xpath = '//button[contains(@class, "action__btn-login") and contains(., "Login")]'
    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    email_input.send_keys("invalid@email.com")
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("invalidpass")
    login_button = driver.find_element(By.CSS_SELECTOR, ".login-popup__form button[type='submit']")
    login_button.click()
    time.sleep(3)
    login_button_xpath = '//button[contains(@class, "action__btn-login") and contains(., "Login")]'
    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
    assert "Invalid email or password." in error_message.text, "Test Case 1 succeeded: Incorrect error message"
    print("Test Case 1: Successful - Incorrect Login")

def test_existing_email():   #varolan emailin kayıt ettirilememsini testeder
    driver.get("http://127.0.0.1:3000")    
    time.sleep(3)
    login_button_xpath = '//button[contains(@class, "action__btn-login") and contains(., "Login")]'
    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()
    time.sleep(4)
    register_button = wait.until(EC.element_to_be_clickable((By.ID, "go-register")))
    register_button.click()
    time.sleep(4)
    register_email_input = driver.find_element(By.CSS_SELECTOR, "#register-popup input[name='email']")
    register_email_input.send_keys("admin@admin.com")
    register_password_input = driver.find_element(By.CSS_SELECTOR, "#register-popup input[name='password']")
    register_password_input.send_keys("admin")
    register_button = driver.find_element(By.CSS_SELECTOR, "#register-popup button[type='submit']")
    register_button.click()
    time.sleep(3)
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "action__btn-login")))
    login_button.click()
    time.sleep(3)
    registration_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-popup__form .alert.alert-danger")))
    assert "Email is already taken." in registration_message.text, "Test Case 2 succeeded: correct register message"
    print("Test Case 2: Successful - Registered email can not register")
    time.sleep(5)

def test_register(): # kayıt etme işlemlerini test eder

    driver.get("http://127.0.0.1:3000")    
    time.sleep(3)
    login_button_xpath = '//button[contains(@class, "action__btn-login") and contains(., "Login")]'
    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()
    time.sleep(4)
    register_button = wait.until(EC.element_to_be_clickable((By.ID, "go-register")))
    register_button.click()
    time.sleep(4)
    register_email_input = driver.find_element(By.CSS_SELECTOR, "#register-popup input[name='email']")
    register_email_input.send_keys("deneme@deneme.com")
    register_password_input = driver.find_element(By.CSS_SELECTOR, "#register-popup input[name='password']")
    register_password_input.send_keys("deneme")
    register_button = driver.find_element(By.CSS_SELECTOR, "#register-popup button[type='submit']")
    register_button.click()
    time.sleep(3)
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "action__btn-login")))
    login_button.click()
    time.sleep(3)
    registration_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-popup__form .alert.alert-danger")))
    assert "Registration successful." in registration_message.text, "Test Case 2 succeeded: correct register message"
    print("Test Case 3: Successful - Correct Registered email")
    time.sleep(5)
    
def test_correct_login(): # doğru logini test eder
    # login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "action__btn-login")))
    # login_button.click()
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("deneme@deneme.com")
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("deneme")
    login_button = driver.find_element(By.CSS_SELECTOR, ".login-popup__form button[type='submit']")
    login_button.click()
    time.sleep(3)
    user_email_text = driver.find_element(By.CSS_SELECTOR, ".action__btn-login span").text
    assert user_email_text in user_email_text
    print("Test Case 4: Successful - Correct Login ")

def test_industries(): # industry kısmını test eder
    driver.get("http://127.0.0.1:3000/industries/")
    time.sleep(2)
    assert "Consultative Approach On Emerging Technology" in driver.page_source
    print("Test Case 5: Successful - element found")

def test_add_industry(): # add industry kısmını test et
    driver.get("http://127.0.0.1:3000/industries/")
    time.sleep(3)
    add_industry_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn__primary')]")))
    add_industry_button.click()
    time.sleep(5)
    service_title_input = wait.until(EC.visibility_of_element_located((By.ID, "serviceTitle")))
    service_title_input.send_keys("New Service Title")
    service_description_input = driver.find_element(By.ID, "serviceDescription")
    service_description_input.send_keys("This is a service description that is written to be tested by Selenium Python testing robot")
    service_image_input = driver.find_element(By.ID, "serviceImage")
    service_image_input.send_keys("/static/images/service/1.jpg")
    service_link_input = driver.find_element(By.ID, "serviceLink")
    service_link_input.send_keys("http://127.0.0.1:3000/index/")
    time.sleep(5)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)
    assert "New Service Title" in driver.page_source
    print("Test Case 6: Successful - İndustry added")

def test_blog():  # blog kısmını test et
    driver.get("http://127.0.0.1:3000/blog/")
    time.sleep(3)
    assert "Our Blog" in driver.page_source
    print("Test Case 7: Successfull - Blog page is accesible")

def test_add_blog(): # add blog kısmını kontrol et
    driver.get("http://127.0.0.1:3000/blog/")
    time.sleep(3)
    add_blog_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn__primary')]")))
    add_blog_button.click()
    time.sleep(4)
    service_title_input = wait.until(EC.visibility_of_element_located((By.ID, "blogTitle")))
    service_title_input.send_keys("New Blog Title")
    service_description_input = driver.find_element(By.ID, "blogContent")
    service_description_input.send_keys("This is a blog description that is written to be tested by Selenium Python testing robot")
    service_image_input = driver.find_element(By.ID, "blogImage")
    service_image_input.send_keys("/static/images/service/1.jpg")
    service_link_input = driver.find_element(By.ID, "blogLink")
    service_link_input.send_keys("http://127.0.0.1:3000/index/")
    time.sleep(5)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)
    assert "New Blog Title" in driver.page_source
    print("Test Case 8: Successful - Blog added")

def test_industries_single():  #single-industry kısmını test et
    driver.get("http://127.0.0.1:3000/industries-single-industry/")
    time.sleep(3)
    assert "Provide Appropriate View And Access Permissions To" in driver.page_source
    print("Test Case 9: Successfull - Single Industry page is accesible")

def test_single_blog(): #single blog kısmını test et
    driver.get("http://127.0.0.1:3000/blog-single-post/")
    time.sleep(3)
    assert "Five Ways To Develop A World Sales Operations Function" in driver.page_source
    time.sleep(3)
    print("Test Case 10: Successfull - Blog Single Post is accessible")

def test_index_page():  # index sayfasını test et
    driver.get("http://127.0.0.1:3000/index/")
    time.sleep(3)
    assert "Fuad Garibli Yazılım Testi Dersi" in driver.page_source
    time.sleep(3)
    print("Test Case 11: Successfull - index.html is accessible")

def test_github_button(): #github butonunu test et
    # Set up the WebDriver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Navigate to the page
        driver.get("http://127.0.0.1:3000/")
        
        # Locate the GitHub button
        github_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'https://github.com/garibli')]")))

        # Verify the href attribute
        assert github_button.get_attribute("href") == "https://github.com/garibli", "GitHub link mismatch"
        
        # Click the button and verify the navigation
        github_button.click()
        wait.until(EC.url_contains("github.com/garibli"))
        assert "github.com/garibli" in driver.current_url, "Navigation to GitHub failed"
        print("Test Case 12: Github button test passed")
    
    finally:
        # Close the browser
        driver.quit()

def test_linkedin_button(): #linked in buttonunu test 
    # Set up the WebDriver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Navigate to the page
        driver.get("http://127.0.0.1:3000/")
        
        # Locate the LinkedIn button
        linkedin_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'https://az.linkedin.com/in/fuad-garibli-936354272')]")))

        # Verify the href attribute
        assert linkedin_button.get_attribute("href") == "https://az.linkedin.com/in/fuad-garibli-936354272", "LinkedIn link mismatch"
        
        # Click the button and verify the navigation
        linkedin_button.click()
        wait.until(EC.url_contains("linkedin.com/in/fuad-garibli-936354272"))
        assert "linkedin.com/in/fuad-garibli-936354272" in driver.current_url, "Navigation to LinkedIn failed"
        print("Test Case 13: Linkedin button test passed")
    
    finally:
        # Close the browser
        driver.quit()

def test_image_control(): #image control testi
    print("İmage")





# test_incorrect_login()
# test_existing_email()
# test_register()
# test_correct_login()
# test_industries()
# test_add_industry()
# test_blog()
# test_add_blog()
# test_industries_single()
# test_single_blog()
# test_index_page()
# test_github_button()
# test_linkedin_button()
test_image_control()
driver.quit()