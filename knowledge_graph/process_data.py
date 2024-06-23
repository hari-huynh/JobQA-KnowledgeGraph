import json

def get_job_desc(job_lists):
    for data in job_lists:
        job_title, company, job_desc, date_posted = data["title"], data["company"], data["jd_text"], data["date_posted"]
        yield job_title, company, job_desc, date_posted


if __name__ == "__main__":
    pass
    # filename = "job_posts_data/job_posts_artificial_intelligence_2024-06-03.json"
    # for d in get_job_desc(filename):
    #     print(d)