### UserManager.h 부분


````
#pragma once
#include <mutex>


using namespace std;

class User
{
	//Todo 
};
class UserManager
{
public:
	static UserManager* Instance()
	{
		static UserManager instance;

		return &instance;
	}


	User* GetUser(__int32 id)
	{
		lock_guard<mutex> guard(_mutex);

		return nullptr;	
	}

	void ProcessSave();

private:
	mutex _mutex;
};


````