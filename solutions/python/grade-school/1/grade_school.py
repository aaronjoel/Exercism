class School:
    def __init__(self):
        '''
        Initialise a dictionary to keep students' info
        '''
        self.__students = {}

    def add_student(self, name, grade):
        '''
        add the student to the database
        '''
        if grade in self.__students:
            self.__students[grade].append(name)
        else:
            self.__students[grade] = [name]
        

    def roster(self):
        '''
        return a roster of students from students sorted by grade and then
        alphabetically for students within the same grade.
        '''
        grades = sorted(self.__students.keys())
        students = []
        for grade in grades:
            students.extend(sorted(self.__students[grade]))
        return students
        
    def grade(self, grade_number):
        '''
        return all students within a given grade sorted alphabetically.
        '''
        students_in_grade = sorted(self.__students.get(grade_number, []))
        return students_in_grade
