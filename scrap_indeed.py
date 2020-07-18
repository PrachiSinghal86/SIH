from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup


driver = webdriver.Chrome("./chromedriver")

df = pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Sponsored","Description"])

for i in range(0, 200,10):
    driver.get('https://www.indeed.co.in/jobs?q=android+developer&l=India&fromage=3&start=' + str(i))

    driver.implicitly_wait(4)

    for job in driver.find_elements_by_class_name('result'):


        soup = BeautifulSoup(job.get_attribute('innerHTML'), 'html.parser')

        try:
            title = soup.find("a", class_="jobtitle").text.replace("\n", "").strip()

        except:
            title = 'None'

        try:
            location = soup.find(class_="location").text
        except:
            location = 'None'

        try:
            company = soup.find(class_="company").text.replace("\n", "").strip()
        except:
            company = 'None'

        try:
            salary = soup.find(class_="salary").text.replace("\n", "").strip()
        except:
            salary = 'None'

        try:
            sponsored = soup.find(class_="sponsoredGray").text
            sponsored = "Sponsored"
        except:
            sponsored = "Organic"

        try:
            sum_div=job.find_element_by_class_name("summary")


            driver.execute_script("arguments[0].click();",sum_div)
            job_desc=driver.find_element_by_id('vjs-desc').text
        except:
            job_desc=soup.find(class_="summary").text.replace("\n", "").strip()



        df = df.append({'Title': title,'Location': location, 'Company': company, 'Salary': salary,
                        'Sponsored': sponsored,'Description': job_desc}, ignore_index=True)



df.to_csv("adnew.csv", index=False)