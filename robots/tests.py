from selenium.webdriver import Firefox, Chrome, Edge
from time import sleep
from elements import jobs


class CheckSubjectJobs:
    requirements = []
    job_pages = []
    jobs = []

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
            self._browser = Firefox()
        elif browser == 'chrome':
            self._browser = Chrome()
        else:
            self._browser = Edge()

    def pages(self):
        return self._pages

    def get_pages(self):
        for i in range(1, self._pages + 1):
            self.job_pages.append(f'https://programathor.com.br/jobs-{self.type_job}?expertise=J%C3%BAnior&page={i}')

    @property
    def type_job(self):
        return self._type_job

    @type_job.setter
    def type_job(self, type='front-end'):
        self._type_job = str(type)

    def get_jobs(self):
        for i in range(1, 16):
            path = f'/html/body/div[3]/div/div[2]/div[2]/div[{i}]/a/div/div[2]/div/h3'
            self.jobs.append(path)

    def find_subjects(self, type_browser):
        for page in self.job_pages:
            self.browser = type_browser
            self.browser.get(page)
            for job in jobs:
                try:
                    self.browser.find_element_by_xpath(job).click()
                    sleep(4)
                    try:
                        self.requirements.append(self.browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[9]').text)
                        self.requirements.append(self.browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[10]').text)

                    except:
                        self.requirements.append(self.browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/p[9]').text)
                    sleep(5)
                    self.browser.execute_script("window.history.go(-1)")
                    sleep(5)
                except Exception as e:
                    pass
            self.browser.close()
        for text in self.requirements:
            print(text)

    def insert_datas(self):
        with open('habilities.txt', 'r+') as file:
            file.truncate(0)

        for text in self.requirements:
            with open('habilities.txt', 'a', encoding='UTF-8') as file:
                file.write('_____' * 10 + '\n')
                file.write(text + '\n')
                file.write('_____' * 10 + '\n')
                file.write('\n\n\n')


if __name__ == '__main__':
    a = CheckSubjectJobs('chrome', 'front-end', 3)
    a.get_pages()
    a.find_subjects('firefox')
    a.insert_datas()

