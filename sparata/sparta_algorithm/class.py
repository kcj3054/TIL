class Person:
    # 파이썬 생성자 만들때 인자에 자기 자신을 넘겨준다
    def __init__(self, param_name):
        print("i am created", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요 저의 이름은 "  + self.name + "입니다")




person1 = Person("유재석")
person1.talk()

person2 = Person("박명수");