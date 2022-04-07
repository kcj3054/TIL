## 메모리 풀을 사용할려는 이유

- 메모리를 조금만 떼서 가져온다면 다시 커널레벨로 들어가서 메모리를 가져와야한다 이렇게 되면 컨텍스트 스위칭 비용이들어간다..

- 메모리가 짜잘하게 메모리를 요청하면 만약 사용한 메모리의 크기가 다를 수도 있다 예를들면
````
[a] [      ][b][    ][]..

이상황에서 a, b메모리를 해제한다면 , 쪼개진 상태로 메모리가 남아있다
근데 a + b보다 작지만 a, b 각각보다는 큰 메모리를 할당해야한다면 영역이 분산 되어있어서 문제가 발생한다. 
````


## Allocator (메모리 할당 정책)

- 메모리 할당정책에서.. new도 오버라이딩을 해서 사용할 수 있다 

````
void* operator new(size_t size) //size는 Knight의 사이즈를 말한다.
{
	cout << "new!" << size << endl;
	void* ptr = ::malloc(size);
	return ptr;
}
void operator delete(void* ptr)
{
	cout << "delete!" << endl;
	::free(ptr);
}
````

- 해당 정책을 사용하면 내가 원할대는 커스텀을 아닐때는 만들어진 new를 쓰고싶은데 그것이 안되어서 따로 Allocator쪽에서 나만의 정책을 만들 수 있다. 


### 커스텀 Memory 부분
````
#pragma once
#include "Allocator.h"

//Args 넘겨받을 인자.. 여러개를 받는다..., 베어릭 템플릿?
template<typename Type, typename... Args>
Type* xnew(Args&&... args)
{
	//메모리 영역할당하기 
	Type* memory = static_cast<Type*>(BaseAllocator::Alloc(sizeof(Type)));
    
	//placement new (메모리 위에 생성자를 호출해줘!)
	//가변인자를 전달하는 것 
	new(memory)Type(forward<Args>(args)...);

	return memory;
}

template<typename Type>
void xdelete(Type* obj)
{
	obj->~Type();

	BaseAllocator::Release(obj);
}


````

- 위에서 메모리를 할당할 때 xnew, 아닐 때 xdelete로 할 수 있다 여기서 메모리를 먼저 memory잡아 놓고 그 위에 생성자를 호출해돌라는 placement new문법을 사용하였다. 

- 위에서 template<typename Type, typename... Args>에서 인자쪽에 ...이 붙어있다 이부분은 가변인자 템플릿(Variadic template)이다. 갯수나 타입이 다양해도 여러개 받아주겠다는 것이다.  해당 인자를 받고 다시 전달할때는 forward로 전달한다. 

- 출처 : https://www.devoops.kr/143
- 루키스님의 서버 강의를 학습 후 작성하였습니다.