## UserManager.cpp

- 설명은 AccountManager부분에서 설명 

## 소스 

````
#include "UserManager.h"
#include "AccountManager.h"

void UserManager::ProcessSave()
{
	//userLock
	lock_guard<mutex> guard(_mutex);


	//accountLock
	Account * account = AccountManager::Instance()->GetAccount(100);



}
````