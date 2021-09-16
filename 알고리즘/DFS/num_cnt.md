#### 문제설명

이문제는 주어진 v백터안의 내용들을 +, - 연산을 통해서 원하는 결과값 k가 나 올수 있는 경우의 수를 파악하는 것이다.


#### 풀이법

1. 아주쉽다 

2. 그냥 dfs로 +는 경우, -는 경우를 다 살펴보면된다.ㄴ

3. 여기서 실수 -> 
밑의 구문에서 사이즈인 경우 && sum == k를 같이 보면 아닌경우는 무한루프에 빠지게된다. 
````
if (idx == v.size()) {
        if (sum == k) {
            ans++;
        }
        return;
    }
````

#### 소스코드

````

    #include <bits/stdc++.h>
    using namespace std;

    //5
    vector<int> v = { 1, 1, 1, 1, 1 };
    int k = 3;
    int ans, sum ;

    void dfs(int idx, int sum) {

    //cout << idx << " " << sum << " ";

    if (idx == v.size()) {
        if (sum == k) {
            ans++;
        }
        return;
    }
    
    dfs(idx + 1, sum + v[idx]);
    dfs(idx + 1, sum - v[idx]);
    
    }
    int main() {
    dfs(0, 0);
    cout << ans;

    return 0;
    }

````