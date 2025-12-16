students = ['Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden:
    def __init__(self, diagram, students=students):
        # make sure the student list is sorted
        self.diagram = diagram
        self.students = sorted(students)
        self.plant_dict = {'V' : 'Violets', 
                           'R' : 'Radishes',
                           'C' : 'Clover',
                           'G' : 'Grass'}
    
    def plants(self, student):
        # student's name are stored alphabetically
        # this is used to find the starting position 
        # in which to analyze the diagram
        idx = self.students.index(student)
        
        # starting index in diagram for this student
        i = idx * 2
        
        diagrams = self.diagram.split()
        # get starting letter of each plant
        
        labels = [d[j] for d in diagrams for j in range(i, i+2)]
        
        # generate the list of plants for this student
        student_plants = [self.plant_dict[letter] for letter in labels]
        
        
        return student_plants
        
        
