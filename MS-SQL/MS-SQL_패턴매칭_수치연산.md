## MS - SQL

-  MS - SQL는 이름에서 보듯이 MS에서 만든 것이고 대형 게임사에서는 많이 MS를 사용하는 추세라한다. 

- https://www.sqlskills.com/에서 야구게임 정보를 바탕으로 기능들을 익혀보는 공부를 할 것입니다.

````
USE BaseballData;





select nameFirst, nameLast, birthYear, birthCountry
from players
WHERE  birthYear = 1974 AND  birthCountry != 'USA' 
````


- 위의 구문에서 SQL은 영어라고 생각하자 한국어는 집에서 ~을 찾아주세요 이지만 영어는 찾아주세요가 먼저 나오게된다. SQL은 반대로 분석하는 것이 빠르다.

## 패턴 매칭

- 패턴에 따라서 정보를 찾을 수 있다 LIKE를 한후 % 와 _ 두가지가 사용된다.

- %는 임의의 문자열이지만, _는 임의의 문자 1개이다.

````
SELECT birthCity
FROM players
WHERE birthCity LIKE 'New%'
````

- birthCity가 New로 시작하는 문자열들이 출력되기 시작한다.. 

## 수치연산 

````
SELECT (2022 - birthYear) As KoreanAge
FROM players
WHERE deathYear IS NULL AND birthYear IS NOT NULL AND (2022 - birthYear) <= 80
ORDER BY KoreanAge
````

- SQL 구문에서 조건을 걸 때 WHERE에 조건을 거는데 위의 구문처럼 AND OR, >  <=로 조건을 걸 수 있다.. 

````
SELECT (2022 - birthYear) As KoreanAge
FROM players
WHERE deathYear IS NULL AND birthYear IS NOT NULL AND (2022 - birthYear) <= 80
ORDER BY KoreanAge
````

- 위의 구문에서 별칭을 사용하면 에러가 발 생할 수 있다 왜냐?? SQL의미가 해석되는 순서를 보자. 

- SQL 의미가 해석되는 순서는 FROM, WHERE, SELECT ORDER BY 이다 책상에서 무엇을 선택해라 어떤 순으로...


