#### 문제 설명 

이 문제는 단어가 예시로 "abcbc"가 있을 경우 이 것이 팰린드롬인지 아닌지를 파악하는 것이다.



#### 풀이법 

1. 일단 단어가 1개이면 무조건 팰린드롬이다

2. 첫과 끝을 비교하면서 점점 줄여나가는 방향으로 가면 좋다

3. 그럼 계속해서 넘어오는 문자열의 첫과 끝을 계속 비교하는 식으로 dfs를 진행해주면된다.


#### 코드 

````
#include <bits/stdc++.h>

using namespace std;

string input = "abcba";


bool recur(string v) {
   
   if (v.length() <= 1) return true;

   if (v[0] != v[v.length() - 1]) return false;

   string newV = "";
   for (int i = 1; i < v.length() - 1; ++i) {
      newV += v[i];
   }
   //cout << newV << endl;
   return recur(newV);
}

int main() {

   cout<< recur(input);
   return 0;
}
````