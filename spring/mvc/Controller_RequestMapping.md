### mvc구조 
[##_Image|kage@8czf5/btrlyYUSwDD/Yvo1PU4CSwL8YeeIM9ytv1/img.png|alignCenter|width="100%"|_##]

- 컨트롤러가 호출 될려면 핸들러  맵핑, 핸들러 어뎁터가 필요하다 

- HandlerMapping
	- 어노테이션 기반의 컨트롤러 @RequestMapping에서 사용하고 후순위로 스프링 빈이름으로 핸들러를 찾는다
    
- HandlerAdapter
	- 어노테이션 기반의 컨트롤러 @RequestMapping에서 사용,  후순위로 HttpRequestHandler 등등.. 에서 처리 
    
- 결론 컨트롤러가 호출 될려면 핸들러 맵핑과 핸들러 어댑터가 필요한데 그것들이 RequestMapping이 역할을한다.

### RequestMapping, Controller

- Controller로 하면 component스캔 대상이 되어서 빈으로 쪽쪽 부트가 가져간다.

- 그런데 여기서 한가지더 Controller는 RequestMapping을 사용할 수 있다는 것이다. RequestMapping을 편리하게 사용하도록 메소드를 구분해서 사용할 수 있다 그것이 -> GetMapping, PostMapping, DeleteMapping..이있다..


- RequestMapping은 요청 정보를 맵핑한다,


- RequestMappingHandlerMapping, RequestMappingHandlerMapping은 가장 우선순위가 높은 핸들러 매핑, 핸들러 어댑터이다 이 부분을 스프링빈중에서 @RequestMapping, or @Controller가 클래스레벨에서 붙어있으면 매핑정보를 인식할 수 있다.. ! 그래서 컨트롤러에 @Controller를 쓴다.. 



### ResController

- controller로 하고 return "hello"하면 hello로 되는 뷰리졸버가 뷰네임을 찾아주지만 restcontroller로 return "hello"하면 메시지 바디에 hello를 넣고 바로 반환해버린다. (RestController는 restapi만들 때 핵심 기능)
