'''
leetcode 225
https://leetcode.com/problems/implement-stack-using-queues/
'''

'''

q=Queue()
q.put('x')  -> enqueue
q.get() -> dequeue
q.empty()
q.qsize()


-----------
Analysis
-----------

In 0512
When we push a value v to the stack -> we directly enqueue v to q1
when we pop the value from stack    -> step 1) move all values except last one from q1 to q2
                                       step 2) return q1.dequeue()
                                       
                                       
In 0513
When we push a value v to the stack -> step 1) move all values from q1 to q2, now q1 is emtpy
                                       step 2) q1.enqueue(v)
                                       step 3) move all values from q2 back to q1
when we pop the value from stack    -> we directly dequeue from q1

Solution 2) step 1) q2.enqueue(v)
            step 2) move all values from q1 to q2, now q1 is empty
            step 3) swap q1 and q2 (now q2 becomes q1)  

'''


from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        v = self.pop()
        if v != None:
            self.push(v)
        return v


    def empty(self) -> bool:
        return self.q1.empty()

    def size(self) -> int:
        return self.q1.qsize()




# our test code ---------------------
q = MyStack()
print("push ----------------")
q.push("eat")
q.push("sleep")
q.push("code")
print(q.size()) # 3

print("pop ----------------")
print(q.pop()) # code
print(q.top()) # sleep
print(q.pop()) # sleep
print(q.pop()) # eat

print(q.empty())
print(q.size())
