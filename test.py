from enum import Enum

class Test(Enum):
    STUDENT = "Student"
    TEACHER = "Teacher"
    ADMIN = "Admin"



def main():

    list = [(test.name, test.value) for test in Test]
    print(list)



if __name__ == "__main__":
    main()
