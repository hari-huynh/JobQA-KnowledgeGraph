import os
import re
import time
import urllib
import json
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class IndeedScraper:
    def __init__(self, logger):

        # WebDriver Configurations
        WINDOW_SIZE = "1920,1080"
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=%s" % WINDOW_SIZE)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')

        self.driver = webdriver.Edge(options=options)
        self.logger = logger
        self.jd_dict = {}

    def access_web(self, url):
        """
        Access website using URL
        """
        self.driver.get(url)

        # Wait a second
        time.sleep(2)

    def extract_one_jd(self):
        """
        Extract Job Description text
        """
        time.sleep(2)

        # Job title
        job_title_raw = self.driver.find_element(By.XPATH, '//h2[@data-testid="jobsearch-JobInfoHeader-title"]/span')
        job_title = job_title_raw.text.replace("- job post", "").strip()

        # Company name
        company_name = self.driver.find_element(By.XPATH, '//div[@data-testid="inlineHeader-companyName"]/span/a').text

        # Location
        location = self.driver.find_element(By.XPATH, '//div[@data-testid="inlineHeader-companyLocation"]/div').text

        # Job Description Text
        job_description = self.driver.find_elements(By.XPATH, '//div[@id="jobDescriptionText"]')

        full_jd = ""
        for jd in job_description:
            html_txt = jd.get_attribute("innerHTML")  # Get HTML text
            soup = BeautifulSoup(html_txt, 'html.parser')
            cleaned_jd = soup.get_text()  # Get text after remove HTML tags
            cleaned_jd = re.sub(r"\n{2,}", "\n\n", cleaned_jd)  # Replace multiple \n

            full_jd += cleaned_jd

        num_token = len(full_jd.split())

        return job_title, company_name, full_jd, num_token

    def goto_nextpage(self):
        try:
            page_next = self.driver.find_element(By.XPATH, '//a[@data-testid="pagination-page-next"]')
            page_next.click()
            time.sleep(2)

            # If popup display, close it
            try:
                close_popup = self.driver.find_element(By.XPATH, '//button[@aria-label="close"]')
                close_popup.click()
            except NoSuchElementException:
                pass

            time.sleep(2)
            return True

        except NoSuchElementException:
            time.sleep(2)
            return False

    def extract_all_jd(self):
        # Start index
        job_id = len(self.jd_dict.keys())

        while True:
            job_infors = self.driver.find_elements(By.XPATH, '//div[@class="job_seen_beacon"]')

            for job_info in job_infors:
                job_info.click()

                job_title, company_name, full_jd, num_token = self.extract_one_jd()

                # If job doesn't exists, add to dictionary
                job_key = f"{job_title} @ {company_name}"

                try:
                    self.jd_dict[job_key]
                except KeyError:
                    self.jd_dict[job_key] = {
                        "id": job_id,
                        "title": job_title,
                        "company": company_name,
                        "jd_text": full_jd,
                        "jd_num_tokens": num_token
                    }

                print("({}) Processed ...... {} @ {}".format(job_id, job_title, company_name))
                self.logger.info("({}) Processed ...... {} @ {}".format(job_id, job_title, company_name))
                job_id += 1
                time.sleep(2)

            # Move to next page
            if not self.goto_nextpage():
                break

        # Quit website
        self.driver.quit()

    def get_scraped_data(self):
        return self.jd_dict

def save_job_desc(jd_dict, keyword):
    directory = './job_posts_data'

    today = str(datetime.date.today())
    filename = f"{directory}/job_posts_{keyword}_{today}.json"

    json_file = json.dumps(jd_dict, indent=4, ensure_ascii=False)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_file)