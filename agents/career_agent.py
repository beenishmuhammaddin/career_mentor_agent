class CareerAgent:
    def suggest_careers(self, interests):
        if "tech" in interests:
            return ["Software Developer", "AI Engineer"]
        elif "design" in interests:
            return ["Graphic Designer", "UX Designer"]
        else:
            return ["Teacher", "Business Analyst"]