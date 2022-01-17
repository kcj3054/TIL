## 다형성과 가상함수

-  다형성 => 겉은 똑같은데 기능이 다르게 동작하는 것이다.

- 오버로딩 : 함수 이름의 재사용 매개변수만 변화를 준 것이다 
- 오버라이딩 : 부모클래스의 함수를 자식 클래스에서 재정의 

- 일반 함수는 정적바인딩으로 컴파일 시점에서 결정이된다, 그러나 가상함수(virtual) 동적바인딩으로 묶이게된다.

- 가상함수 virtual을 사용하면 .vftable이 생기고 실제로 가리키는 곳이 생긴다. [vMove][vDie] 

*/

````
#include <bits/stdc++.h>

using namespace std;


class Player
{
public:
	virtual void Move() { cout << "Move Player! " << endl; }

public:
	int _hp;
};

class Knight : public Player
{
public:
	int _stamina;
};
class Mage : public Player
{
public:
	int _mp;
};

//Player 객체 주소의 첫번째에 가리킬 이정표를 가지고 있다고 생각하면된다.
void MovePlayer(Player *player)
{
	player->Move();
}
int main() {


	return 0;
}
````