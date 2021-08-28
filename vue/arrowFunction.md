#### 애로우 함수


* 함수를 사용할때 function을 사용하지 않고 => 를 사용한다 


* 예시 1

//ES 5
var sum = function(a, b) {
    return a + b;
};


//ES6

var sum  = (a, b) => {
    return a + b;
};

* 예시 2

//ES 5


var arr = ["a", "b", "c", "d"];

arr.forEach(function(value) {
    console.log(value);
});


//ES 6

var arr = ["a", "b", "c", "d"];

arr.forEach( value => console.log(value));

