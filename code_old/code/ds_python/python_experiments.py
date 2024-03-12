
class UserInput:

    def user_input(self):
        input_usr = input("enter input")
        print("type ::", type(input_usr))
        input_usr = list(map(int , input_usr.split()))
        print("value ::", input_usr)

usr_in = UserInput()
usr_in.user_input()