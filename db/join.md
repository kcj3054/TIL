## join 

조인은 두 테이블에서 공통적인 칼럼이 있으면 join으로 연결 하는 것이다.

조인에는 left join, inner join이있다


#### inner join
- 교집합 칼럼을 통해서 join한다 

ex:
select ( from user)



#### left join
- join을 해서 왼쪽에 붙이는 것이다.
- 여기서는 왼쪽에 붙이는 것이기 때문에 순서가 중요하다 



#### subquery 



#### with 절 



#### self join

- 조직도 관계에서 셀프 조인을 할 경우가 발생한다. 

````mysql

DepartmentID	DepartmentName	ParentDepartmentID
1	            Headquarters	    NULL
2	            Sales	            1
3	            Marketing	        1
4	            East Coast Sales	2
5	            West Coast Sales	2
````

- ParentDepartmentID는 상위 부서를 가리킵니다. NULL이면 최상위 부서입니다.

- select d1.DepartmentID as DepartmentID, d1.DepartmentName as DepartmentName  from Department d1 left join Department d2 on d1.DepartmentID = d2.DepartmentID 

- self join은 재귀이다.  재귀또한 반복문 -> 이러한 것이 데이터양이 많아지게된다면 당연히 손해겠지만, 데이터 양이 많지않으면 괜찮은 방법일 것같다. 


#### self join 대안제 

- 프로젝트 -> 프로젝트의 하위 프로젝트 -> 또 하위 프로젝트 이러한 행위는 self join으로 해결 가능하지만 여기 대안제도 존재한다. 

- Project table에는 project에 대한 정보, 프로젝트이름, 생성시간, 생성자 아이디.. 

- ProjectUser table에는 project에 속한 유저정보를 가지는 것이다. 

- ProjectName으로 Join을 하면 해당 프로젝트정보와, 유저정보들을 가지고 올 수있다.  

- 부가 설명 부족. .