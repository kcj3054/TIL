## indexSeek가 빠른가, IndexScan이 빠른가 ?

- 결론을 먼저 말하면 때에 따라 다르다 왜냐? clustered가 존재하는지, 없는지 NonClustered Index만 있는지 모두 고려해야하기때문이다..

````
USE Northwind;

-- 인덱스 접근 방식 


CREATE TABLE TestAceess
(
	id INT NOT NULL,
	name NCHAR(50) NOT NULL,
	dummy NCHAR(1000) NULL
);

GO

CREATE CLUSTERED INDEX TestAccess_CI
ON TestAceess(id);

GO

CREATE NONCLUSTERED INDEX TestAccess_NCI
ON TestAceess(name)

DECLARE @i INT;
SET @i = 1;

WHILE (@i <= 500)
BEGIN
	INSERT INTO TestAceess
	VALUES (@i, 'Name' + CONVERT(VARCHAR, @i), 'Hello World' + CONVERT(VARCHAR, @i));
	SET  @i = @i + 1;
END



-- 인덱스 정보

EXEC sp_helpindex 'TestAceess'

-- 인덱스 번호
SELECT index_id, name
FROM sys.indexes
WHERE object_id = object_id('TestAceess')

--조회 
DBCC IND('Northwind', 'TestAceess', 1)
DBCC IND('Northwind', 'TestAceess', 2)


-- CLUSTERED (1) : id

-- 9121  167개

-- NonCLUSTERED (2) : name
--      857
-- 856  858 860 861~ 973(13)개


-- 논리적 읽기 -> 실제 데이터를 찾기 위해 읽은 페이지 수 
SET STATISTICS TIME ON;
SET STATISTICS IO ON;


-- INDEX SCAN = LEAF PAGE 순차적으로 검색 
select *
from TestAceess;


--논리적 읽기2번 -> 클러스터드 인덱스 -> ROOT한번 보고 그후 원하는 LEAF로 이동 .. 그래서 총 2번
select *
from TestAceess
WHERE ID = 104


-- index seek + KEY LOOK UP 총4
-- NAME의 ROOT로 이동 후 -> 클러스터드 인덱스가 있다면 LEAF에 클러스터드인덱스의 KEY값만 가지고있다. -> 그후 ID값을 가진 후 CLUSTERED로 이동 후 해당 ID로 찾는다 
-- 총4
select *
from TestAceess
WHERE name = 'name5'


-- INDEX SCAN + KEY LOOCK UP -> 경과 시간이 굉장히 짧다 -=> 이유 ! INDEX SCANF이 LEAF부터 쫙 다 스캔하는 것이다 그런데 NAME은 NONCLUSTERED로 잡고 있다 .
-- 그래서 ORDER BY name은 LEAF를 5개만 순차적으로 추출하면된다. 

SELECT TOP 5 *
FROM TestAceess
ORDER BY name;


````


- 위의 소스에서 id가 clustered이고, name은 NonClustered이다...  

````
-- CLUSTERED (1) : id

-- 9121  167개

-- NonCLUSTERED (2) : name
--      857
-- 856  858 860 861~ 973(13)개
````

- id를 조건으로 주면서 검색을 하면 논리적 읽기가 2번으로 나온다 왜냐? ID는 clustered Index로 잡혀있어서 이동 순서가 root페이지로 이동 -> key에 해당하는 page로 바로 이동해서 LEAF PAGE 자체가 DATA이기에 총 2번 이동하면 끝이다. 
````
select *
from TestAceess
WHERE ID = 104
````


- 밑에서 NAME으로 찾을 경우 논리적 읽기가 총4번 나오게된다.  이유를 살펴보면 NAME은 NonClusteredIndex이다 그래서 해당 인덱스 root page로 이동 -> key를 들고 있는 leaf page로 이동 -> clustered page의 root로 이동 -> 실질적인 데이터를 가진 leaf page로 이동 그래서 총4번이 걸리게된다. 

````
select *
from TestAceess
WHERE name = 'name5
````

[##_Image|kage@bbDPKz/btryu9xJXMI/FKw6dyV3mCbSOPG7RyxrY0/img.png|alignCenter|width="100%"|_##]


### INDEX SCAN + KEY LOOCK UP -> 경과 시간이 굉장히 짧다 왜??

````
SELECT TOP 5 *
FROM TestAceess
ORDER BY name;
````

- INDEX SCANF이 LEAF부터 쫙 다 스캔하는 것이다 그런데 NAME은 NONCLUSTERED로 잡고 있다 . 그래서 ORDER BY name은 LEAF를 5개만 순차적으로 추출하면된다.


### 결론

- clustered의 경우 Index Seek가 느릴 수가 없다. 바로 해당 인덱스의 위치로 이동하니
- NonClustered의 경우 데이터가 Leaf Page에 없다 따라서 한번 타고가야한다 
	- RID가 존재하는 경우(CLUSTERED가 없는 경우) -> Heap Table로 이동한다 (Bookmark Lookup)
    -  Key -> Clustered 클러스터드가 있는경우는 리프 페이지가 key를 의미한다. 