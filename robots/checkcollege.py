from selenium.webdriver import Firefox, Chrome, Edge
from time import sleep
from elements import jobs


class CheckSubjectJobs:

    requirements = []

    def __init__(self, browser, type_job, pages, **kwargs):
        self._browser = browser
        self._type_job = type_job
        self._pages = pages

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, browser):
        if browser == 'firefox':
            self._browser = Firefox
        elif browser == 'chrome':
            self._browser = Chrome()
        else:
            self._browser = Edge()
        print(self._browser)

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, number=5):
        for i in range(1, number):
            self.pages.append(f'https://programathor.com.br/{self.type_job}?expertise=J%C3%BAnior&page={i}')

    @property
    def type_job(self):
        return  self._type_job

    @type_job.setter
    def type_job(self, type='front-end'):
        self._type_job = str(type)

    def find_subjects(self):
        for page in self.pages:
            print(page)

browser.get(url)
sleep(4)
requirements = []

for job in jobs:
    try:
        browser.find_element_by_xpath(job).click()
        sleep(4)
        print(job)

        try:
            requirements.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[9]').text)
            requirements.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[10]').text)

        except:
            requirements.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[9]').text)
        sleep(5)
        browser.execute_script("window.history.go(-1)")
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







