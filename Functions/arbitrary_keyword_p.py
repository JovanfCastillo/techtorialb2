# We are going to use two * symbol for this implementation.

def print_student_names(**names):
    print(names["last_name"])

print_student_names(name="yusuf",last_name="Turan")

#You can encounter that someone call this implementation as kwargs

#used to leave method block empty
def empty_function():
    pass

