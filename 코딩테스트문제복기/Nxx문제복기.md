

# 구슬 문제

- 주어진 문자열(M)은 꿰어진 구슬 .. S번째 구슬부터 E번째 구슬까지 남도록 양쪽을 자른 후 남은 구슬의 합을 필요로한다.

- N(M의 길이), M(구슬의 문자열), Q(자를 위치의 개수), s1 e1, s2 e2..

## 테케 

````
20
111*213*22*3*132**12
4
3 8
10 18
0 11
4 9

````


### 테케 1의 정답 
````
6
9
10
0
````


### 풀이방법 

- n의 크기가 10만이라서 매 질문마다 구간에 적합한 구슬의 누적 갯수를 찾는 것은 불가능함 왜냐 O(n^2)이라서..

- O(1)이나 , O(n)처리로 진행해야할 것같다.. 

- 해당 구간에 대한 갯수를 구하는 것은 누적합이 존재한다. 

- 해당 문제는 전처리로 O(N)을 진행한 후 질의를 처리하는 부분은 O(1)로 진행하면된다.

- 전처리하는 과정에서 해당 위치에서 가장 가까운 매듭들을 구해주면디는 것이다. 밑의 in lknot는 왼쪽에서 가장 가까운 매듭이고, rknot은 각 위치 기준 오른쪽에서 가장 가까운 매듭이라고 생각하면된다.  이러한 부분들을 전처리로 구해주면 끝..  

### 소스 


````c++

#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MAX_N = 100030;

string s;
int sum[MAX_N];         // 각 위치까지의 구슬 누적합
int lknot[MAX_N];       // 각 위치에서 가장 가까운 왼쪽 매듭(`*`)의 위치
int rknot[MAX_N];       // 각 위치에서 가장 가까운 오른쪽 매듭(`*`)의 위치

int main() {
    int n, q;
    cin >> n >> s;

    if (s[0] == '*')
    {
        sum[0] = 0;
    }
    else
    {
        sum[0] = s[0] - '0';
    }
   
    for (int i = 1; i < n; i++) 
    {
        if (s[i] == '*') 
        {
            sum[i] = sum[i - 1];  // 매듭이면 누적합 변화 없음
        }
        else 
        {
            sum[i] = sum[i - 1] + (s[i] - '0');  // 구슬 가격을 누적합에 더함
        }
    }

    // 왼쪽 매듭 위치 
    // 1 2 3 4 .. n까지 진행하면서 매듭을 갱신해 나아가는 것이다.. 
    int lastLeftKnot = -1;  // 현재까지 가장 가까운 왼쪽 매듭 위치
    for (int i = 0; i < n; i++) 
    {
        if (s[i] == '*') 
        {
            lastLeftKnot = i;
        }
        lknot[i] = lastLeftKnot;
    }

    // 오른쪽 매듭 위치 
    int lastRightKnot = n;  // 현재까지 가장 가까운 오른쪽 매듭 위치
    for (int i = n - 1; i >= 0; i--) 
    {
        if (s[i] == '*') 
        {
            lastRightKnot = i;
        }
        rknot[i] = lastRightKnot;
    }

    // 질의 처리
    cin >> q; 
    for (int i = 0; i < q; i++) 
    {
        int s, e;
        cin >> s >> e;  // 질의 입력

        int l = rknot[s];  // s 위치에서 가장 가까운 오른쪽 매듭 위치
        int r = lknot[e];  // e 위치에서 가장 가까운 왼쪽 매듭 위치

        if (l >= r) 
        {
            cout << 0 << endl;  // 구슬이 남아있지 않음
        }
        else 
        {
            if (l == 0)
            {
                cout << sum[r] << endl;
            }
            else
            {
                cout << sum[r] - sum[l - 1] << endl;
            }
        }
    }

    return 0;
}

````


# 금칙어 문제 


# 하이퍼 웜홀 문제 

- 여러 도시들이 서로 연결되어있음,  연결된 부분끼리는 서로 여행이가능..

- 자기별을 포함해서 연결된 별들로 여행 가능한 것 중 N = 10이라면 (N이라하면 갈 수 있는 별의 횟수 하나의 그룹 내에서)


- 별들의 ID는 유니크하게 표시되는데 21억XX까지 가능하다 INT 최대범위 ..


## 풀이 방법 

- 위 문제들은 처음에 bfs로 풀면되지 않을까? 하다가 int 범위 node수가 너무 많아서 그것을 배열에 할당하다가 segmentation falut가  발생함...

