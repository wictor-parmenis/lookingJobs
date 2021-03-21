

type_job = 'jobs-front-end'


# Jobs
jobs = []
for i in range(1, 16):
    path = f'/html/body/div[3]/div/div[2]/div[2]/div[{i}]/a/div/div[2]/div/h3'
    jobs.append(path)

# Pages
pages = []
for i in range(1,6):
    pages.append(f'https://programathor.com.br/{type_job}?expertise=J%C3%BAnior&page={i}')
