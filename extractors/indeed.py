from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#브라우저 연결
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)

#scrapping code
def get_indeed(keyword):
  results = [] #결과 박스
  url = f"https://kr.indeed.com/jobs?q={keyword}" #들어갈 링크
  browser.get(url) #링크 가져와 주세요
  
  soup = BeautifulSoup(browser.page_source, 'html.parser') #링크 들어가서 html 가져와주세요
  ul = soup.find('ul', class_="jobsearch-ResultsList") 
  lis = ul.find_all('li', recursive=False)
  for x in lis:
    zone = x.find('div', class_='mosaic-zone')
    if zone == None:
      a = x.select_one("h2 a")
      title = a['aria-label']
      link = a['href']
      company = x.select_one('.companyName')
      location = x.select_one('.companyLocation')
  
      job_data = {
        'link' : f'https://kr.indeed.com{link}',
        'company': company.string.replace(",", " "),
        'location' : location.string.replace(",", " "),
        'position' : title.replace(",", " ")
      }
      
      results.append(job_data)
  
  
  pagination = soup.find("nav", attrs={"aria-label":"pagination"})
  next_button = pagination.find("a", attrs={"aria-label":"Next Page"})

  while next_button != None:
    next_url = next_button["href"]
    url = f"https://kr.indeed.com{next_url}"
    print(url)
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    ul = soup.find('ul', class_="jobsearch-ResultsList")
    lis = ul.find_all('li', recursive=False)
    for x in lis:
      zone = x.find('div', class_='mosaic-zone')
      if zone == None:
        a = x.select_one("h2 a")
        title = a['aria-label']
        link = a['href']
        company = x.select_one('.companyName')
        location = x.select_one('.companyLocation')
        
        job_data = {
          'link' : f'https://kr.indeed.com{link}',
          'company': company.string.replace(",", " "),
          'location' : location.string.replace(",", " "),
          'position' : title.replace(",", " ")
        }
        
        results.append(job_data)
    
    
    pagination = soup.find("nav", attrs={"aria-label":"pagination"})
    next_button = pagination.find("a", attrs={"aria-label":"Next Page"})
  
  return results

