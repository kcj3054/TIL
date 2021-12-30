## 집계함수란?

- 집계함수는 숫자를 셀 수 있는 것들이다.


- 집계함수는 하나의 질의에 여러개를 동시에 사용할 수 있다

````
SELECT COUNT(*), SUM(GD_PRICE * GC_STOCK), MAX(GD_PRICE), MIN(GD)PRICE) FROM GOODS;
````


### COUNT

- 행들의 개수를 세기 위해서 count를 사용한다 , 

- 사용법 -> COUNT(칼럼 또는 * )

- 칼럼을 사용 할때와 * 를 사용할때 결과가 다르다

[##_Image|kage@cZaGB8/btrpgx7UFRC/LHjYvOTrrsJR6P9lemSdmK/img.png|alignCenter|width="100%"|_##]


- 위에서 상품 번호로 COUNT를 하면 5개가 나올 수도 있는데 NULL 값이 있는 상품이름 칼럼으로 COUNT를 하면 총 갯수가 3개가 된다.



### AGB

- 숫자형 값을 가진 행들의 평균값을 계산하기 위해서 AVG 사용

````
SELECT AVG(GD_PRICE) FROM GOODS;
````

### MAX, MIN

- 맥스 민도 동일하게 원하는 칼럼들을 넣으면 계산이된다.

- CF
	- 총 판매금액은 어떻게 계산이 될 것인가?
    - SUM 함수를 이용하면된다, SUM(PRICE * 갯수) 
    
    
    
    

## GROUP BY

- 상품의 수가 많을 경우 묶을 데이터를 찾기가 힘들고 실수 할 수도 있다. 그래서 동일한 값끼리 묶어서 그룹 단위로 집계하면 실수를 줄일 수 있다.

[##_Image|kage@spFWJ/btrplhbVcRP/G4GysE3sqm1i4dqIv3d4Z0/img.png|alignCenter|width="100%"|_##]



#### 질문 위의 그림에서 같은 연도에 같은 월인 주문들의 결제액의 총합을 구해라 

- GROUP BY를 이용하면 두 칼럼의 동일한 값의 그룹(년, 월)을 묶은 후 결제액의 총합을 구할 수 있다

````
SELECT OD_PAYMENT_YEAR, OD_PAYMENT_MONTH, SUM(OD_PAYMENT_AMOUNT) FROM ORDER_LIST 

GROUP BY OD_PAYMENT_YEAR, OD_PAYMENT_MONTH
````

#### 상품별 결제액의 총합을 구하는 구문

````
select sum(OD_PAYMENT_AMOUNT) FROM ORDER_LIST GROUP BY OD_GOODS_ID;
````

- 

## HAVING 조건식

- 그룹화된 결과물을 기준으로 조건식을 작성해서, 필터링 할 때 사용된다. 


- WHERE은 그룹화 이전의 필터링, HAVING은 그룹화 이후의 필터링이다. 


- 위의 '같은 연도에 같은 월인 주문들의 결제액의 총합을 구해라' 질의에서 금액인 3만원 이상인 조건이 들어갔으면 HAVING이 필요하다

````
SELECT OD_PAYMENT_YEAR, OD_PAYMENT_MONTH, SUM(OD_PAYMENT_AMOUNT) AS paymentAmount 

FROM ORDER_LIST 

GROUP BY OD_PAYMENT_YEAR, OD_PAYMENT_MONTH 

HAVING paymentAmount >= 30000;
````
    

