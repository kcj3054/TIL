## 만약 다형성을 사용하는 중 부모 소멸자에 virtual을 빠져먹으면?!!


````
while (true)
	{
		Player* p = nullptr;

		switch (rand() % 3)
		{
		case 0:
			p = new Knight();
			p->_hp = 100;
			p->_attack = 100;
			break;
		case 1:
			p = new Archer();
			p->_hp = 100;
			p->_attack = 100;
			break;
		case 2:
			p = new Mage();
			p->_hp = 100;
			p->_attack = 100;
			break;
		}		

		delete p;
	}
````


- 위에서는 다형성을 사용하고 new delete 짝도 맞췄는데 크래쉬가난다! 살펴보면 delete쪽에서 크래쉬가 발생했는 이유를 살펴보자 /


## 원인 소스
````
class Player
{
public:
	Player();
	Player(int hp);

	~Player();
````

- 부모의 소멸자에서 virtual를 빼게 되면 만약 아쳐였다면 아처를 delete를 하는 것이 아닌 Player를 delete하게 되고 계속해서 아처는 남게된다.  이상한 놈만 자꾸 지우게되는 현상이 발생하게 되는 것이다.!