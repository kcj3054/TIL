#### factory 패턴이란? 

팩토리는 말 그래도 공장이다 공장에서 무엇을 생성한다?? 

이것은 객체 생성을 팩토리 패턴에 위임해서 생성하는 것이다 

### why? 

이유는 객체를 new를 해서 생성을 하면  강력한 연결관계가 생긴다 
그것을 느슨하게 만들기 위해서 factory 클래스에 객체 생성을 위임하는 것이다. 



#### 참고 
(1)캡슐화 :
클래스에서 데이터와 함수를 하나의 그룹으로 묶는 것 

(2)의존 :
객체지향에서 객체의 관계 설정을 하는 것  or 객체가 서로 결합한다는 의미 

cf : 외부에 의해서 결합 관계가 생성되면 의존성 주입  
