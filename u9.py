class Person:
    def __init__(self, first_name: str, last_name: str, birth_date: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_info(self):
        return f"""
First name: {self.first_name}
Last name: {self.last_name}
Birth date: {self.birth_date}"""


class Student(Person):
    def __init__(self, first_name: str, last_name: str, birth_date: str, faculty: str, level: int) -> None:
        super().__init__(first_name, last_name, birth_date)
        self.faculty = faculty
        self.level = level
        self.subjects = []

    def get_info(self):
        return f"""{super().get_info()}    
Faculty: {self.faculty}
Level: {self.level}
Subjects: {self.to_str()}"""

    def add_subject(self, subjects):
        count = 1
        for i in self.subjects:
            if subjects.subject == i.subject:
                count = 0
                break
        if count:
            self.subjects.append(subjects)


    def remove_subject(self, removed_subject):
        if removed_subject in self.subjects:
            self.subjects.remove(removed_subject)


    def to_str(self):
        all_subjects = str()
        for i in self.subjects:
            all_subjects += i.subject + ", "
        return all_subjects[:-2]


class Subjects:
    def __init__(self, subject):
        self.subject = subject


user = Student("Akramjon", "Abduvahobov", "14.03.2009", "Kiber injinering", 1)
subject1 = Subjects("Ximiya")
user.add_subject(subject1)
subject2 = Subjects("Ximiya")
user.add_subject(subject2)
subject3 = Subjects("Fizika")
user.add_subject(subject3)
subject4 = Subjects("Fizra")
user.add_subject(subject4)

print(user.get_info())