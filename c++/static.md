
## static?

- struct와 class의 차이
    - struct는 기본적으로 public 접근제한자인데, class는 기본적으로 private 접근제한자이다.
- static(정적, 고정된) 
- 모든 마린이 공통적으로 공격이 있는데, a마린과 b마린의 공격력이 다르면 안된다. 
static을 사용하면 특정 객체에 해당하는 것이 아니라 마린이라는 class에 연관지을 수 있다! 

````
#include <bits/stdc++.h>

using namespace std;


class Marine
{

public:
	int _hp;

	static void SetAttack() {}


	static int s_attack; // 
};
int main() {

	Marine m1;

	Marine::s_attack = 10;
	Marine::SetAttack();
	return 0;
}

````