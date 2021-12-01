q : 스레드 세이프한가라고 들어봤나요?

a : 멀티스레드 환경에서 주의 해야한다. ! 대표적으로 스프링에서 싱글톤을 자동으로 객체를 생성할 때 주의해야한다 .

-   예시를 한번 살펴보자 밑의 예시는 private한 생성자를 이용하고, static 메소드를 만든 것이다. 밑의 상황은 스레듣 세이프한 것인가?
-   아니라고한다=> 멀티스레드 상황에서..

```
public class Settings {

    private static Settings instance;


    private static Settings getInstance() {

        if(instance == null) {
            instance = new Settings();
        }

        return instance;
    }
}
```

-   위의 상황에서 스레드 safe하지않다 이유는 a 스레드, b 스레드가 있을 때를 가정하다

1.  a 스레드가 new Setting에 들어오고 b스레드가 if문을 타고 있을 때다.
2.  만약 a스레드가 instance를 만들기전이면 b가 if문 안으로 들어오게 된다.
3.  그렇게 되면 싱글톤이 되는 것이 아니라 두개의 객체가 생성된다.

## 해결 방법

#### synchronized 키워드 사용하기

-   private static synchronized Settings getInstance() 를 사용하면 lock이 걸리면 들어오지 못한다. 그러나 매번 getInstance가 호출 될때마다 synchronized가 비용이 많이 들기 때문에 double checking lock을 사용한다.

### double check lock 사용 , volatile 사용

```
public class Settings {

    private static volatile Settings instance;

    private Settings() {}

//    instance가 있는 경우에는 
    private static  Settings getInstance() {
        if(instance == null) {
            synchronized (Settings.class) {
                if( instance == null) {
                    instance = new Settings();
                }
            }

        }
        return instance;
    }
}
```