## 포인터 vs 참조


- 성능은 동일


- 편의성은 참조가 좋다

- 그러나 꼭 편의성이 참조가 좋다는 것은 아니다, 왜냐 포인터는 주소를 넘기니 확실하게 원본을 넘긴다고 알 수 있지만, 참조는 원본을 넘기는 것인지 확실하게 알 수는 없다


- 확실하게 원본을 고친다고 알 수없기에 마음대로 고칠 수 있어서 막는 방법이 const가 존재한다.




## 소스

````
#include <bits/stdc++.h>

using namespace std;


struct StatInfo
{
	int hp; // +0
	int attack; // +4
	int defencd; // +8
};

void CreateMonster(StatInfo * info) {
	info->hp = 100;
	info->attack = 8;
	info->defencd = 5;
}

void PrintInfoByPtr(StatInfo * info) {
	cout << "=====================" << endl;

	cout << "Hp : " << info->hp << endl;

	//const 붙일 때 

	//별 뒤에 붙인다면?


	//별 이전에 붙인다면? 

	//info[주소 값]    주소 값[데이터] 


}

void PrintInfoByRef(const StatInfo & info) {
	cout << "=====================" << endl;

	cout << "Hp : " << info.hp << endl;

}
int main() {

	StatInfo info;

	//포인터 vs 참조 대결
	// 성능 : 똑같음

	// 편의성 : 참조 승!

	// 1) 편의성 관련 -=> 꼭 장점은 아니다
	// 포인터는 주소를 넘기니 확실하게 원본을 넘긴다는 점 
	

	 
	CreateMonster(&info);

	PrintInfoByPtr(&info); //명시적으로 주소값을 넘김
	
	// 참조는 자연스럽게 모르고 넘길 수 있다. -> 원본을 고치는 건지 아닌지 잘 모를 수 있다 
	//마음대로 고친다면 => const로 마음대로 못 고치도록 막을 수도 있다
	PrintInfoByRef(info); //

	return 0;
}
````