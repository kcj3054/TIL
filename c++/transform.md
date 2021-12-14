## cpp에서 transform이라는 함수가 존재한다.

#### 사용법

```
문자열 s에 대문자 소문자가 섞여있다고 가정.

transform(s.begin(). s.end(), s.begin(). ::toupper);
```

-   transform는 transform(A, B, C, D)으로 보면 좋다 A부터 B전까지 값들을 D로 변환하고 그 값들을 C부터 저장한다

#### 예시

-   프로그래머스 매칭점수에서 사용이 되어서 공부를 했다.

```
String transToUpper(string s) {
    transform(s.begin(), s.end(), s.begin(), ::toupper);
    return s;
}
```