## pk 중요성

- PK가 커지면 일반 인덱스의 크기도 커집니다. 이는 성능에 악영향을 미칠 수 있습니다.
- 같은 테이블에서 pk의 타입만 a는 bigint, b는 varchar(50)으로 했을 경우 a일 경우 테이블의 크기가 커지게됩니다.
- 또한 인덱스의 크기가 커지는데 이유는 일반 인덱스의 leaf level 페이지들에는 pk가포함되어있어서 그렇다. 그렇게되면 pk가 커지면 당연히 인덱스 크기도
커지겠지 또한 RDBMS가 B TREE로 구성되어있으니 크기가 커지면 트리의 높이가 높아지면서 검색에도 시간이 더 소요될 수밖에없다..  
- 테이블의 크기가 커지면 작업 시 io 작업이 많다. 
- 간결하면서 조회에 자주 사용되는 것을 사용하는 것이 맞다.
- 의미가 없는 PK를 인조식별자라고도한다. (account_uid)
- 
````
SELECT
    table_name,
    ROUND((data_length + index_length) / 1024 / 1024, 2) AS size_in_mb
FROM
    information_schema.tables
WHERE
    table_schema = 'game' AND
    table_name = 't_abnormality';

````


## Auth 네이밍 의미 (폴더 위치 옮김 필요) 
- Auth라는 이름을 많이 사용하다, 로그인 서버나 인증 서버에서 Auth를 많이붙이기도했다.
- https://news.hada.io/topic?id=15051 해당 토픽을 살펴보면 Auth는 의미를 모호하게한다고 적혀있다 authentication, authorization 인증 권한 모두 authxx로 시작해서 auth만으로는 어떤의미를 가지는지 모호하는 것이다. 
	- 게임에서 로그인을 할 때 Auth 서버보다는 LoginServer가 더 나은 듯하다. 
- 해당 링크에서는 Auth 대신 인증인 login과 권한 부여인 permission으로 제안하고있다.


## pk, 외래키 

- 외래키를 걸지 말자는 주장이있었다. 

- 실제로 아는 만큼 보이는 데이터 베이스 설계와 구축라는 책을 살펴보다보면 예전에는 성능 상이유로 fk를 걸지 않았다고한다 그때는 cpu성능이 현재랑 다르게 낮았고, 또한 fk를 적용한 컬럼에 index를 걸지 않아서 발생한 성능 이슈였다. 
    - 외래 키가 자주 조인에 사용된다면, 인덱스가 없을 경우 조인 성능도 크게 저하될 수 있습니다.
    - 

- 데이터 무결성을 위해서는 pk fk는 무조건 설정해야한다. 


````mysql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
````

- 부서, 직원 사이의 관계에서 1 : N이다.. 직원 테이블에 fk가 걸려있지만 index는 설정되어있지않다.
    - 이 경우 employees 테이블에 데이터를 삽입하거나, 삭제할 때 mysql은 department_id 값이 departments에 존재하는지 확인하기 해야한다. 만약 데이터가 100만개면 100만번 확인하는 과정이필요하다. 
    - 확인할 때 index가 없다면 테이블 풀 스캔이 작동한다, 해결하기위해서 index 설정.. -> create index idx_department_id on employees(department_id);

- 결론은 index 설정을 잘 한다면 fk를 거는 것에 성능상 문제가 없다. 

- 