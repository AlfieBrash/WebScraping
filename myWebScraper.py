from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

countries = soup.findAll("div", attrs={"class":"country"})
countriesExtracted = []
for country in countries:
    # Extract country details:
    countryName = country.find('h3', class_='country-name').get_text(strip=True)    
    countryCapital = country.find('span', class_='country-capital').get_text(strip=True)
    countryPopulation = country.find('span', class_='country-population').get_text(strip=True)
    countryArea = country.find('span', class_='country-area').get_text(strip=True)
    countriesExtracted.append([countryName,countryCapital,countryPopulation,countryArea])

# Output to a csv
filePath = "C:/Users/Admin/Documents/Alfies_Stuff/PythonCoding/myWebScraper/scrapedCountries.csv"
with open(filePath, "w", encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "Capital", "Population", "Area"])
    writer.writerows(countriesExtracted)
    file.close()

print("Finished")