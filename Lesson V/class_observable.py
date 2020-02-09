"""
The module contains class 'Observable'
"""


class Observable(dict):
    """
    Overrides the magic methods __getattr__ and __str__.
    Extends the built-in dict class.
    """

    def __getattr__(self, attr):

        try:
            return self[attr]
        except KeyError:
            raise AttributeError

    def __str__(self):

        public_fields = filter(lambda item: not item[0].startswith('_'),
                               self.items())
        formated_fields = map(lambda item: '='.join(list(map(str, item))),
                              public_fields)

        formated_fields_string = ','.join(formated_fields)
        return f'{type(self).__name__}({formated_fields_string})'


class XClass(Observable):
    """
    Just a inheritor of class Observable
    """


if __name__ == '__main__':

    X_OBJ = XClass(a=10, b=20, __c=1, d={'a': 'b'})
    print(X_OBJ)
