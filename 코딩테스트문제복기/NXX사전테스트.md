## Test1 

- Linked list 클래스 구현 후 해당 연결리스트를 이용해, 삭제 삽입 검색을 이용 


````c++
#include <iostream>

using namespace std;
/*
* ================================================
*                   Test1
* ================================================
*/
struct Node {
    int value;
    Node* next;

    Node(int val) : value(val), next(nullptr) {}
};

class CLinkedList {
public:
    CLinkedList() = default;
    ~CLinkedList();

    bool Insert(Node* target, Node* temp);
    Node* Find(int value);
    bool Delete(Node* target);
    void Print();

private:
    Node* head = nullptr;
};

CLinkedList::~CLinkedList() {
    
    Node* current = head;
    while (current != nullptr) 
    {
        Node* next = current->next;
        
        delete current;
        
        current = next;
    }
}

// target -> temp -> ( target -> next )
bool CLinkedList::Insert(Node* target, Node* temp) {
    
    if (target == nullptr) 
    {
        //list null check 
        if (head == nullptr) 
        {
            head = temp;
        }
        else 
        {
            //제일 앞으로 당김 
            temp->next = head;
            head = temp;
        }
    }
    else 
    {
        temp->next = target->next;
        target->next = temp;
    }
    return true;
}

Node* CLinkedList::Find(int value) {

    Node* current = head;
    
    while (current != nullptr) 
    {
        if (current->value == value) 
        {
            return current;
        }

        current = current->next;
    }

    return nullptr;
}

bool CLinkedList::Delete(Node* target) {

    if (target == nullptr || head == nullptr) 
    {
        return false;
    }

    if (target == head)
    {
        head = head->next;
        delete target;
        return true;
    }

    //target을 찾자
    Node* current = head;
    while (current->next != nullptr && current->next != target)
    {
        current = current->next;
    }

    if (current->next == target)
    {
        current->next = target->next;
        delete target;
        return true;
    }

    return false;
}

void CLinkedList::Print() {
    
    Node* current = head;
    
    while (current != nullptr) 
    {
        cout << current->value << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    CLinkedList list;

    Node* n1 = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(5);

    list.Insert(nullptr, n1);  // n1을 리스트의 첫 번째 노드로 삽입
    list.Insert(n1, n2);       // n2를 n1 뒤에 삽입
    list.Insert(n2, n3);       // n3를 n2 뒤에 삽입
    list.Insert(n3, n4);       

    // 전체 순회 
    list.Print();

    // Find 기능 테스트 
    Node* findNode = list.Find(2);
    if (findNode != nullptr) 
    {
        cout << "Found: " << findNode->value << endl;
    }

    // Delete 기능 테스트
    cout << "find node 제거 " << endl;
    bool result = list.Delete(findNode);
    if (result == true)
    {
        cout << "제거 완료" << endl;
    }
    else
    {
        cout << "없는 node 입니다" << endl;
    }

    // 전체 순회 
    list.Print();

    return 0;
}

````


## Test2

- 문자열구분 함수 구현

- sep : 구분자, out 구분된 문자열 저장하는 곳 


````c++

#include <iostream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>

using namespace std;

void Tokenizer_boost(std::string str, const char* sep, std::vector<std::string>& out)
{
	boost::split(out, str, boost::is_any_of(sep), boost::token_compress_on);
}

void Tokenizer(std::string str, const char* sep, std::vector<std::string>& out)
{
	int pos = 0;
	std::string token;

	std::cout << "sep : " << sep << endl;

	int delimiter_length = strlen(sep);

	while ((pos = str.find(sep)) != std::string::npos)
	{
		token = str.substr(0, pos);

		if (token.empty() == false)
		{
			out.push_back(token);
		}

		str.erase(0, pos + delimiter_length);
	}

	if (str.empty() == false)
	{
		out.push_back(str);
	}
}

int main()
{
	std::string str = "boost is a powerful c++";
	const char* sep = ",";
	std::vector<std::string> tokens;

	// Tokenizer_boost(str, sep, tokens);
	Tokenizer(str, sep, tokens);

	for (const auto& token : tokens)
		std::cout << token << std::endl;

	return 0;
}

````


- 위에서 원본 string 매개변수값을 최적화 하기 위해서 string_view를 사용하고싶지만 그렇게할 수가 없다 이유는 string_view는 소유권을 가지지 않으면 && 읽기 전용이기에..
  - 밑에 string.erase로 원본을 훼손 시키는 부분들이 존재한다 (쓰기 영역)

- boost:..

## Test3


- 1 ~ N까지 숫자를 더함     Thread M개를 생성해서 스레드 분산 시킨 후 성능 측정 


````c++
#include <iostream>
#include <thread>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <boost/chrono.hpp>

using namespace std;
/*
* ======================================================
*					TEST3
* ======================================================
*/


using ClOCK = boost::chrono::high_resolution_clock;

void PartialSum(int start, int end, int& result)
{
	for (int i = start; i <= end; ++i)
	{
		result += i;
	}
}

int main()
{

	int M = 100; // 1 ~ 100
	int N = 100; // thread 10개 

	std::vector<std::thread> threads;
	std::vector<int> results(N, 0);

	int chunk_size = M / N;
	int start = 1;

	auto start_time = ClOCK::now();

	for (int i = 1; i <= N; ++i)
	{
		int end = (i == N) ? M : start + chunk_size - 1;

		// results[i - 1] 참조 전달을 위해 std::ref 사용 
		threads.push_back(std::thread(PartialSum, start, end, std::ref(results[i - 1])));

		start = end + 1;
	}

	for (auto& t : threads)
	{
		if (t.joinable())
			t.join();
	}

	int sum = 0;
	for (auto result : results)
	{
		sum += result;
	}

	auto end_time = ClOCK::now();

	cout << "sum : " << sum << std::endl;

	// 일반적으로 출력하면 nanoseconds로 출력 됌 
	// cout << "총 소요 시간 : " << end_time - start_time << endl;

	auto total_time = boost::chrono::duration_cast<boost::chrono::milliseconds>(end_time - start_time);


	cout << "총 소요 시간 : " << total_time << endl;

	return 0;
}
````