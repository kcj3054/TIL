## deque란?

- 앞뒤로 넣고 뺄 수 있는 큐이다. 그래서 이름이 double - ended - queue이다.

- 데크는 시퀀스 컨테이너이다
    - 시퀀스 컨테이너는 데이터가 넣은순으로 나열되어있는 것이다.

- 데크는 벡터와 매우 비슷한데, 메모리 할당 정책에서 조금 차이가 있다.
    - vector는 크기를 넘게 된다면, 더 큰 capacity를 만든 후 이전값들을 새로 만든 공간으로 값을 복사하는 정책을 가진다.
    - deque는 크기가 가득 차면 앞에 넣으면 새로운 공간을 만든다 , 이전과 새로운 공간 두가지 모두를 사용한다 -> 바구니를 늘려간다고 생각하자!

## 참고 소스 

````
#include <iostream>
#include <deque>
using namespace std;

int main()
{
	

	deque<int> dq;
	dq.push_back(1);
	dq.push_front(2);

	cout << dq[0] << endl;
	

	/*
	* deque
	* 1. 중간 삽입 삭제는 안좋다
	* 2. 처음 .끝 삽입/삭제는 빠르다
	* 3. 임의 접근도 벡터처럼 지원이된다.
	*/

	return 0;
}


````