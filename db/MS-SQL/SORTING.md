## Sorting

- db에서 정렬을 줄이는 것이 중요하다 
	- 왜 ? -> db는 데이터가 어마어마하게 많이 들어있기때문에 정렬이 한번 일어날때마다 매우 성능이 떨어진다. sorting이 언제 일어나는지 파악하고 줄일 수 있으면 노력하자!
    
    
- 정렬이 일어나는 경우는 MERGE SORT, ORDER BY, GROUP BY, DISTINCT, UNION, 이다 모두 확인해보자

### group by 
````
select college, COUNT(college)
from players
where college LIKE 'C%'
GROUP BY college
````
[##_Image|kage@dg4kTQ/btryz0AIdoy/HhSW7xcultlRKLGdfAvGa0/img.png|alignCenter|width="100%"|_##]

- COLLEGE 칼럼을 보면 인덱스가 걸려있지않다.

### union

````
select college
from players
where college LIKE 'B%'

UNION

select college
from players
where college LIKE 'C%'
````

- 만약 UNION ALL을 한다면 어떻게 될까?

[##_Image|kage@1yxKM/btryCljQ7NY/I0HHJ5ulhr2dOl32AnkMOK/img.png|alignCenter|width="100%"|_##]

- 쿼리를 봐도 중복이 안될 것같으면 UNION을 사용할 필요가 없다. UNION ALL을 한다면 SORTING이 없다.. 

## 결론

- 인덱스를 잘 활용한다면 정렬을 안해도된다. 머지 소트도 CLUSTERED INDEX가 있는 경우 이미 정렬이 되어있기 때문에 정렬을 따로하지않는다 또한 ORDER BY도 인덱스가 걸려있다면 SORTING이 필요없고.. union도 중복제거가 필요해서 그런데 조건을 보고 딱 봐도 중복이 없을 것같으면 UNION ALL을 사용해서 SORTING이 없도록 하면된다. 
