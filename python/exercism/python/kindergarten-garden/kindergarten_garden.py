STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
		    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANTS = {
    'C': 'Clover',
    'G': 'Grass',
    'V': 'Violets',
    'R': 'Radishes'
}

class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        idx = self.students.index(student)

        plants_lst = []

        for row in self.diagram:
            plants_lst += list(map(lambda x: PLANTS[x], row[idx*2:idx*2+2]))

        return plants_lst