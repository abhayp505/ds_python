
class Sorting:
    a={'name':'pathak', 'age':30, 'salary': 30000 }
    b={'name':'rakesh', 'age':32, 'salary': 80000 }
    c={'name':'pathak', 'age':20, 'salary': 60000 }
    d={'name':'sonu', 'age':29, 'salary': 35000 }
    e={'name':'Abhay', 'age':31, 'salary': 90000 }

    sorted_list =[a,b,c,d,e]

    def sortlist(self):

        print("list 1::", self.sorted_list)
        new_list=sorted(self.sorted_list, key=lambda d:(d['name'], d['salary']))
        print("\n")
        print("list 2::", new_list)

sorting_const = Sorting()
sorting_const.sortlist()

