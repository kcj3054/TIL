## 가상메모리, 

- 우선 stompAllocator를 보기전에 가상메모리를 살펴보겠습니다.

- 일반적으로 코딩에서 사용하는 메모리 주소는 물리적 주소가 아닌라 랩핑된 가상메모리 주소이다.

- 가상 메모리에도 정책을 둘 수 있는데 만약 4GB를 할당하면 메모리를 관리할 때 페이지 단위로 관리를 한다  비유를하면 아파트 분향 모형처럼 생각하는 것이 페이지이다.   

- 윈도우 PAGE는 기본적은 4KB로 고정되어있습니다.

- VirtualFree를 사용하면 가상메모리 부분을 FREE하는 것이 아니라 실제로 할당 받은 메모리 부분을 지우는 것이라서 메모리 오염을 방지할 수 있다. 



##  stompAllocator

- stompAllocators는 언리얼에서도 사용한다고 알고있습니다.  실제로 물리적메모리를 할당하거나 지워서 오염된 메모리영역을 건드리지 않도록 하기 위해서 사용합니다..


### class StompAllocator

````
class StompAllocator
{
	enum { PAGE_SIZE = 0x1000 };

public:
	static void*	Alloc(int32 size);
	static void		Release(void* ptr);
};
````
- 위에서 PAGE_SIZE는 0x1000이다.

### StompAllocator::Alloc부분

- 실제로 사용할 영역은 size이다 . 
````
void* StompAllocator::Alloc(int32 size)
{
	//size(실제로 사용될 공간), dataOffset은 오버플로우를 잡아주기 위해서 띄우는공간
	//
	const int64 pageCount = (size + PAGE_SIZE - 1) / PAGE_SIZE;
	const int64 dataOffset = pageCount * PAGE_SIZE - size;

	//시작 주소가 0x1000 배수로 할당되고
	void* baseAddress = ::VirtualAlloc(NULL, pageCount * PAGE_SIZE, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
	return static_cast<void*>(static_cast<int8*>(baseAddress) + dataOffset);
	//[                  [   ] -> 뒷부분에 위치 할 수 있다
 }
````

- 여기서 오버플로우를 잡아주기 위해서 offset만큼 띄어준 다음 그 다음 공간에 data를 사용한다. [  offset][data] 이런 느낌

- 실제로 할당 받는 부분은 baseAddress부분이고 void* baseAddress = ::VirtualAlloc(NULL, pageCount * PAGE_SIZE, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE); 여기서 페이지카운트 * 페이즈 사이즈로 할당

- 사용하는 부분은 offset을 띄운 부분부터 사용 return static_cast<void*>(static_cast<int8*>(baseAddress) + dataOffset);


### void StompAllocator::Release(void* ptr)

````

void StompAllocator::Release(void* ptr)
{
	//받아준 ptr은 뒷부분이다 그래서 Release할대는 첫시작부터해야한ㄷ.

	const int64 address = reinterpret_cast<int64>(ptr);
	const int64 baseAddress = address - (address % PAGE_SIZE);
	::VirtualFree(reinterpret_cast<void*>(baseAddress), 0, MEM_RELEASE);
}
````

- 여기서 Release 부분이 많이 헷갈렸다. 원래 baseAddress는 밑의 사진이지만.

[##_Image|kage@Yg8rI/btryTOr4nKK/siXpGveoyNGBoqy9zqCIZ0/img.png|alignCenter|width="100%"|_##]

- offset만큼 띄웠기 때문에 + offset만큼 뒤에 위치하게된다. 

- 그래서 baseAddress를 계산할때 현재 address는 ptr의 위치라서 offset만큼 당겨야해서 - (address % PAGE_SIZE)가 된다. 

- VirtualFree 통해 알게된 baseAddress를 지운다. 


- 루키스님의 서버강의를 학습 후 작성하였습니다. 