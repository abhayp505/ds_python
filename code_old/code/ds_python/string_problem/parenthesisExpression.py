class Expressions:

    dictonaries = {"(" : ")",
                   "[" : "]",
                   "{" : "}"
                   }
    stacks =[]

    def verifyBrackets(self, exp=str)->bool:

        for elements in exp:

            if elements in self.dictonaries.keys(): #checking if the element in string is part of keys of the map(dictonary) if yes push in the stack
                self.stacks.append(elements)

            elif elements in self.dictonaries.values(): #checking if the element in string is part of values of the map(dictonary) if yes check match with last opened bracket
                if elements == self.dictonaries.get(self.stacks[len(self.stacks)-1]): # len(self.stacks)-1 will give the top element in the stack
                    self.stacks.pop() # pop the element if matched from the stack
                    continue
                elif elements != self.dictonaries.get(self.stacks[len(self.stacks)-1]): #if not matched raise an exception
                    raise Exception('brackets are not matching')
                    return False


        print("expression is correct"+exp)
        return True



obj = Expressions()
exp = "[2+(4+3)]"
exp2 = "{7+[{78+9+(90+45)}]}"
wrong = "{7+ [ { 78+9+ (90+45) } ) }"
obj.verifyBrackets(wrong)