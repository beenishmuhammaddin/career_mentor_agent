def get_career_roadmap(career):
    roadmap = {
        "Software Developer": ["Learn Python", "Data Structures", "Git & GitHub"],
        "AI Engineer": ["Python", "ML Algorithms", "TensorFlow/PyTorch"]
    }
    return roadmap.get(career, ["No roadmap available"])