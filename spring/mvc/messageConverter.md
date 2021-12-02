# MessageConverter

- 메시지 컨버터가 무엇인가? 메시티 컨버터는 @RequestBody, @ResponseBody의 내용을 통해서 알 수 있다 흔히 이것들은 엥 json으로 반환되는 것 아닌가? 아니다!

- @RequestBody에 살펴보자
	- Http의 Body에 값을 직접 넣는다
    - 이때 HttpMessageConverter가 작동한다. 객체처리,  StringHttpMessageConverter(문자처리), byte[]메시지컨버터
    - HttpMessageConverter는 인터페이스이다 여기서 canRead, canWrite메소드들이있다. -> 메시지 컨버터가 해당 클래스, 미디어 타입을 지원하는지 여부를 체크하는 것이다. 
    
- 스프링부트에서의 MessageConverter

	- 0순위로 Bye메시지컨버터, 1순위로 String메시지컨버터, 2순위로 MappingJackson2HttpMessageConver이다
    - 여기서 주의할 것은 Bye메시지컨버터와 String메시지컨버터는 클래스타입만 바이트, 스트링 체크만 하지 미디어 타입은 */* 로 모든 타입을 받을 수 있지만 MappingJackson2HttpMessageConver는 클래스타입과, 미디타입(application/json) 둘다 체킹이 엄격하다.
#### 예시 
````
content - type : application/json

@RequestMapping
void hello(@RequestBody String data) {}
````

- 만약 위의 내용이면 어떻게 작동할까?

- 메시지 컨버터는 첫째 byte[]메시지컨버터, 둘째는 StringHttpMessageConverter가 동작하고, 셋째는 MappingJackson2HttpMessageConver이다.. 


-  RequestBody가 String형이다 그런데 미디어 타입이 application/json이다. 이때는 StringHttpMessageConverter를 살펴보자
StringHttpMessageConverter는 클래스타입은 'String'인데, 미디어 타입은 */* 로 다 받아들인다는 것이다. 그럼 결과적으로 StringHttpMessageConverter가 작동한다. 




#### 예시 2 (안되는 예시)


````
content - type : text/html

@RequestMapping
void hello(@RequestBody HelloData data) {}
````


- 위의 내용은  메시지 컨버터가 받아 들일 수 없다 왜??? 왜냐 HelloData면 MappingJackson2HttpMessageConver가 작동하지 않나? 

- 그렇지 않다 왜냐? MappingJackson2HttpMessageConver는 클래스타입이 객체, HashMap일 경우이면서 && 미디어 타입이 application/json인 경우에만 가능하다  

- 그럼 위의 내용은 탈락한다. 


- 출처 : 김영한님의 spring mvc