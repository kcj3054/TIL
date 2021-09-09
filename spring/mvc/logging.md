#### 로그 확인법 

#### Slf4j
log는 lombok의 slf4를 사용하면 쉽게 사용 할 수 있다 
log의 디폴트값은 info이다. 
개발영역은 debug로 설정하고 , 사용자레벨에서는 info로 둔다 

#### log 출력할때 

log.info("info = {}", a)
이런 방법과 
log.info("info = " + a) 이런 방법이 있는데 위의 방식이 맞다 
왜냐  + a를 사용하면 만약 log를 시작 하지않아도 + a 연산을 시작학때문에 메모리 낭비가 되기 때문입니다.

#### logging level 설정
application.properties로 들어가서 설정 ~ 


cf : 
spring 'Jar'를 사용하면 resource/static/index.html를 사용하면 
index.html를 welcompage로 인식 할 수 있다 
