from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.keys import Keys
from elements import jobs

browser = Firefox()
type_job = 'jobs-front-end'
pages = [1, 2, 3, 4, 5]
url = f'https://programathor.com.br/{type_job}?expertise=J%C3%BAnior&page=1'


browser.get(url)
sleep(4)
requirements = []

for job in jobs:
    try:
        browser.find_element_by_xpath(job).click()
        sleep(4)
        print(job)
        """
        if job == '/html/body/div[3]/div/div[2]/div[2]/div[2]/a/div/div[2]/div/h3':
            sleep(3)
            print(browser.current_url)
            browser.execute_script("window.history.go(-1)")
            sleep(3)
            if browser.current_url == 'https://programathor.com.br/jobs-front-end?expertise=J%C3%BAnior&page=1':
                next = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[18]/nav/ul/li[2]/a')
                next.click()
            if browser.current_url == 'https://programathor.com.br/jobs-front-end?expertise=J%C3%BAnior&page=2':
                next = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[18]/nav/ul/li[5]/a')
                next.click()
        """
        try:
            requirements.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[9]').text)
            requirements.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[10]').text)

        except:
            requirements.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[9]').text)
        sleep(5)
        browser.execute_script("window.history.go(-1)")
        """
        page 3, 4 and 5:
        ('/html/body/div[3]/div/div[2]/div[2]/div[18]/nav/ul/li[5]/a')
        ('/html/body/div[3]/div/div[2]/div[2]/div[18]/nav/ul/li[6]/a')
        ('/html/body/div[3]/div/div[2]/div[2]/div[18]/nav/ul/li[7]/a')
        """
        sleep(5)
    except Exception as e:
        pass


with open('habilities.txt', 'r+') as file:
    file.truncate(0)

for text in requirements:
    with open('habilities.txt', 'a', encoding='UTF-8') as file:
        file.write('_____'*10 + '\n')
        file.write(text + '\n')
        file.write('_____'*10 + '\n')
        file.write('\n\n\n')


browser.close()







