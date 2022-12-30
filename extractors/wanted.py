from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)

def get_wanted(keyword):
  results = []
  base_url ="https://www.wanted.co.kr"
  url = f"{base_url}/search?query={keyword}"
  browser.get(url)
  
  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_list = soup.find("ul", attrs={"data-cy":"job-list"})
  lis = job_list.select("li")
  for x in lis:
    link = x.select_one("a")["href"]
    company = x.select_one(".job-card-company-name")
    location = x.select_one(".job-card-company-location").get_text()
    position = x.select_one(".job-card-position")

    job_data = {
      "link" : f"{base_url}{link}",
      "company" : company.string.replace(",", " "),
      "location" : location.replace(",", " "),
      "position" : position.string.replace(",", " ")
    }
    results.append(job_data)

  return results