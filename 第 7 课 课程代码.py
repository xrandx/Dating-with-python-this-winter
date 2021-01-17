class Player(object):
    def __init__(self, public_name):
        self.__public_name = public_name
        self.__score = 0

    def increase_score(self):
        self.__score += 1

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def __test(self):
        print(self.__public_name, "test")

    def print(self):
        self.__test()


class Human(Player):

    def __init__(self, public_name, money):
        super().__init__(public_name)
        self.__money = money

    def increase_score(self):
        if self.__money > 10:
            self.set_score(self.get_score() + 1.5)
        else:
            self.set_score(self.get_score() + 1)

    def decrease_score(self):
        if self.__money > 10:
            self.set_score(self.get_score() - 1)
        else:
            self.set_score(self.get_score() - 1.2)


class Robot(Player):

    def increase_score(self):
        self.set_score(self.get_score() + 0.8)

    def decrease_score(self):
        self.set_score(self.get_score() - 0.8)


def increase_score(Obj):
    Obj.increase_score()


def detect(winner, loser):
    winner.increase_score()
    loser.decrease_score()

if __name__ == '__main__':
    # dict
    # key_value = dict()
    score_sheet = {
        "语文": 90,
        "数学": 90
    }

    # print(score_sheet["语文"])
    score_sheet["英语"] = 90

    # score2name = dict()
    # score2name[90.0] = "英语"

    # array = tuple([2, 1])
    # score_sheet.clear()

    # print(score2name[90.0])
    # for key, value in score_sheet.items():
    #     if value == 130:
    #         print(key)


    # key
    # value
    # sheet = dict()
    # sheet["我的身高"] = [177, 178]
    # sheet["我的身高"].append(180)
    # print(sheet.pop())

    # xiaoming = Human("xiaoming", 20)
    # Matrix = Robot("Matrix")
    #
    # for i in range(10):
    #     if i % 3 == 0:
    #         detect(Matrix, xiaoming)
    #     else:
    #         detect(xiaoming, Matrix)
    # print(xiaoming.get_score(), Matrix.get_score())

    # increase_score(xiaoming)
    # increase_score(Matrix)
    #
    # print(xiaoming.get_score(), Matrix.get_score())



    # a = 0
    #
    # def modify_var(diff_var):
    #     print(a is diff_var)
    #     diff_var += 1
    #     print(a is diff_var)
    #
    # modify_var(a)
    #
    # print(a)
    # array = [1, 2, 3]
    #
    # def modify_list(diff_list):
    #     print(array is diff_list)
    #     diff_list.append(4)
    #     print(array is diff_list)
    #
    # modify_list(array)
    # print(array)

