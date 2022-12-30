from extractors.indeed import get_indeed 
from extractors.wanted import get_wanted
from extractors.wwr import get_wwr

keyword = input("What do you search")

indeed = get_indeed(keyword)
wanted = get_wanted(keyword)
wwr = get_wwr(keyword)

jobs = indeed + wanted + wwr

file = open(f"{keyword}.csv", "w")
file.write("Position, Company, Location, URL\n")

for job in jobs:
  file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")

file.close()
