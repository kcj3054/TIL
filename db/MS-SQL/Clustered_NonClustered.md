## Clustered . NonClustered

- Clusterd (영한 사전)이고  Non - Clusterd(색인)으로 본다 왜? Clustered index를 보면 바로 데이터를 찾아 갈 수 있는데 Non clustered는 데이터를 색인처럼 중복해서 가지고 있을 수 있기 때문이다. 

- Clusterd는 leaf Page가 Dage Page이다.  데이터는 ClusterdIndex 키 순서로 정렬된다..

-  Non - Clusterd는 Clusterd Index에 따라서 다르게 결정된다..  
	- 1) Clusterd Index가 존재하는 경우 HEAP Table이 없다 leaf table에 실제 테이블에 실제 데이터가 존재한다.  
    
    - 2)  Clusterd Index가 존재하지 않는 경우 데이터는 HEAP Table이라는 곳에 저장된다 , 페이지 정보를 살펴보면  Heap RID라는 것이이는데 이것을 살펴보면서  PAGE DATE를 찾아가면서 HEAP Table을 찾아 갈 수 있다..
    
    
## Clustered . NonClustered 실습

````
-인덱스 번호 찾기 
SELECT index_id, name
FROM sys.indexes
WHERE object_id = object_id('TestOrderDetails')

-- 조회 PageType이 2이다 Nonclustered
DBCC IND('Northwind', 'TestOrderDetails', 2)

-- Index Level이 높을 수록 root이다. 

--         944
--  856  888 889 890 891....
--Heap RID  ([페이지주소][파일ID][슬록])
-- Heap Table [{page}{page}{}..]
-- 
DBCC PAGE('Northwind', 1/*페이지 ID*/,888, 3)

-- HEAP RID가 존재... HEAP RID를 이용해서 데이터가 있는 Heap Table에서 데이터를 꺼내서 사용한다.. 



````
    


## clustered 추가 

````
--clusterd 추가 

CREATE CLUSTERED INDEX Index_OrderDetails_Clustered
ON TestOrderDetails(OrderID)


-- 조회 PageType이 1이다 clustered
DBCC IND('Northwind', 'TestOrderDetails', 1)
--         968
--   920 928 929 931....  (실제 데이터를 물고 있는 페이지..)

DBCC PAGE('Northwind', 1/*페이지 ID*/,931, 3)
````