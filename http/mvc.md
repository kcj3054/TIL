#### mvc 패턴

mvc 패턴이란 -> model view controll이다 

이 패턴이 나오는 이유는 이전에 jsp, servlet에서 한 곳에 너무 많은 기능을 두게 되면 유지 보수가 어려워진다 
그래서 jsp는 view를 렌더링 하는 것에 특화가 되어있으니 그곳 집중을 하고 비지니스로직은 servlet에서 담당하는 것이 좋다 



#### mvc 담당 분야 

* controller

http요청을 파라미터로 받아서 검증하고, 비지니스 로직을 실행한다 그리고 뷰에 전달할 결과 데이터를 조회해서 모델에 담아 둡니다. 
-> controller는  클라이언트 요청을 받고 그에 해당 하는 것들을 처리한다.

* model 
1. 뷰에 출력할 데이터를 담아둔다
2. 뷰에 필요한 데이터를 담아줘서 뷰는 비지니스로직이나 데이터 접근을 알 필요가 없다 

* view

1. model에서 화면에 출력할 것들을 가져와서 화면에 그리는 것을 집중한다 



#### frontController

frontController가 나오기전에는 각각의 컨트롤러가 클라이언트의 요청을 처리하고 있었습니다 

그러나 이 중복되는 것을 하나로 모을 수 있는 것이 frontController입니다.

1. 프론트 컨트롤러 서블릿 하나로 클라이언트의 요청을 받음
2. 프론트 컨트롤러가 요청에 맞는 컨트롤러를 찾아서 호출
3. 입구를 하나로!
4. 공통 처리 가능
5. 프론트 컨트롤러를 제외한 나머지 컨트롤러는 서블릿을 사용하지 않아도 됨

스프링 mvc의 DispatcherServlet이 이런 frontController로 구현이 되어있습니다

#### viewResolver
컨트롤러가 반환한 논리 뷰 이름을 실제 물리 뷰 경로로 변경한다. 그리고 실제 물리 경로가 있는 MyView
객체를 반환한다

출처 : 김영님 스프링 mvc1
