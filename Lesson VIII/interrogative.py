"""
Contains regular expression for matching interrogative sentences
"""

import re


if __name__ == '__main__':

    PATTERN = re.compile((
        r'^(?=[a-z]).*'  # check if sentence starts with letter
        r'(\b[A-Za-z]{3,}\b)'  # capture word with length > 2
        r'(?:.*\b\1\b.*){3,}\?$'  # find further captured group
    ), re.IGNORECASE | re.DOTALL)

    SENTENCE = ("Would you like to go to the new water parkif the weather\n"
                "was warm and if you were\n"
                "notsick and try to ride new slides, for example, \n"
                "'the giant spiral' or 'the highest hill in the world'?")

    MATCH = re.match(PATTERN, SENTENCE)

    print(MATCH.string)