- 그 이후 bfs는 적합하지않고 해당 문제를 풀기위해서는 그래프가 그룹핑되어있는 union - find를 생각 함 union - find에서도 엄청 헤맸는데 findParent로 부모를 찾는 부분에서 무한 재귀가 발생한 후 스택 영역이 가득차서 또한 segmentation fault가 발생 함.. 

- 여기서 vector -> unordered_map으로 전환을 했다.. 왜냐하면 vector는 공간을 미리 다 할당받아 놓는 것이고 unordered_map은 동적으로 공간을 할당 받는 것이다. 

- 모든 node 들을 기록했을 때 문제가 발생하는 부분도 존재했다.
  - 입력 받을 때 단순하게 자주 사용하던 vector를 이용했는데 vectorfmf 사용함에 문제는 중복되는 node들이 들어갔을 경우 해당 문제들을 다시 예외처리하는 과정이 필요했다. 이럴 때 필요한 자료구조가 set을 이용하는 것이었다 set은 중복을 허용하지 않기때문에 해당 입력 처리에 적합했다.. 

## 풀이 소스 

````c++

#include <bits/stdc++.h>
using namespace std;
int cnt, N, t1, t2;
// const int NODES = 2147483647;
//각 컴포넌트들이 몇개의 별들을 이루고있는지 체크 component 
unordered_map<int, int> parent;
int findParent(int x)
{
    if(parent.find(x) == parent.end())
    {
        parent[x] = x;
    }
    
    if(parent[x] == x)
    {
        return x;
    }
    return parent[x] = findParent(x);
}
void Merge(int x, int y)
{
    int rootX = findParent(x);
    int rootY = findParent(y);
    
    if(rootX != rootY)
    {
        parent[rootY] = rootX; 
    }
}
int main() {
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    vector<int> nodes;
    
    int result = 0;
    //하이퍼 웜홀의 총 갯숫
    
    cin >> cnt >> N;
    
    /*
    //미리 할당 받을 필요없어짐 
    for(int i= 0; i < NODES; ++i)
    {
        parent[i] = i;
    }
    */
    
    for(int i = 0 ; i < cnt; ++i)
    {
        t1 = t2 = 0;
        cin >> t1 >> t2;
        
        // 디버깅 출력 추가
        cout << "Processing nodes: " << t1 << " " << t2 << endl;
        
        // 노드가 처음 등장할 때 초기화
        if (parent.find(t1) == parent.end()) {
            parent[t1] = t1;
        }
        if (parent.find(t2) == parent.end()) {
            parent[t2] = t2;
        }
        
        Merge(t1, t2);
        
        //나중에 카운팅위한 
        nodes.push_back(t1);
        nodes.push_back(t2);
    }
    
    // pair 어떤 집합의 몇개가 존재한다 
    // 갯수를 찾자 
    // rootNode, count
    unordered_map<int, int> component;
    for(auto num : nodes)
    {
        int p = findParent(num);
        component[p]++;
    }
    
    for(auto &node : component)
    {
        if(node.second <= N)
        {
            result += node.second;
        }
    }
    
    cout << result << endl;
    
    return 0;
}

````

# 아빠랑 아들 이름 맞추기 놀이 


## 풀이 방법 

- 가능한 모두 경우의 수를 탐색하면되는 것이다.

# DP 

- dp문제가 나왔다.. 딱 봐도[i]를 할 수 있는 경우의 수를 찾는 문제.. 
  

- dp는 점화식 을 세운 후 해당 점화식에 맞춰서 그대로 풀이를 코드로 옮겨 적으면된다. 

- dp[i]를 i번째 칸에 도달할 수 있는 방법의 수로 정의합니다

- dp[i] = dp[i - d1] + dp[i - d2] + ... + dp[i - dn] (단,

- 각 칸 i에 대해, 주사위에서 나온 가능한 모든 값을 사용하여 그 이전의 칸에서 현재 칸으로 이동할 수 있는 방법의 수를 합산합니다.

## 풀이

````c++

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int M, n;
    cin >> M >> n;

    vector<int> dice(M);
    for (int i = 0; i < M; ++i) {
        cin >> dice[i];
    }

    vector<int> dp(n + 1, 0);
    dp[0] = 1;  // 시작점

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < M; ++j) {
            if (i - dice[j] >= 0) {
                dp[i] += dp[i - dice[j]];
            }
        }
    }

    cout << dp[n] << endl;

    return 0;
}

````