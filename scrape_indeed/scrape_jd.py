from utils import IndeedScraper, save_job_desc
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Indeed URL website", default= "https://vn.indeed.com/jobs")
    parser.add_argument("--job", help="Job Position")
    parser.add_argument("--loc", help="Job Location")
    args = parser.parse_args()
    
    
    job_desc_dict = {}
    indeed_url, job, loc = args.url, args.job, args.loc
    
    scraper = IndeedScraper(job_desc_dict)
    scraper.access_web(indeed_url)
    scraper.filter_job_location(job, loc)
    scraper.extract_all_jd()
    
    job_desc_dict = scraper.jd_dict
    
    keyword = "_".join(job.lower().split())
    # Save job description file
    save_job_desc(job_desc_dict, keyword)
    

    
    