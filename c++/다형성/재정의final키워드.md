
## const + override -> final 키워드

- 재정의 , override는 내가 최조의 함수를 만든 것이 아니라 부모의 것을 재정의해서 사용했다고 알려주는 키워드



## 소스 

````
#include <bits/stdc++.h>

using namespace std;
/*
//재정의 , override는 내가 최조의 함수를 만든 것이 아니라 부모의 것을 재정의해서 사용했다고 알려주는 키워드
   //final은 override + const이다
*/
class Creature
{

};

class Player : public Creature
{
public:
	virtual void Attack()
	{
		cout << "Player " << endl;
	}
};

class Knight : public Player
{
	void Attack() final // 
	{
		cout << "Knight " << endl;
	}
};
int main()
{
	Player * p1 = new Knight();
	p1->Attack();  // Knight출력 
	return 0;
}
````