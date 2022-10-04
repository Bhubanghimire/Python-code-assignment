
class Stack:
    def __init__(self):
        self.item = []
        self.pos = -1

    def is_empty(self):

        if self.item == []:
            return False
        else:
            return True

    def push(self,data):
        self.item.append(data)
        self.pos +=1
        # print("one data added")
    
    def pop(self):
        # print("one data remove")
        
        if self.is_empty():
            data = self.item.pop()
            self.pos -=1
            return data
           
        else:
            return 0
            
        

    def postfix_evaluate(self,items):
        result = 0
        for item in items:
            if item == "+":
                item1=self.pop()
                item2 = self.pop()
                result = item1+item2
                self.push(result)

            elif item == "-":
                item1=self.pop()
                item2 = self.pop()

                result = item1 - item2
                self.push(result)

            elif item == "*":
                item1=self.pop()
                item2 = self.pop()

                result = item1*item2
                self.push(result)

            elif item == "/":
                item1=self.pop()
                item2 = self.pop()

                result = item1/item2
                self.push(result)

            else:
                self.push(item)
        return result


stack_obj = Stack()
items =[1, 2, 3, 4, 5, 6, '*', '*', '*', '*','*']
result = stack_obj.postfix_evaluate(items)
print(result)

