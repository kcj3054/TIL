## AccountManager.cpp 부분

- ProcessLogin을 할때 accountLock을 걸어놓고, userLock부분을 실행하는데 이미 UserManager부분에서도 GetUser부분에 이미 lock이 걸려있다. 서로 lock을 걸어 놓고 풀지는 않으면 데드락 문제가 발생하게된다.

## 소스

````
#include "AccountManager.h"
#include "pch.h"
#include "UserManager.h"

void AccountManager::ProcessLogin()
{
	//accountLock
	lock_guard<mutex> guard(_mutex);


	//userLock
	User * user = UserManager::Instance()->GetUser(100);


}
````