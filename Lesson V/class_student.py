"""
Student class for presenting information about
the success of a student of a certain course.
"""


class Student:
    """
    The class implements methods for adding grades
    for laboratory work and for the exam and obtaining
    statistics on the success of the course.
    """

    def __init__(self, fio, config):

        self.student_fio = fio
        self.__course_config = config
        self.__passed = {x: None for x in
                         range(self.__course_config['lab_num'])}
        self.__attempts = {x: 0 for x in
                           range(self.__course_config['lab_num'])}
        self.__attempts['exam'] = 0
        self.__exam_grade = 0

    @property
    def grades_sum(self):
        """
        Returns student score
        """

        lab_grades = sum(filter(lambda x: x, self.__passed.values()))

        return lab_grades + self.__exam_grade

    @property
    def course_max(self):
        """
        Return course max score
        """

        return self.__course_config['lab_max'] * \
            self.__course_config['lab_num'] + \
            self.__course_config['exam_max']

    @property
    def is_certified(self):
        """
        Returns a tuple, where the first value is student score
        and the second one is the certificate confirmation
        """

        certified = False

        if self.grades_sum >= self.course_max * self.__course_config['k']:
            certified = True

        return self.grades_sum, certified

    def make_lab(self, grade, lab_n=None):
        """
        Adds grade m for the nth lab and returns
        reference to the current object
        """

        if grade > self.__course_config['lab_max']:
            grade = self.__course_config['lab_max']

        if lab_n in range(self.__course_config['lab_num']):
            if self.__attempts[lab_n] < 3:
                self.__passed[lab_n] = grade
                self.__attempts[lab_n] += 1

        if lab_n is None:
            for key, value in self.__passed.items():
                if value is None:
                    self.__passed[key] = grade
                    break

        return self

    def make_exam(self, grade):
        """
        Adds grade m for the exam and returns
        reference to the current object
        """

        if grade > self.__course_config['exam_max']:
            grade = self.__course_config['exam_max']

        if not self.__attempts['exam']:
            self.__exam_grade = grade
            self.__attempts['exam'] += 1

        return self


if __name__ == '__main__':

    CONF = {
        'exam_max': 30,
        'lab_max': 7,
        'lab_num': 10,
        'k': 0.61
    }

    STUDENT = Student("Alex", CONF)
    STUDENT.make_lab(5, 1).make_lab(6, 1).make_lab(8).make_lab(6, 10). \
        make_lab(3, 3).make_lab(7).make_lab(4, 5).make_lab(7). \
        make_lab(7).make_lab(7, 3).make_exam(35).make_exam(10)

    print(STUDENT.is_certified)
