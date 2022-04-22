from Web_Scrape_Timejobs import JobsResults

key_skills = ['Python', 'JavaScript']


jobslist = JobsResults(key_skills)
jobslist.collect_jobs()
