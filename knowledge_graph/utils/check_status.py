import os
from .scrape_utils import read_job_desc

DATA_DIR = "job_posts_data"

def manage_jobs():
   # First day
   if len(os.listdir()) == 1:
      # Add all jobs to knowledge graph
      file_today = os.listdir(DATA_DIR)[0]
      jobs_today= read_job_desc(file_today)
      new_jobs = list(jobs_today.values())

      return new_jobs, []


   closed_jobs = []
   new_jobs = []
   file_yesterday, file_today = os.listdir(DATA_DIR)[-2:]
   jobs_yesterday = read_job_desc(file_yesterday)
   jobs_today = read_job_desc(file_today)

   # Check new jobs open
   jobs_title_today = list(jobs_today.keys())
   for job_title in jobs_title_today:
      if not jobs_yesterday.get(job_title):
         new_jobs.append(jobs_today[job_title])

   # Check jobs closed
   jobs_title_yesterday = list(jobs_yesterday.keys())
   for job_title in jobs_title_yesterday:
      if not jobs_today.get(job_title):
         closed_jobs.append(jobs_yesterday[job_title])

   return new_jobs, closed_jobs

if __name__ == "__main__":
   new_jobs, closed_jobs = manage_jobs()
   print(len(new_jobs), len(closed_jobs))





