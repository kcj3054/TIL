## Adapter패턴?

- 어댑터패턴은 말 그래도 콘센트 어댑터를 생각하면 편리하다 A와 B가 맞지 않지만 그것을 연결해주기 위해서 중간에 어댑터를 두는것과 같다..


## STL과 Adapter 패턴..

- Container Adapter는 컨테이너 인터페이스를 수정해서 stack, queue, pq를 제공한다.. 

````
list를 포함한다 포함을 이용한 방법..
template<typename T, typename Container = list<T>> 
class Stack
{
	Container st;
public:
	void push(const T& a) { st.push_back(a); }
	void pop() { st.pop_back(); }
	T& top() {	return st.back(); }
};
int main()
{
	Stack<int, vector<int> > s1;
	Stack<int> s2;

	return 0;
}
````

- list를 포함해서 사용한다. 커스텀으로 구현된 Stack인데 list의 기능을 사용할 수가 없다 왜냐하면 list는 private으로 막혀있고, public의 기능은 진짜로 stack에서 필요한 부분만 list 것을 추출해서 사용 중이기때문이다.. 

- 여기서 list의 기능을 수정해서 사용했기에 container adapter라고한다.. 

## Adapter패턴 예 (도형편집기 사용..)

````
class TextView
{
	string data;
	string font;
	int		width;

public:
	TextView(string s, string fo = "나눔", int w = 24) : data(s), font(fo), width(w) {}
	void Show() { cout << data << endl; }
};


class Shape
{
public:
	virtual void Draw() { cout << "Draw Shape" << endl; }
};

class Text : public TextView, public Shape
{
public:
	Text(string s) : TextView(s) {}

	virtual void Draw() { TextView::Show(); }

};

//개체 어댑터 
class ObjectAdapter : public Shape
{
	TextView* pView;
public:
	ObjectAdapter(TextView* p) : pView(p) {}

	virtual void Draw() { pView->Show(); }
};

int main()
{  
	vector<Shape*> v;
	for (auto a : v)
		a->Draw();
	return 0;
}
````

- 위의 예제에서 vector<Shape*> v;에 들어갈려면 기반 클래스가 Shape이어야한다. 

- 여기서 Text 클래스의 기능을 TextView에서 가지고 있는데 TextView만 상속받으면 vector<Shape*> v; 에 넣을 수가 없다...

- 이 문제를 해결하기위해서 adapter패턴에는 포함을 사용하거나, 다중상속을 받는다... 

- 위의 Text클래스에서 TextView와 Shape 두가지 모두를 상속 받고있다.. 그러면서 Shape의 virtual을 구현하되 구현부에서 TextView::Show()를 사용하면된다.. 이부분이 adapter의 핵심이다..!! Text안에 TextView의 기능을 끼워넣었다.. 


### 어댑터의 종류

- 개체 어답터
	- 객체의 인터페이스를 변경한다.
    - 구성을 사용하는 경우가 많다.
    
- 클래스 어댑터
	- 클래스의 인터페이스를 변경한다.
    - 다중 상속 or 값으로 포함하는 경우가 많다.
    - 이미 존재하는 개체의 인터페이스는 변경할 수 없다..
    