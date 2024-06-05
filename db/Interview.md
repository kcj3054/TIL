

1. sp 와 ad hoc query의 차이점?
- Ms SQL은 SP를 사용하게 된다면 PRECOMPIE이 된다는 장점이 있다.
그렇지만 현재 MYSQL 8.0 버전에서는 PRECOMPIE은 지원되지 않는다.

- 그렇다면 precompie의 이점은 무엇인가?

2. sql injection 방어하기 위해서 어떤 걸 해보았냐?

- parameterized query
    - 단순 쿼리로 입력 받은 데이터를 이어주는 것이 아닌 매개변수로 받는 데이터는 @ 파람으로 넣는 형태이다.
    - 예시로 c# dapper에서는 select * from account where id = @id and password = @password, new {id, password} 이러한 형태로 사용하기도 한다.
- stored procedure
    - SP 데이터는 DB에 저장되어있기에 INJECTION을 막는 것이 가능하다
    - sql injection에서 자주 사용되는 -- 용법도 적용 될 수 없는 이점이 있다.
    - mysql은 sp를 사용하게된다면 precompile 되지 않지만, ms sql은 precompile까지 되기에 성능상 단점도 사라진다.
- ORM
    - ORM을 사용한다는 것 자체로 INJECTION 공격을 막을 수 있다. 
    - 하지만 ORM을 사용하게 된다면 성능상 단점이 발생할 수 있고, DBA분들이 쿼리 모니터링을 하기 힘들어진다.


3. 잘못된 Join 사용 예를 하나 말해주세요

- Join을 사용할 때 대다수 잘못된 사용법은 full join을 사용하는 것이다. full join을 사용하게 된다면 

4. 동적 쿼리와 정적 쿼리의 차이점?
- 

5. transaction 격리 수준

- 