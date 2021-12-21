
- 자바에서 문자열을 구분할 때 split도 있고, StringTockenizer도 있다. spit이 짧아 보이는데 왜 StringTokenizer을 많이 사용하나?


### split
- 지정한 구분자로 문자열을 나눠 배열에 저장한다. 

- 만약 "a,b,,c"가 있을 경우 split을 사용하면 결과과 a, b, , c 공백문자열도 포함하여 데이터가 나뉜다.

### StringTokenizer


- StringTokenizer는 공백도 포함해서 데이터가 나뉘는 것이아니라 구분자를 통해서 나뉘어진다-> 위에서 a, b, c 딱딱 나뉘어진다.




출처 : https://lnsideout.tistory.com/entry/JAVA-%EC%9E%90%EB%B0%94-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0-split-StringTokenizer-%EC%B0%A8%EC%9D%B4-%EB%B9%84%EA%B5%90
