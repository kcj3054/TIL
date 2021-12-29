# 빈 lifecycle

- 스프링 빈의 라이플  사이클
	- 스프링 컨테이너 생성 -> 스프링 빈 생성 -> 의존관계 주입 -> 초기화 콜벡 -> 사용 -> 소멸전 콜백 -> 스프링 종료


- 참고 객체 생성시, 초기화
	- 객체를 생성할 때 생성자에 값을 다 넣으면 되지 않냐? -> No!!!
	- 객체 생성과 초기화를 분리하는 것이 유지보수에 좋다.
    - 초기화는 생성된 값들을 활용해서 외부 커넥션을 연결하는 등 무거운 동작을 수행

#### BeanLifeCycleTest
````
public class BeanLifeCycleTest {

    @Test
    public void lifeCycleTest() {
        ConfigurableApplicationContext ac = new AnnotationConfigApplicationContext(LifeCycleConfig.class);

        NetworkClient client = ac.getBean(NetworkClient.class);
        ac.close();
    }


    @Configuration
    static class LifeCycleConfig {

        @Bean
        public NetworkClient networkClient() {
          
            NetworkClient networkClient = new NetworkClient();
            networkClient.setUrl("http://hello-spring.dev");
            return networkClient;
        }
    }

}
````

# PrototypeBean

- 스프링은 기본적으로 빈이 싱글톤으로 관리된다.

- 그러나 프로토타입으로 빈을 생성해도된다 이렇게 프로토타입으로 빈을 생성하면 스프링 컨테이가 빈을 모두 관리해주는 것이 아니라 소멸은 프로토타입 빈을 프로그래머가 관리를 해주어야한다.

- 스프링 컨테이너는 프로토타입빈을 만들어주고, di까지 해주고 끝낸다. @Predetroy가 호출되지 않는다. 


### 소스

````
public class PrototypeTest {


    @Test
    void

    @Scope("prototype")
    static class PrototypeBean {
        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init");
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }
    }
}
````