## Merge Join

- merge조인에는 many to many 와 one to many가 있다 여기서 many to many는 다대다 방식으로 outer 바깥쪽인 중복되는 데이터가 있다는 것이다. 여기서 바까쪽에서 one. 유일한 데이터들이 매우 중요하다... 



- [##_Image|kage@rsSiU/btryEtg5qHq/dWqdV7ZDKeDYQha5k3ENKk/img.png|alignCenter|width="100%"|_##]

````
SELECT *
FROM players AS p
	INNER JOIN salaries AS s
	ON p.playerID = s.playerID
````

- 여기서 실행계획을 살펴보면 merge join이고,  many to many이다...     그런데 players에  p.playerID 는 인덱스가 걸려있다. (nonclustered)... 그런데 왜 indexScand을 할까? 이유는 nonClustered이니 해당 값을 가지고 Heap Table로 다시 가거나, Clustered로 이동을 또 해야하기에 그럴빠엔 scan을 하는 것이 더 빠르다고 생각했기때문이다. 

## 결론 

- merge join에서 outer가 unique하다면.. 좋다(one to many) one은 outer가 유일하다는 뜻..



- 루키스님의 서버db강의를 학습 후 작성하였습니다. 