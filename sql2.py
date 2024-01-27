import datetime

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    student_id = Column('studentID', Integer, autoincrement=True,
                        primary_key=True, nullable=False)
    first_name = Column('firstname', String(50), nullable=False)
    last_name = Column('lastname', String(50), nullable=False)
    birth_date = Column('birth_date', DATE)
    gpa = Column('gpa', Integer)
    university_id = Column('universityID', Integer,
                           ForeignKey('universities.universityID'))

    def __init__(self, firstname, lastname, birthdate, gpa, university_id):
        self.first_name = firstname
        self.last_name = lastname
        self.birth_date = birthdate
        self.gpa = gpa
        self.university_id = university_id

    def __str__(self):
        return f'{self.student_id}: {self.first_name} {self.last_name}'


class University(Base):
    __tablename__ = "universities"
    university_id = Column('universityID', Integer, autoincrement=True,
                           primary_key=True, nullable=False)
    university_name = Column('universityName', String(50), nullable=False)
    students_number = Column('studentsNumber', Integer)

    def __init__(self, university_name, students_number):
        self.university_name = university_name
        self.students_number = students_number

    def __str__(self):
        return f'{self.university_id}: {self.university_name}'


my_db = create_engine("sqlite:///student_uny", echo=True)
Base.metadata.create_all(my_db)

Session = sessionmaker(bind=my_db)
session = Session()


def add_university(university_name, students_number):
    university = University(university_name, students_number)
    session.add(university)
    session.commit()


def add_student(firstname, lastname, birthdate, gpa, university_id):
    ids = session.query(University).filter(University.university_id
                                           == university_id).all()
    if len(ids) == 1:
        student = Student(firstname, lastname, birthdate, gpa, university_id)
        session.add(student)
        session.commit()
    else:
        print('There is not any university with this id!')


def delete_student(student_id):
    student = (session.query(Student).filter(Student.student_id == student_id).all())
    if len(student) > 0:
        session.delete(student[0])
        session.commit()


def update_student_name(student_id, new_name):
    updating_student = session.query(Student).filter(Student.student_id == student_id).first()
    updating_student.first_name = new_name
    session.commit()



universities = [
    {'university_name': 'BTU', 'students_number': 8500},
    {'university_name': 'KIU', 'students_number': 5300},
    {'university_name': 'TSU', 'students_number': 14000},
    {'university_name': 'GAU', 'students_number': 3500},
    {'university_name': 'SEU', 'students_number': 4500}
]

students = [
    {'firstname': 'Dato', 'lastname': 'Bitsadze', 'birthdate':
        datetime.date(2004, 9, 2),
     'gpa': '4.6', 'university_id': 1},
    {'firstname': 'Luka', 'lastname': 'Vashadze', 'birthdate':
        datetime.date(2004, 4, 15),
     'gpa': '4.6', 'university_id': 2},
    {'firstname': 'Tika', 'lastname': 'Vashadze', 'birthdate':
        datetime.date(2005, 5, 24),
     'gpa': '4.5', 'university_id': 5},
    {'firstname': 'Dato', 'lastname': 'Tsertsvadze', 'birthdate':
        datetime.date(2004, 5, 31),
     'gpa': '4.6', 'university_id': 1},
    {'firstname': 'Eka', 'lastname': 'Kutaladze', 'birthdate':
        datetime.date(2004, 6, 14),
     'gpa': '4.45', 'university_id': 3},
    {'firstname': 'Mariam', 'lastname': 'Kapanadze', 'birthdate':
        datetime.date(2004, 8, 19),
     'gpa': '4.45', 'university_id': 5},
    {'firstname': 'Givi', 'lastname': 'Tsukhishvili', 'birthdate':
        datetime.date(2004, 11, 19),
     'gpa': '4.4', 'university_id': 3},
    {'firstname': 'Toma', 'lastname': 'Burchuladze', 'birthdate':
        datetime.date(2004, 10, 15),
     'gpa': '4.5', 'university_id': 1},
    {'firstname': 'Vato', 'lastname': 'Tsitskishvili', 'birthdate':
        datetime.date(2005, 2, 5),
     'gpa': '4.5', 'university_id': 1},
    {'firstname': 'Goga', 'lastname': 'Kavtelashvili', 'birthdate':
        datetime.date(2004, 6, 13),
     'gpa': '4.45', 'university_id': 1},
    {'firstname': 'Nini', 'lastname': 'Vardidze', 'birthdate':
        datetime.date(2004, 12, 15),
     'gpa': '4.45', 'university_id': 1},
    {'firstname': 'Zaza', 'lastname': 'Bitsadze', 'birthdate':
        datetime.date(2005, 6, 6),
     'gpa': '4.35', 'university_id': 1},
    {'firstname': 'Nugzar', 'lastname': 'Chubinidze', 'birthdate':
        datetime.date(2004, 8, 19),
     'gpa': '4.7', 'university_id': 4},
    {'firstname': 'Luiza', 'lastname': 'Darbaidze', 'birthdate':
        datetime.date(2004, 8, 19),
     'gpa': '4.8', 'university_id': 2}

]

# insert

# for university in universities:
#     add_university(university['university_name'], university['students_number'])
#
#
# for student in students:
#     add_student(student['firstname'], student['lastname'],
#                 student['birthdate'], student['gpa'], student['university_id'])



# add_student('Juan', 'Reyes', datetime.date(2004, 9, 2),
#       '5', 1)

# update
# update_student_name(13, 'Nugzara')

# delete
# delete_student(15)

studentsInfo = session.execute(sqlalchemy.text("SELECT studentID, firstname, lastname "

                                               "FROM students")).fetchall()

for i in studentsInfo:
    print(f'id: {i[0]}, {i[1]} {i[2]}')


session.close()
