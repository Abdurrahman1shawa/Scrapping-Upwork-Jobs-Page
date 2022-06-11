from bs4 import BeautifulSoup
import requests

#parsing jobs from upwork saved web page 

html_page = open("Freelance Python Jobs - Upwork.html", "r")
html_page = html_page.read()

parser = BeautifulSoup(html_page, "lxml")

jobs = parser.find_all("section" ,class_ = "up-card-section up-card-list-section up-card-hover")

#problem, fix the problem of avoiding the first job announcement.

for job in jobs:
	print(job)
	job_title = job.find("h4" , class_ = "my-0 p-sm-right job-tile-title").text
	job_text = job.find("span" , attrs={'data-test' : 'job-description-text'}).text
	print(job_title)
	print(job_text)



