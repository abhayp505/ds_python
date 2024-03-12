"""Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another
    expression.
Some examples:
 ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6"""
import operator
from stack import push, pop, length, stacks

class ReversePolishNotation:

    # define operators you wanna use
    def __init__(self, list):
        self.list=list
        self.allowed_operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv}

    def isInteger(self, data):
        flag = True
        try:
            # try converting to integer
            int(data)
        except ValueError:
            flag = False
            return flag
        return flag

    def calculate(self):
        list = self.list
        for element in list:
            if self.isInteger(element) :
                num = int(element)
                push(num)
            elif element in ("+","-","/","*"):
                ele1 = pop()
                ele2 = pop()
                ele = self.allowed_operators[element](ele2, ele1)
                print("value ::", ele)
                push(ele)
            else:
                print("Not a valid element")
                continue
        result = pop()
        print("result ::", int(result))
        return int(result)



input = ["2", "1", "+", "3", "*"]
rpn=ReversePolishNotation(input)
rpn.calculate()

