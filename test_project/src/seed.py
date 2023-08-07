from random import randint
from datetime import datetime, timedelta

from faker import Faker

from database import session
from models import Student, Teacher, Group, Grade, Discipline

fake = Faker()

GROUPS = ['TF-01', 'TFS-02', 'TFR-03']
DISCIPLINES = ['informatics', 'history', 'design', 'mathematics', 'geography']

COUNT_TEACHERS = 5
COUNT_GRADES = 20
COUNT_STUDENTS = 50


def create_students():
    for _ in range(1, COUNT_STUDENTS+1):
        student = Student(fullname=fake.name(), group_id=randint(1, len(GROUPS)))
        session.add(student)
    session.commit()

def create_teachers(teachers):
    for _ in range(1, teachers+1):
        teacher = Teacher(email=fake.email(), fullname=fake.name())
        session.add(teacher)
    session.commit()

def create_groups(groups):
    for gr in groups:
        group = Group(name=gr)
        session.add(group)
    session.commit()

def create_grades():
    for student in range(1, COUNT_STUDENTS + 1):
        for g in range(1, 20):

            grade = Grade(grade=randint(1, 5), date_of=str(datetime.now().date()), student_id=randint(1, COUNT_STUDENTS), discipline_id=randint(1, len(DISCIPLINES)))
            session.add(grade)
    session.commit()

def create_discipines(disciplines):
    for d in disciplines:
        discipline = Discipline(name=d, teacher_id=randint(1, COUNT_TEACHERS))
        session.add(discipline)
    session.commit()


if __name__ == '__main__':
    create_groups(GROUPS)
    create_students()
    create_teachers(COUNT_TEACHERS)
    create_discipines(DISCIPLINES)
    create_grades()

