## malloc이란?

- 동적 크기를 할당 받는 것인데. 메모리 할당 후 시작주소를 가리키는 포인터를 반환해준다. 


## *void란 ?

- 포인터는 주소를 가리킨다 근데 가리킬 주소가 아직 정해지지 않았다는 것이다 !


## headp overflow

- 유효한 힙 범위를 초과해서 사용하는 문제이다, malloc으로 할당 받은 메모리(heap 영역, 동적 배열)를 초과하면 발생한다 .

## Use-After-Free

- free(pointer)를 하면 날아간 메모리라고 건드리면 안되는데, m1->_hp = 100;로 건드릴 수 있는데 문제가 발생한다 



### 관련 소스

````
#include <bits/stdc++.h>

using namespace std;

class Monster
{
public:
	int _hp = 1000;
};
int main()
{
	void *pointer = malloc(1000);
	Monster *m1 = (Monster*)pointer;

	m1->_hp = 100;

	free(pointer);


	//new delete 버전 
	Monster *m2 = new Monster;
	delete m2;
	return 0; 
}
````