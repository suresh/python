# Sample Diagram
# VRCGVVRVCGGCCGVRGCVCGCGV
# VRCCCGCRRGVCGCRVVCVGCGCV

class Garden:
    def __init__(self, diagram, students=''):
        if students == '':
            self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                             'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            self.students = students
            self.students.sort()

        self.plant_names = {'R': "Radishes",
                            'C': "Clover", 'G': "Grass", 'V': "Violets"}
        self.diagram = [list(e) for e in diagram.split('\n')]

    def plants(self, student):
        idx = self.students.index(student)
        plant_codes = [p[(2*idx): (2*idx+2)] for p in self.diagram]
        flat_list = [item for sublist in plant_codes for item in sublist]

        return [self.plant_names[pl] for pl in flat_list]
