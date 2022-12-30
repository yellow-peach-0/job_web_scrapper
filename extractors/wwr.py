from requests import get
from bs4 import BeautifulSoup 

def get_wwr(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  response = get(f'{base_url}{keyword}')
  
  if not response.status_code == 200:
    print("Can't request website")
  else: 
    results = []
    
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_='jobs')
    
    #last_li = jobs[2].find_all('li')[3]
    for x in jobs:
      features = x.find_all('li')
      features.pop(-1)
  
      for x in features:
        a_s = x.find_all('a')
        a = a_s[1]
  
        link = a['href']
        #find_all로 검색할 시 list 속성으로 나오기에 string 못씀
        title = a.find('span', class_='title').string
        name, shift, region = a.find_all('span', class_='company')
        
        job_data = {
          'link' : f'https://weworkremotely.com{link}',
          'company' : name.string.replace(",", " "),
          'location' : region.string.replace(",", " "),
          'position' : title.replace(",", " "),
        }
        results.append(job_data)
  
  
    return results

      



