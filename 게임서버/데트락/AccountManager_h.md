## AccountManager.h 부분 

- GetAccount부분에 lock_guard가 걸려있다

## 소스
````
#pragma once

#include <mutex>
using namespace std;

//계정 
class Account
{
	//Todo
};


class AccountManager
{

public:
	static AccountManager* Instance()
	{
		static AccountManager instance;
		return &instance;
	}

	Account* GetAccount(__int32 id)
	{
		lock_guard<mutex> guard(_mutex);

		return nullptr;
	}

	void ProcessLogin();


private:
	std::mutex _mutex;
};


````