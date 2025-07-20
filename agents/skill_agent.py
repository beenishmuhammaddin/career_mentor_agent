from tools.roadmap_tool import get_career_roadmap

class SkillAgent:
    def provide_skills(self, career):
        return get_career_roadmap(career)