#### 최대 최소

- cpp에서 최대, 최소 값들을 넣을 때 #include<climits>를 선언해서 INT_MIN, INT_MAX를 사용했다.
  
- 자바에서는 따로 선언할 필요가 없다 각 클래스마다 MIN_VALUE, MAX_VALUE가 존재한다 예시를 보자

	-  System.out.println(Integer.MIN_VALUE);
  	-  System.out.println(Long.MIN_VALUE);

#### to_string

-   cpp에서 숫자를 문자열로 바꿀 때 to\_string을 사용한다
    
-   자바에서는 Integer.toString()을 사용하거나, String.valueOf()를 사용하면된다
    
    -   예시
    -   1번 String str1 = String.valueOf(intValue1)
    -   2번 String str1 = Integer.toString(intValue1);

#### strip(), trim()

-   cpp에서는 split이 없어서 매우 불편했다 그러나 자바에서는 있다

-   출차 : [https://hianna.tistory.com/524](https://hianna.tistory.com/524) (to\_string)
    

[https://hianna.tistory.com/526?category=650599](https://hianna.tistory.com/526?category=650599) (strip, trim)