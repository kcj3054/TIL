## lambda

- 람다식은 자바에서 함수형 프로그래밍을 구현하는 방식이다.

- 함수형 프로그래밍이란 순수함수를 구현하고, 외부 자료에 부수적인 영향을 주지 않고 매개 변수만을 사용하도록 만든 함수이다.

- 밑의 예에서 MyNumber라는 인터페이스가 존재한다, 변수에 람다식을 넣은 것이다. 이후 변수가 인터페이스의 getMaxNumber를 사용한다.

- 람다식이 간편해보이는데, 자바는 객체지향언어이다. 어떤 작업이든 객체를 생성한다, 그래서 람다식도 내부적으로 객체를 생성하여서 값을 넘겨준다.

````
public class TestMyNumber {
    public static void main(String[] args) {

        MyNumber maxNum = (x, y) -> (x >= y) ? x : y;
        int max = maxNum.getMaxNumber(10, 20);


        //실질적으로 6line처럼 쓰지만 실제로는 11라인처럼 내부적인 익명클래스가 호출되는 것이다
        MyNumber aaa= new MyNumber() {
            @Override
            public int getMaxNumber(int num1, int num2) {
                return 0;
            }
        };
    }
}
````

## stream

- 특징
	- 한 번생성하고 사용된 스트림은 재사용할 수 없다.
    - 스트림은 기존 자료형을 변경하지 않는다, 스트림을 사용하면 별도의 메모리 공간을 사용하므로 기존 자료를 변경하지 않음
    

````
public class ArrayListTest {
    public static void main(String[] args) {


        List<String> sList = new ArrayList<>();
        sList.add("Tomas");
        sList.add("James");
        sList.add("Edward");

        Stream<String> stream = sList.stream();   // sList에 stream을 만들었다.
        stream.forEach(s -> System.out.println(s));

        sList.stream().sorted().forEach(s -> System.out.println(s)); // stream을 만들고 -> 중간 연산으로 sorted하고, forEach로 최종연산을 수행
    }
}
````


## innerclass

-  클래스안에 클래스가 있다는 것이다.

- innerclass는 외부 클래스에 대한 참조값들을 가지고 있어서 외부 클래스의 값들을 사용가능하다.

- inner class, 인스턴스변수와 나란히 있어서 인스턴스 인너클래스라고도 한다

- 밑의 main함수를 보자, InStaticClass는 stataic 클래스이다 그래서 외부 클래스인 OutClass의 생성과 상관없이 사용가능하다

- sTest innerclass의 staic 메소드이다, static!!이다, 그래서 어떤 것의 생성과 상관없이 클래스를 통해 접근해서 사용가능하다.

````
package com.example.item02.innerclass;

class OutClass {

    private int num = 10;
    private static int sNum = 20;
    private InClass inClass;

    public OutClass() {

    }

    //인스턴스 inclass는 외부 클래스에 대한 참조값들을 가지고 있어서 외부 클래스의 값들을 사용가능하다
    //inner class, 인스턴스변수와 나란히 있어서 인스턴스 인너클래스라고도 한다
    private class InClass {
        int num = 20;

        //static int i = 20; x 불가 메모리 로딩 시점 기억

        void inTest() {
            System.out.println(num);
            System.out.println(sNum);  // 정적변수를 선언을 못할 뿐이지 외부에 있는 것을 가져다가 쓰는 것은 가능하다
        }
    }

    public void usingInTest() {
        
        inClass.inTest();
    }


    static class InStaticClass {
        int iNum = 100;
        static int sInNum = 200;  //static 변수

//        이것은 인스턴스 메소드라서 InStaticClass가 생성된 이후에 호출되어야한다 d
        void inTest() {
           // num += 10;// 불가 InStaticClasss는 객체 생성을 안해도 사용할 수 있기에
            sInNum += 20;
            System.out.println(sNum);
            System.out.println(iNum);
            System.out.println(sInNum);
        }

//        static 메소드도 외부에서 바로 쓸 수 있기에 staic변수들만 접근 가능
        static void sTest() {
            System.out.println(sNum);
            System.out.println(sInNum);
        }
    }
}

public class OutClassTest {
    public static void main(String[] args) {

        OutClass outClass = new OutClass();
        outClass.usingInTest();

        OutClass.InStaticClass sInClass = new OutClass.InStaticClass();  // OutClass의 생성과 상관없이 사용 가능

        OutClass.InStaticClass.sTest(); // 그 무엇의 생성고 ㅏ상관없이 호출될 수 있다
    }
}


````