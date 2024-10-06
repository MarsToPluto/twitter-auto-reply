from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep as s

posts = [
    'https://twitter.com/example/status/1396877846111424512',
    'https://twitter.com/example/status/1397015676695498762',
    'https://twitter.com/example/status/1397015551906570243',
    'https://twitter.com/example/status/1397014809200132096'
]

text = "Come & get Me"
loginURL = "https://twitter.com/login"

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
except Exception as e:
    print(f"Error initializing WebDriver: {e}")
    exit()

try:
    driver.get(loginURL)
    s(4)
except Exception as e:
    print(f"Error loading Twitter login page: {e}")
    driver.quit()
    exit()

try:
    username_or_email = driver.find_elements_by_name("session[username_or_email]")[0].send_keys("Shreya94087966")
    password = driver.find_elements_by_name("session[password]")[0].send_keys("asjkdsal*(&A*(S&AS()A*S()S")
    driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]').click()
    s(4)
except Exception as e:
    print(f"Error during login: {e}")
    driver.quit()
    exit()

for post in posts:
    try:
        driver.get(post)
    except Exception as e:
        print(f"Error loading post {post}: {e}")
        continue

    y = 3000
    try:
        for timer in range(10):
            driver.execute_script(f"window.scrollTo(0, {y})")
            y *= 2
            s(4)
    except Exception as e:
        print(f"Error scrolling through post {post}: {e}")
        continue

    s(2)

    try:
        replies = driver.find_elements_by_xpath('//div[@data-testid="reply"]')
        print(driver.current_url)
        print(f"Total replies: {len(replies)}")
    except Exception as e:
        print(f"Error finding replies for post {post}: {e}")
        continue

    posted = 1
    for replyOpen in replies:
        try:
            driver.execute_script("arguments[0].click();", replyOpen)
            s(2)
            driver.find_element_by_xpath('//div[@data-testid="tweetTextarea_0"]').send_keys(text)
            driver.find_element_by_xpath('//div[@data-testid="tweetButton"]').click()
            print(f"Success: {posted}")
        except Exception as e:
            try:
                close = driver.find_elements_by_class_name('css-1dbjc4n r-11z020y r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af')
                if close and len(close) > 0:
                    close[0].click()
            except Exception as inner_e:
                print(f"Error closing pop-up: {inner_e}")
            print(f"Failed: {posted} due to {e}")
        posted += 1
        s(5)

try:
    driver.quit()
except Exception as e:
    print(f"Error closing the WebDriver: {e}")