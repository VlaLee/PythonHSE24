class Student:
    def __init__(self, name: str, age: int, ID: int, grade: float):
        self.__name = name
        self.__age = age
        self.__ID = ID
        self.__grade = grade

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def getID(self) -> int:
        return self.__ID

    def getGrade(self) -> float:
        return self.__grade

    def getGoodMark(self) -> None:
        self.__grade += 0.5

    def getBadMark(self) -> None:
        self.__grade -= 0.5


st = Student("Oleg", 20, 101, 4.5)

print(st.getName())
print(st.getAge())
print(st.getID())
print(st.getGrade())

st.getBadMark()
st.getBadMark()
st.getBadMark()
st.getBadMark()
print(st.getGrade())

st.getGoodMark()
st.getGoodMark()
st.getGoodMark()
print(st.getGrade())
