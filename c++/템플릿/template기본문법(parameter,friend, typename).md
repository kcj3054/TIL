
# template의 parameter


## template parameter로 template받기.. 

- 템플릿의 인자로 non-type, type, template을 받을 수 있다 템플릿의 인자로 템플릿을?! 가능하다.

### 예시

````
template<typename T> class list{};


template<typename T, template<typename> class C  > 
class Stack
{

};
int main()
{
	//list s1; // list는 타입이 아니고 템플릿이라서 에러! 이렇게할려면 생성차를 통해서 타입을 deduction하도록해야한다.
	list<int> s2;  //list<int>는 타입..

	Stack<int, list > s3;
	return 0;
}
````

- 위의 소스에서 list를 보면 list는 템플릿 클래스이다.

- main부에서 Stack<int, list > s3으로 하나는 int타입을 하나는 템플릿을 받고있다.   그럼 Stack에서 그렇게 만들면된다.

- Stack의 template 인자에서 template<typename> class C 는 list의 앞부분이다. 그래서 이것은 템플릿의 x를 받겠다는 것이다. 
  
- 또한 main함수 부분을 보자! list s1을 하면 list는 타입이 아니라 템플릿이다. , list<int> s2를 하면 list<int>는 타입이다. 
  

## default parameter..
  
````
  template<typename T = int, int N = 10>
class Stack
{

};

int main()
{
	Stack<int, 10> s1;

	Stack<int> s2;

	Stack<> s3;
}

  
````
  
- 위의 소스는 기본값을 설정한 것이다.. Stack<> s3으로 하면 값을 지정하지 않고 default값으로 사용하겠다는 의미이다..
  
  
  
## typename 