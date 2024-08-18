#### builder 패턴이란 ? 

빌더 패턴이란 
자바에서 

- 빌더 패턴은 복잡한 개체 생성을 할 때 간단하도록 돕는 장점이있고, 쉽게 말하면 매서드 체이닝이라고 보실 수도있습니다.

````c#

public class Car
{
    public string Engine { get; private set; }
    public string Wheels { get; private set; }
    public string Color { get; private set; }

    public Car SetEngine(string engine)
    {
        Engine = engine;
        return this;
    }

    public Car SetWheels(string wheels)
    {
        Wheels = wheels;
        return this;
    }

    public Car SetColor(string color)
    {
        Color = color;
        return this;
    }
}

// Usage
class Program
{
    static void Main()
    {
        Car car = new Car()
                    .SetEngine("V8")
                    .SetWheels("Alloy")
                    .SetColor("Red");

        Console.WriteLine($"Car Details: Engine={car.Engine}, Wheels={car.Wheels}, Color={car.Color}");
    }
}

````