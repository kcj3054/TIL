## Container

- c++ STL(STANDARD TEMPLATE LIBRARY)에는 연속 컨테이너(sequence container), 연관 컨테이너(associate continaer)가 존재한다. 
  - 연관 컨테이너는 배열처럼 객체들을 순차적으로 보관하는 시퀀스 컨테이너
  - 키를 바탕으로 대응되는 값을 찾아주는 연관 컨테이너. associative container.  
- 우편배달부로 생각하면 우편을 넣는 우편함이 컨테이너라고 생각하자라는 비유가 아주 좋았다. 


## vector

- vector의 경우 현재 가지고있는 원소의 개수보다 더 많은 공간을 할당해 놓고있다.  그러므로 새로운 원소를 추가하게 된다면 새롭게 메모리를 할당할 필요없이, 이미 할당된 공간에 그 원소를 쓰기만 하면된다. 그러므로 대부분의 삽입에서 시간 복잡도는 O(1)이다. 
    - O(1)로 vector 맨 뒤에 새로운 원소를 추가하거나 지울 수 있다. 
    - 엄밀히 말하면 amortized O(1)이다. 분할 상환..
      - 일반적으로는 O(1)인데, 문제가 되는 상황은 공간을 다 채웠을 경우, 새로운 공간을 다시 할당한 후 기존의 맴버들을 다 복사하기에 O(N)이 걸리게된다. 
      - 이런 경우는 드물어서 amortized O(1)이라고한다. 



- 출처 : 씹어먹는 c++ 


## vector 예제 

````c++
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	//size  -> 실제 용량 중 사용하는 부분
	//capacity  -> 실제 용량

	//int* v = new int[3] {1, 2, 3};

	vector<int> v{ 1, 2, 3 };

	//stack<int> s ->  stack 사용할 때 재귀를 사용하면 stackoverflow가 발생하기도한다 그럴 때 
	// vector<int> v v.reserve(1024) 후 사용하면 효율이 더 좋다 

	// 미리 용량을 다 할당 받아 놓기때문에 속도에 향상이있다, 
	//v.reserve(1024)  // 메모리 용량 미리 할당 받음 , capacity 용량이 됌 
	v.resize(2);

	for (auto& e : v)
		cout << e << " "; 
	cout << endl;
	
	// 2 3 으로 출력 됌 , 속도를 높이기 위해 더 작은쪽으로 resize할 때 메모리는 반납하지 않는 상태로있는다.
	
	cout << v.size() << " " << v.capacity() << endl;

	cout << v[2] << endl; // run time error 발생 
	cout << v.at(2) << endl; // 


	int* ptr = v.data();
	cout << ptr[2] << endl; // 출력 가능 


	return 0;
}
````