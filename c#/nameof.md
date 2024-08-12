## nameof

- c++에서 enum 값들을 출력할 때나 1, 2, 3 숫자로 표현되어서 바로 인식에 어려움을 겪는다. 이럴 때 c#에서 유용했던 것이 nameof를 사용하는 것이었다.

- 너무 편리했던 점은 enum으로 정의 되어있던 것들을 nameof을 이용하면 해당 값으로 출력이 되었다 밑에 예시를 보면.. 

- enum 타입을 nameof로 연동 시 컴파일 타임에 연동되는데, ToString을 하게된다면 런타임에 연동된다고한다. 

````c++



````



### 예2 (Exception 발생 시 )

- nameof의 다른 장점 중 하나는 exception 발생 시 메시지에 parameter로 nameof 사용한 것을 추가할 수 있다. 

- 예외 메시지에 변수 이름을 포함 시키면 변수명이 변경되더라도 update되어, 코드 유지보수에 좋다. 

````c#
public class Program
{
    public static void ExceptionMessage(object thisCanBeNUll)
    {
        if(thisCanBeNUll == null)
        {
            throw new ArgumentNullException(nameof(thisCanBeNUll), "can't be null');
        }
    }

    public static void Main(string[] args)
    {
        try
        {
            ExceptionMessage(null);
        }
        catch(ArgumentNullException ex)
        {
            Console.WriteLine(${ex.Message})
        }
    }
}

````

- 위 결과로는 
````
can't be null (parameter 'thisCanBeNUll')
````