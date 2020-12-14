from selenium import webdriver
from bs4 import BeautifulSoup as soup

#customising options for driver
options = webdriver.ChromeOptions()
options.add_argument("--lang=en")
driver = webdriver.Chrome('/Users/calvintsang/Desktop/chromedriver', options=options)

#target url
my_url = "https://www.google.com/maps/search/frankfurt+bornheim+businesses/@50.1204283,8.7095445,15z"

driver.get(my_url)

#creating page soup
page_soup = soup(driver.page_source, 'html.parser')
print(page_soup.body)
#a list of company info containers
containers = page_soup.find_all('div', class_='section-result-text-content')
#create storing file
filename = "Frankfurt Bornheim Companies.csv"
f = open(filename, "w")
headers = "company_name, company_type, company_location, company_telephone\n"
f.write(headers)


#extract data
for container in containers:
    com_name = container.div.div.find('div', class_='section-result-title-container').h3.span.text
    com_dets = container.find('div', class_='section-result-details-container')
    com_type = com_dets.find('span', class_='section-result-details').text
    com_loc = com_dets.find('span', class_='section-result-location').text
    com_num = container.find('div', class_='section-result-hours-phone-container').find('span',
                                                    class_='section-result-info section-result-phone-number').span.text

    print(f"name: {com_name}")
    print(f"type: {com_type}")
    print(f"location: {com_loc}")
    print(f"contact number: {com_num}")

    f.write(com_name + "," + com_type + "," + com_loc + "," + com_num + '\n')
f.close()



