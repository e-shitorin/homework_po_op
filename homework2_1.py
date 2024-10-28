class Faculty:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Факультет: {self.name}"

class ITFaculty(Faculty):
    def __init__(self, name, departments):
        super().__init__(name)
        self.departments = departments

    def get_info(self):
        departments_list = ", ".join(self.departments)
        return f"{super().get_info()} | Отделение: {departments_list}"

class ComputerScience(ITFaculty):
    def __init__(self, name, departments, research_areas):
        super().__init__(name, departments)
        self.research_areas = research_areas

    def get_info(self):
        research_areas_list = ", ".join(self.research_areas)
        return f"{super().get_info()} | Области иследования: {research_areas_list}"

computer_science_faculty = ComputerScience(
    "Факультет Computer Science",
    ["Software Engineering", "Data Science", "Cybersecurity"],
    ["Artificial Intelligence", "Machine Learning", "Computer Vision"]
)

print(computer_science_faculty.get_info())