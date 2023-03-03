class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:   # elif self.language != language:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.skills >= skills_needed:
            if self.language != new_language:
                previous_language = self.language
                self.language = new_language
                return f"{self.name} switched from {previous_language} to {new_language}"
            else:   # elif self.language == new_language:
                return f"{self.name} already knows {new_language}"
        else:   # elif self.skills < skills_needed:
            needed_skills = abs(self.skills - skills_needed)
            return f"{self.name} needs {needed_skills} more skills"


# programmer = Programmer("John", "Java", 50)
# print(programmer.watch_course("Python Masterclass", "Python", 84))
# print(programmer.change_language("Java", 30))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Java: zero to hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python Masterclass", "Python", 84))


# class Programmer:
#     def __init__(self, name: str, language: str, skills: int):
#         self.name = name
#         self.language = language
#         self.skills = skills
# 
#     def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
#         if self.language == language:
#             self.skills += skills_earned
#             return f"{self.name} watched {course_name}"
#         else:
#             return f"{self.name} does not know {language}"
# 
#     def change_language(self, new_language: str, skills_needed: int) -> str:
#         if self.skills >= skills_needed and new_language != self.language:
#             previous_language = self.language
#             self.language = new_language
#             return f"{self.name} switched from {previous_language} to {new_language}"
#         elif self.skills >= skills_needed and new_language == self.language:
#             return f"{self.name} already knows {new_language}"
#         elif self.skills < skills_needed:
#             needed_skills = skills_needed - self.skills
#             return f"{self.name} needs {needed_skills} more skills"
