from utils.scrape_utils import IndeedScraper, save_job_desc
import argparse
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "logs/scrape_jd.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Indeed URL website", default="https://vn.indeed.com/jobs")
    parser.add_argument("--job", help="Job Position")
    parser.add_argument("--loc", help="Job Location")
    args = parser.parse_args()

    job_desc_dict = {}
    indeed_url, job, loc = args.url, args.job, args.loc

    indeed_url = indeed_url + f"?q={job}&l={loc}"
    scraper = IndeedScraper(logger)
    scraper.access_web(indeed_url)
    scraper.extract_all_jd()

    job_desc_dict = scraper.get_scraped_data()

    keyword = "_".join(job.lower().split())
    # Save job description file
    save_job_desc(job_desc_dict, keyword)
