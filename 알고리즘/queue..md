## queue

큐는 앞 뒤를 가리키는 것이 있어야한다 
왜냐? -> 앞은 head 뒤는 tail로 해서,  앞에서 값이 빠져나가고  뒤에서는 값이 들어오기때문입니다.

queue의 기능들은 enqueue, dequeue, peek, is_empty이 있습니다.


* enqueueu
값을 넣는 것입니다 뒤에서 넣으면됩니다 tail을 이용해서
new_node를 통해서 node를 하나 만들고 

````
    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return
````

* dequeue
제일 앞쪽의 값을 빼오는 것이 좋은거같습니다

* peek
제일 위층 값이 있는지 없는지 확인합니다

* is_empty
큐가 비었는지를 확인하는 것입니다 
간단하게 헤드가 있는지 없는지 보면됩니다