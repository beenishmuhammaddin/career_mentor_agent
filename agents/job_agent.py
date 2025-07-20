class JobAgent:
    def show_job_roles(self, career):
        jobs = {
            "Software Developer": ["Frontend Dev", "Backend Dev", "Full Stack Dev"],
            "AI Engineer": ["ML Engineer", "Data Scientist"]
        }
        return jobs.get(career, ["No jobs available"])