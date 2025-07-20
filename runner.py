from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

class CareerMentorRunner:
    def __init__(self):
        self.career_agent = CareerAgent()
        self.skill_agent = SkillAgent()
        self.job_agent = JobAgent()

    def start(self):
        interests = input("🧠 What are your interests? (e.g., tech, design): ").lower()
        careers = self.career_agent.suggest_careers(interests)
        
        print(f"\n🎓 Suggested careers: {careers}")
        career_choice = input("\n✅ Choose a career to explore: ")

        skills = self.skill_agent.provide_skills(career_choice)
        print(f"\n🛠 Skills for {career_choice}: {skills}")

        jobs = self.job_agent.show_job_roles(career_choice)
        print(f"\n💼 Job roles in {career_choice}: {jobs}")

if __name__ == "__main__":
    runner = CareerMentorRunner()
    runner.start()