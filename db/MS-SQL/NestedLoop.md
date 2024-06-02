## NestedLoop

-   NestedLoop는 이중 포문에서 안쪽 포문이 해쉬를 사용한다고 보면된다.

```
-- 실행계획을 보면 merge join을 사용한다고 나오있다
select *
from players As p
    INNER JOIN salaries As s
    ON p.playerID = s.playerID
    OPTION(LOOP JOIN)
```

[##_Image|kage@qpJEa/btryDPxJyiO/Sf3nS1stfJxm1BAqRID0H0/img.png|CDM|1.3|{"originWidth":841,"originHeight":767,"style":"alignCenter","width":null}_##]

````
위에서 
index seek가 발생했다는 것은 안쪽 부분인 인덱스를 활용해서 찾을 수 있다는 것이다. 
바깥쪽은 for인데  안쪽은 해쉬정도라고 (map) 생각하면 될 것같다. 
player를 먼저하고 inner join을 salary로 했는데 바깥이 salary인 이유는 db차원에서 그것이 더 빠르기때문이다. 
NL 할 경우 내부에 인덱스가 걸려있는지 유무가 가장 중요하다.   
````

-   NL은 최종 결과물 갯수가 정해져있을 경우 성능이 우수하다.. 알맞은 데이터 5개만 보고 바로 break로 나올 수 있기에 성능이 우수하다..

```
SELECT TOP 5 *
FROM players As p
    INNER JOIN salaries AS s
    ON p.playerID = s.playerID
```

-   결론NL은 OUTER 테이블의 ROW를 차례 차례 보면서 INNER 테이블에 랜덤 엑세를 한다. 