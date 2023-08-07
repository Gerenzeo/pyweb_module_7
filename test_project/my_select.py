from sqlalchemy import func, desc, and_

from src.database import session
from src.models import Student, Teacher, Group, Grade, Discipline

def select_1():
    # Найти 5 студентов с наибольшим средним баллом по всем предметам.
    sa_query = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return sa_query

def select_2(discipline_id: int):
    # Найти студента с наивысшим средним баллом по определенному предмету.
    sa_query = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                .select_from(Grade).join(Student).join(Discipline).filter(Discipline.id == discipline_id)\
                .group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).limit(1).all()
    return sa_query

def select_3(group_id: int):
    # Найти средний балл в группах по определенному предмету.
    sa_query = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                .select_from(Group).join(Student).join(Grade).filter(Group.id == group_id).group_by(Group.name).limit(1).all()
    return sa_query

def select_4():
    # Найти средний балл на потоке (по всей таблице оценок).
    sa_query = session.query(func.round(func.avg(Grade.grade))).all()
    return sa_query

def select_5(teacher_id: int):
    # Найти какие курсы читает определенный преподаватель.
    sa_query = session.query(Teacher.fullname, Discipline.name).select_from(Teacher)\
            .join(Discipline).filter(Discipline.teacher_id == teacher_id).all()
    return sa_query

def select_6(group_id: int):
    # Найти список студентов в определенной группе.
    sa_query = session.query(Student.fullname, Group.name).select_from(Group).join(Student).filter(Group.id == group_id).all()
    return sa_query

def select_7(group_id: int, discipline_id: int):
    # Найти оценки студентов в отдельной группе по определенному предмету.
    sa_query = session.query(Student.fullname, Grade.grade, Group.name).select_from(Grade).join(Discipline).join(Student)\
        .join(Group)\
        .filter(and_(Group.id == group_id, Discipline.id == discipline_id)).all()

    return  sa_query

def select_8(teacher_id: int):
    # Найти средний балл, который ставит определенный преподаватель по своим предметам.
    sa_query = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Teacher) \
        .join(Discipline, Discipline.teacher_id == Teacher.id).join(Grade).filter(Discipline.teacher_id == teacher_id).group_by(Teacher.fullname, Discipline.name).all()
    return sa_query

def select_9(student_id: int):
    # Найти список курсов, которые посещает определенный студент.
    sa_query = session.query(Student.fullname, Discipline.name).select_from(Grade).join(Student).join(Discipline)\
                .filter(and_(Grade.student_id == student_id)).distinct(Discipline.name).all()
    return sa_query

def select_10(student_id: int, teacher_id: int):
    # Список курсов, которые определенному студенту читает определенный преподаватель.
    sa_query = session.query(Student.fullname, Discipline.name, Teacher.fullname).select_from(Grade).join(Student).join(Discipline).join(Teacher) \
        .filter(and_(Grade.student_id == student_id, Discipline.teacher_id == teacher_id)).distinct(Discipline.name).all()
    return sa_query


if __name__ == '__main__':
    print(select_10(1, 1))