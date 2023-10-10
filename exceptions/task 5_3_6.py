class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.is_num(ans_digit)
        self.is_num(max_error_digit)
        self.is_positive(max_error_digit)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def is_num(self, num):
        if type(num) not in (int, float):
            raise ValueError('недопустимые значения аргументов теста')
        else:
            return True

    def is_positive(self, num):
        if num < 0 :
            raise ValueError('недопустимые значения аргументов теста')
        else:
            return True

    def run(self):
        ans = float(input())
        if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit:
            return True
        else:
            return False


try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False