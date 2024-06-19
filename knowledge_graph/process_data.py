import json

def get_job_desc(filename):
    with open(filename, "r", encoding="utf-8") as file:
        job_posts = json.load(file)


    for data in job_posts.values():
        job_title, company, job_desc = data["title"], data["company"], data["jd_text"]
        yield job_title, company, job_desc


if __name__ == "__main__":
    filename = "job_posts_data/job_posts_artificial_intelligence_2024-06-03.json"
    for d in get_job_desc(filename):
        print(d)