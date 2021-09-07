#### 자바의 비동기처리 


여기서 비동기란 ? 

비동기란 요청이 왔을때 결과를 처리 해줄때까지 기다리지 않는다 
왜냐? 기다리는 시간조차 아깝기때문이다. 그래서 요청이 온것은 처리하도록 나두면서 결과가 올때까지 기다리지말고
그사이 다른 요청들을 처리하는 것이다 


js에서는 비동기처리를 쉽게 하기 위해서 asyn wait가 있다 

#### 문법 

````
async function 함수명() {
  await 비동기_처리_메서드_명();
}
````
그러고 나서 함수의 내부 로직 중 HTTP 통신을 하는 비동기 처리 코드 앞에 await를 붙입니다. 여기서 주의하셔야 할 점은 비동기 처리 메서드가 꼭 프로미스 객체를 반환해야 await가 의도한 대로 동작합니다.



#### ㅇㅖㅅㅣ
````
async function logTodoTitle() {
  var user = await fetchUser();
  if (user.id === 1) {
    var todo = await fetchTodo();
    console.log(todo.title); // delectus aut autem
  }
}
````

1. fetchUser()를 이용하여 사용자 정보 호출
2. 받아온 사용자 아이디가 1이면 할 일 정보 호출
3. 받아온 할 일 정보의 제목을 콘솔에 출력


#### method call vs callback 

var arr = [1, 2, 3, 4, 5];
var obj = {
  vals: [1, 2, 3];
  logvalues: function(v, i) {
    if(this.vals) {
      console.log(this.vals, i, v)
    } else{
      console.log(this, i, v);
    }
  }
}
obj.logvalues(1, 2); => [1, 2, 3] , 1, 2
arr.forEach(obj.logvalues) =>  callback 
