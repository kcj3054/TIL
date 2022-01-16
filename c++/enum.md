
#include <bits/stdc++.h>

using namespace std;


/*
   Enumerated type
   - Symbolic names to represent integer constants
   - Improve readability ans make it easy to maintain
   - enum-specifiler
*/

//enum을 사용하면 low, medium에 대응하는 값만 바꿔넣으면되서 유지보수에 좋다. !
enum levels
{
	low = 1000,
	medium = 500,
	high = 2000
};
//값을 설정을 안하면 0  1 2 3 4 5 이지 무조건 그런 것은 아니다!! 
enum pet
{
	cat,
	dog = 10,
	lion
};
int main()
{

	int score = 800; // user input
	if (score > high) cout << "high score" << endl;
	else if (score > medium) cout << "medium " << endl;
	return 0;
}