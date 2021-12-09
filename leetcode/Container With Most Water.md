
#### 문제 
https://leetcode.com/problems/container-with-most-water/

#### 풀이

- 다 비교하면 시간복잡도가 터져버린다. 여기서 투포인터로 비교하면된다 

- 가로는 le - ri이고 높이는 두곳중에서 작은 값이다. 이렇게 비교하다가 le ri둘중에서 작은 값을 선택해서 범위를 좁혀나가면서 현재 정답값과 비교하면서 갑을 갱신하면된다. 

#### 주의 
- 틀린점이 투포인터에서 값을 비교할 때    if(height[le] < height[ri]) 값을 비교해야하는데 처음에는 인덱스를 비교해서 알 수 없는 오류에 빠지게 되었다.

#### 소스 


````
class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int le = 0, ri = height.size() - 1, ans = 0;
        
       // cout << height[le] ;
        
        while(le < ri) {
            int mVal =  min(height[le] , height[ri]);
           // cout << le - ri << " " << mVal << endl;
            int tmp = abs(le - ri) * mVal;
            ans = max(ans, tmp);
           // cout << ans << endl;
            if(height[le] < height[ri]) le++;
            else ri--;
        }
        
        return ans;
    }
};
````
