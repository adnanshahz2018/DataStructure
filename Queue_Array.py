

#  Implementation of queue using ARRAY in Python 

class queue_array:
    size = 0
    queue = []
    front = 0 
    back = 0 

    def __init__(self, size):
        self.size = size
        array = [0]*size
        self.queue = array

    def enqueue(self, value):
        if self.isFull():  return
        self.queue[self.back] = value
        self.back += 1

    def dequeue(self):
        if self.isEmpty():  return
        value = self.queue[self.front]
        self.queue[self.front] = -1
        self.front +=1
        print('The Dequeued is = ' , value)
        return value

    def show_front(self):
        print("The Front is = " , self.queue[self.front] )

    def isEmpty(self):
        if self.front == self.back:    
            print('Queue is Empty')
            return True
        return False

    def isFull(self):
        if self.back >= self.size -1 :
            print( "Queue is FULL ")
            return True
        return False

    def show(self):
        for i in range(self.front, len(self.queue)):
            print(self.queue[i], end="")
            if i < len(self.queue) - 1: print(" , ", end="")
            else: print()


if __name__ == "__main__":

    qa = queue_array(5)
    user_input = input('Operation: ')

    while (1):
        if user_input == 'e':
            user_input = input('Number/Value: ')
            qa.enqueue(user_input)

        elif user_input == 'd':
            qa.dequeue() 

        elif user_input == 's':
            qa.show()

        elif user_input == 'l':
            qa.isFull()

        elif user_input == 'f':
            qa.show_front()
            
        elif user_input == 'y':
            if not qa.isEmpty():
                print('Queue is *NOT* empty')

        user_input = input('Operation: ')
        if user_input == 'q' or user_input == 'Q':  break

