## c# IENUMBERABLE 

- 지연실행 (lazy eavluation)을 사용하여. 실제로 데이터를 열거할 때마다 해당 데이터 소스를 최신을 가져옴 , 지연 실행의 특성으로 인해 동일한 IENUMBERABLE을 여러 번 열거할 때마다 데이터 소스에 다시 접근하게된다. 

````c#

IEnumerable<string> names = GetNames(); // GetNames()는 DB 또는 API 호출을 포함한 지연 실행을 반환
foreach (var name in names)
    Console.WriteLine("Found " + name);

var allNames = new StringBuilder();
foreach (var name in names)
    allNames.Append(name + " ");

````

- 첫 번째 열거 작업과 두 번째 열거 작업 사이에 데이터 소스에서 데이터가 변경되었다면, 두 번의 foreach에서 가져온 데이터가 서로 다를 수 있습니다. 이는 다음과 같은 상황에서 문제가 될 수 있습니다:

- 동일한 작업 내에서 동일한 데이터를 기반으로 처리해야 하는 경우, 두 번의 열거가 다른 데이터를 반환하면 데이터 일관성이 깨집니다.

- 만약 위 작업 모두 동일 데이터 기반으로 사용해야한다면, IENUMBERABLE 보다 TOLIST를 사용하는 것이 좋다. 


## async / await 사용 시 hang 문제가 발생하는 경우.

-  ThreadPool 고갈은 .NET 애플리케이션에서 스레드 풀이 필요한 작업을 처리하지 못할 때 발생합니다. 보통 스레드 풀의 스레드는 작업을 처리한 후 대기 상태로 돌아가지만, 작업이 너무 많아 모든 스레드가 바쁘면 새로운 작업이 대기해야 합니다.

- 큐잉의 문제점은, 추가적인 작업들이 큐에 쌓이면서 대기 시간이 길어지고, 이로 인해 응답 속도가 저하될 수 있다는 점입니다. 특히, 스레드 풀이 고갈된 상태에서는 큐에 있는 작업들이 제때 처리되지 않아 성능 문제가 발생할 수 있습니다.
- 