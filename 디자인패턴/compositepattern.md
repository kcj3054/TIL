## 소스
````
#include <iostream>
#include <conio.h>
#include <string>
#include <vector>

using namespace std;

//menu system..

/*
*	composite 패턴을 활용한 메뉴 만들기..
*	
* 우클릭시 나오는 메뉴칸에서 화살표로 새로운 메뉴가 나오느 것은 popupMenu이고, 옵션 같은 것은 MenuItem으로둔다..
* 
* 객체지향에서 중요한것은 공통이 되는 것을 담기 위해서 기반클래스로 담는 것이고, 
* 변하지않는 전체 중에서 변하는 것이 존재한다면 빼내주는 것이다..
*/

class BaseMenu
{
	string title;
public:
	BaseMenu(string s) : title(s) {}
	string getTitle() const { return title; }

	virtual BaseMenu* getSubMenu(int idx)
	{
		return 0;
	}
	virtual void command() = 0; 
};

class MenuItem : public BaseMenu
{
	int id;
public:
	//기반 클래스의 default생성자가 없다면 파생클래스에서 생성자를 부르는 것을 호출해줘야한다
	MenuItem(string s, int n) : BaseMenu(s), id(n) {}
	virtual void command() override
	{
		cout << getTitle() << endl;
		getchar();
	}
};

class PopupMenu : public BaseMenu
{
	vector<BaseMenu*> v;
public:
	PopupMenu(string s) : BaseMenu(s) {}

	void addMenu(BaseMenu* p) { v.push_back(p); }

	virtual void command() override
	{
		while (true)
		{
			system("cls");

			int sz = v.size();

			for (int i = 0; i < sz; i++)
			{
				cout << i + 1 << "." << v[i]->getTitle() << endl;
			}
			cout << sz + 1 << ". 상위 메뉴로.." << endl;
			//---------------------------
			int cmd = 0;
			cout << "메뉴를 선택하세요.." << endl;
			cin >> cmd;

			if (cmd < 1 || cmd > sz + 1) continue;

			if (cmd == sz + 1) break;

			//선택된 메뉴 실행.. 여기서 팝업메뉴인지, 메뉴 아이템인지 알 필요가 없다
			// 왜냐하면..기반 클래스에서 command를 순수가상함수로 정의 해놓고 파생클래스에서 모두 재정의했기때문..
			v[cmd - 1]->command();  //다형성이죠! 
		}
		
	}
	/*
	* getSubMenu()를 파생 클래스에만 넣을 것인가? 기반 클래스에도 넣을 것인가?
	* 파생클래스에만 넣으면 연쇄호출이 불가능하다... 반환 타입이 BaseMenu*인데 base에는 getSub이 없기때문.
	*/
	BaseMenu* getSubMenu(int idx)
	{
		return v[idx];
	}
};
int main()
{
	//MenuItem m("kcj", 11);

	PopupMenu* menubar = new PopupMenu("MenuBar"); // 다른 것을 포함하니 복합객체
	//composite, node
	PopupMenu* pm1 = new PopupMenu("화면설정");
	PopupMenu* pm2 = new PopupMenu("소리설정");
	MenuItem* m1 = new MenuItem("정보확인", 11);

	menubar->addMenu(pm1);
	menubar->addMenu(pm2);
	menubar->addMenu(m1);

	pm1->addMenu(new MenuItem("해상도 변경", 21));
	pm1->addMenu(new MenuItem("글자 변경", 22));

	pm2->addMenu(new MenuItem("음량 조절", 33)); // 다른 것을 포함하지 않으니 개별객체(Leaf)

	/*
	* composite 패턴..
	* 객체들은 트리 구조로 구성하여.. 부분과 전체를 나타내는 계층구조로 만들 수 있다..
	* 개별객체와 복합 객체를 구별하지 않고 동일한 방법으로 다룰 수 있다.. -> ()
	* 컴포지트는 재귀적인 느낌있다..
	*/

	menubar->getSubMenu(1)->getTitle
	//시작
	menubar->command();
	return 0;
}
````