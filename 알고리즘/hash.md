### hash 알고리즘 

hash알고리즘은 검색을 빠르게 할 수 있는 알고리즘이다. 

hash(a) -> 이런식으로 해서 hash index를 찾아서 그쪽으로 값을 넣습니다

그리고 해당 index에 값이 있다면 해쉬 체이닝형식으로 뒤로 계속 해서 이어붙이면 한자리에 중복되는 현상을 막을 수 있습니다.

이 해쉬 체이닝 방법은 -> LinkedList방식으로 배열 타입을 잡아주면됩니다.


#### 값을 넣기 
put을 통해서 값을 넣기 위해서는 일단 값을 넣을 index를 만든 후 해당 index에 원하는 값을 넣으면됩니다.

index를 찾는 방법은 
-> index = hash(key) % len(self.items)
해쉬에 key 값을 넣은 후 그것을 해당 아이템의 길으로 나누면 index가 나옵니다 
````
    def put(self, key, value):
        index = hash(key) % len(self.items)

        self.items[index].add(value)
````


#### 값을 찾기 
찾을 때는 key를 알면 해쉬의 값을 바로 알 수 있습니다.
해당 인덱스에서 key를 넣어주면 바로 값을 가져올 수 있는거같습니다.
인덱스를 찾는 방법은 모두 동일합니다.

````
    def get(self, key):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # [(key1, value1), (key, value)]
        return self.items[index].get(key)
````

여기서 get을해서 가져오는 것은 아이템들이 연결리스트로 구현되어있는데 그 연결리스트에서 get을 구현한 함수가 있습니다.
items ->가 key,value로 들어간 상태입니다
````
def get(selft, key):
    for k, v in self.items:
        if key == k:
            return v
````




#### 모든 소스

````
class LinkedTuple:
    def __init__(self):
        self.items = list()


    def add(self, key, value):
        self.items.append((key,value))


    def get(self,key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)

        self.items[index].add(value)

    def get(self, key):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # [(key1, value1), (key, value)]
        return self.items[index].get(key)
````