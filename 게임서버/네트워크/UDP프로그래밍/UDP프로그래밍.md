## UDP 프로그래밍 

- udp프로그래밍은 빠르고, 안전하지않고 단점이 많은 것같지만 tcp에 비해 경계의 개념이 있어서  택배 박스처럼 패킷을 넣어서 전송하는 느낌이있다.. 


## dummyclient 소스

````
#include "pch.h"
#include <iostream>

#include <WinSock2.h>
#include <MSWSock.h>
#include <WS2tcpip.h>

#pragma comment(lib, "ws2_32.lib")
int main()
{
	WSADATA wsaData;
	if (::WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		return 0;

	// ad : Address Family (AF_INET = IPv4, AF_INET6 = IPv6)
	// type : TCP(SOCK_STREAM) VS UDP(SOCK_DGRAM)
	// protocol : 0
	// return : descriptor
	SOCKET clientSocket = ::socket(AF_INET, SOCK_DGRAM, 0);
	if (clientSocket == INVALID_SOCKET)
	{
		int32 errorCode = ::WSAGetLastError();

		cout << "Socket ErrorCode : " << errorCode << endl;
		return 0;
	}

	SOCKADDR_IN serverAddr;
	::memset(&serverAddr, 0, sizeof(serverAddr));

	serverAddr.sin_family = AF_INET;
	::inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr);

	serverAddr.sin_port = ::htons(7777);   // port 포트 번호 
	

	if (::connect(clientSocket, (SOCKADDR*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR)
	{
		int32 errorCode = ::WSAGetLastError();

		cout << "Connect ErrorCode : " << errorCode << endl;
	}

	cout << "Connected To Server" << endl;

	while (true)
	{
		char sendBuffer[100] = "Hello world";
		
		for (int i = 0; i < 10; i++)
		{
			int32 resultCode = ::sendto(clientSocket, sendBuffer, sizeof(sendBuffer), 0, (sockaddr*)&serverAddr, sizeof(serverAddr));
			cout << "Send Data Len : " << sizeof(sendBuffer) << endl;
		}
		
		

		//-------------------------server에서 보낸 것을 recv

		//char recvBuffer[1000];

		//int recvLen = ::recv(clientSocket, recvBuffer, sizeof(recvBuffer), 0);

		////SOCKET_ERROR가 -1인데 0보다 작으면 에러라고 보자!
		//if (recvLen <= 0)
		//{
		//	int32 errCode = ::WSAGetLastError();
		//	cout << "Rcv ErrorCode : " << errCode << endl;
		//	return 0;
		//}
		//cout << "Rcv Data : " << recvBuffer << endl;

		//this_thread::sleep_for(1s);

	}
	::closesocket(clientSocket);

	::WSACleanup();
}
````

## server소스
````
#include "pch.h"
#include <iostream>
#include <atomic>
#include <mutex>

#include <future>
//#include "ThreadManager.h"

#include <winsock2.h>
#include <mswsock.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
void HandleError(const char* Error)
{
	cout << Error << " ErrorCode" << endl;
	
}
int main()
{
	// 윈속 초기화 (ws2_32 라이브러리 초기화)
	// 관련 정보가 wsaData에 채워짐
	WSAData wsaData;
	if (::WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		return 0;

	SOCKET serverSocket = ::socket(AF_INET, SOCK_DGRAM, 0);
	if (serverSocket == INVALID_SOCKET)
	{
		HandleError("Socket");
		return 0;
	}

	SOCKADDR_IN serverAddr;
	::memset(&serverAddr, 0, sizeof(serverAddr));

	serverAddr.sin_family = AF_INET;
	serverAddr.sin_addr.s_addr = ::htonl(INADDR_ANY);
	serverAddr.sin_port = ::htons(7777);   // port 포트 번호
	
	if (::bind(serverSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR)
	{
		HANDLE("bind");
		return 0;
	}

	//udp는 bind 후 listen, accept 과정이 필요없다.

	while (true)
	{
		this_thread::sleep_for(1ms);

		sockaddr_in clientAddr;
		::memset(&clientAddr, 0, sizeof(clientAddr));
		int32 addrLen = sizeof(clientAddr);

		char recvBuffer[1000];

		int32 recvLen = ::recvfrom(serverSocket, recvBuffer, sizeof(recvBuffer), 0, (sockaddr*)&clientAddr, &addrLen);
	
		if (recvLen <= 0)
		{
			HANDLE("RecvFrom");
			return 0;
		}

		cout << "Recv DATA! " << recvBuffer << endl;
		cout << "Recv Len " << recvLen << endl;

	
	}

	// 윈속 종료
	::WSACleanup();
}
````

- 실행한 결과 데이터길이가 100 100 씩 쪼개져서 나오게된다.