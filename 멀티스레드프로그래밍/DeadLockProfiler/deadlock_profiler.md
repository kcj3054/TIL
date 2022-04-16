## deadlock_profiler
- 데드락을 미리 잡기 위해서 deadlock_profiler를 살펴보자. 일반적으로 데드락은 nullptr이 0순위이다. 빈번하게 발생하는 데드락. 왜? 데드락은 타이밍 이슈라서 찰나가 너무 짧기때문에 개발단계에서는 안 잡히지만 라이브 단계에서는 잡힐 확률이 많아서 미리 예방을 해야한다. 그렇게 하기위해서 그래프 알고리즘을 이용해서 사이클을 판별하면된다.  


- 그래프가 탐색이 완료되기전에 역방향으로 오는 간선을 발견했다면 그것은 교차 간선이 아니라, 역방향 간선이다.


## DeadLockProfiler.h

````
#pragma once
#include <stack>
#include <map>
#include <vector>

class DeadLockProfiler
{
public:
	void PushLock(const char* name);
	void PopLock(const char* name);
	void CheckCycle();

private:
	void Dfs(int32 here);

private:
	unordered_map<const char* , int32 > _nameToId;
	unordered_map<int32 , const char*> _IdToName;
	stack<int>							_lockStack; //락의 상황을 판별.
	//어떤 lock이 몇번 몇번 lock을 잡았는지 다 판별하는 것.
	//ex : 0이 1번을 lock을 잡았따는 것을 정보를 담아 두는 것.
	map<int32, set<int32>>				_lockHistory;

	Mutex	_lock;

private:
	vector<int32>	_discoveredOrder; //노드가 발견된 순서를 기록
	int32			_discoveredCount = 0;// 노드가 발견된 순서
	vector<bool>	_finished; //dfs(i)가 종료되었는지 여부
	vector<int32>	_parent; //역 추적 배열 느낌 
};


````

## DeadLockProfiler.cpp

````
#include "pch.h"
#include "DeadLockProfiler.h"

void DeadLockProfiler::PushLock(const char* name)
{
	LockGuard guard(_lock);

	//아이디를 찾거나 발급한다.
	int32	lockId = 0;
	auto findIt = _nameToId.find(name);
	if (findIt == _nameToId.end())
	{
		lockId = static_cast<int32>(_nameToId.size());
		_nameToId[name] = lockId;
		_IdToName[lockId] = name;
	}
	else
	{
		lockId = findIt->second;
	}

	//잡고 있는 락이 있었다면.
	if (!_lockStack.empty())
	{
		//기존에 발견되지 않은 케이스라면 데드락 여부 다시 확인한다.
		const int32 prevId = _lockStack.top();
		if (lockId != prevId)
		{
			set<int32>& history = _lockHistory[prevId];
			if (history.find(lockId) == history.end())
			{
				history.insert(lockId);
				//새로운 길을 발견하면 사이클을 체크해본다.
				CheckCycle();
			}
		}
	}

	_lockStack.push(lockId);
}

void DeadLockProfiler::PopLock(const char* name)
{
	LockGuard guard(_lock);

	_lockStack.pop();
}

void DeadLockProfiler::CheckCycle()
{
	const int32 lockCount = static_cast<int32>(_nameToId.size());
	_discoveredOrder = vector<int32>(lockCount, -1);
	_finished = vector<bool>(lockCount, -1);
	_parent = vector<int32>(lockCount, -1);

	for (int32 lockId = 0; lockId < lockCount; lockId++)
		Dfs(lockId);

	_discoveredOrder.clear();
	_finished.clear();
	_parent.clear();
}

void DeadLockProfiler::Dfs(int32 here)
{
	if (_discoveredOrder[here] != -1) return;

	_discoveredOrder[here] = _discoveredCount++;

	//모든 인접한 정점을 순회 
	auto findIt = _lockHistory.find(here);
	if (findIt == _lockHistory.end())
	{
		//인접한 정점이 없다면 끝
		_finished[here] = true;
		return;
	}

	//here가 다른 lock을 잡은 적이 있다.
	set<int32>& nextSet = findIt->second;
	for (int32 there : nextSet)
	{
		//아직 방문한적이 없다면 방문한다.
		if (_discoveredOrder[there] == -1)
		{
			_parent[there] = here;
			Dfs(there);
			continue;
		}

		//here가 there보다 먼저 발견되었으면 there는 here의 후손이다. 순방향
		if (_discoveredOrder[here] < _discoveredOrder[there]) continue;

		//순방향 간선이 아니고 dfs가 종료되지않았다면 역방향이다.
		if (_finished[there] == false)
		{
			CRASH("DEADLOCK_DETECTED");
		}
	}
}

````

### PushLock

- 여기서는 말 그대로 해당 이름을 가진 것을 lock을 걸어 주는 역할을 한다. 아이디를 찾아서 없으면 발급해주고, lockStack이 채워져있는 경우 (잡고 있는 락이 있다) 체크를 한다 여기서 왜 lockStack의 top부분만 현재 lockId가 다를때만 체크하는가?  만약 같다고 생각을 해보자 그러면 A에서 A로 락을 거는데 이런 경우는 데드락이 발생하지 않기 때문에 무시하는 것이다.  

###  DeadLockProfiler::Dfs

- 여기서 중요한 부분은 

````
//here가 there보다 먼저 발견되었으면 there는 here의 후손이다. 순방향
		if (_discoveredOrder[here] < _discoveredOrder[there]) continue;

		//순방향 간선이 아니고 dfs가 종료되지않았다면 역방향이다.
		if (_finished[there] == false)
		{
			CRASH("DEADLOCK_DETECTED");
		}
````

- 여기서 discoveredOrder의 here과 there을 비교해서 순방향인지 아니면 역방향인 상태에서 아직 dfs가 종료되지않았는지 체크를 하면서 데드락을 감지하는 부분이 핵심이다.