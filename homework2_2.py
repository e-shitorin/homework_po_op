#Полиморфизм с наследованием
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

def print_faculty_info(faculty):
    print(faculty.get_info())

computer_science_faculty = ComputerScience(
    "Факультет Computer Science",
    ["Software Engineering", "Data Science", "Cybersecurity"],
    ["Artificial Intelligence", "Machine Learning", "Computer Vision"]
)

it_faculty = ITFaculty("Факультет IT", ["Networking", "Web Development"])


print_faculty_info(computer_science_faculty)  
print_faculty_info(it_faculty)




#Полиморфизм без наследования
class ArtFaculty:
    def __init__(self, name, specializations):
        self.name = name
        self.specializations = specializations

    def get_info(self):
        specializations_list = ", ".join(self.specializations)
        return f"Факультет: {self.name} | Специальности: {specializations_list}"

def print_faculty_info_no_inheritance(faculty):
    print(faculty.get_info())

art_faculty = ArtFaculty("Факультет Искусств", ["Живопись", "Музыка", "Танец"])

print_faculty_info_no_inheritance(art_faculty)