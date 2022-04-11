##  overlapped모델(callback 방식)

- 콜백방식이랑 이벤트방식은 비동기방식이다.  완료시점을 뒤로 미루는 느낌.  콜백이랑 이벤트 방식의 차이는 완료되었다는 것을 callback함수로 받거나, 이벤트를 통해 받거나의 차이이다.


- 구현에도 큰 차이가 없다 이벤트 방식은 세션이랑 이벤트를 1대 1대응을 시켰고,WSARecv마지막에 CALLBACK을 사용하지 않았던 것이다.  

- 콜백 방식은 이벤트랑 세션을 1대1 대응할 필요가 없다, 또한 Alertable Wait를 사용해서 받을 callback이 있는지 생길때까지 대기를 타다가 SleepEx하는 순간에 내부적으로 예약 되어있는 callback을 다 호출하는 방식이다. 여기서 특징은 클라갯수만큼 이벤트가 필요하지 않다는점이다.

- alertable wait apc를 찾아보면 쓰레드마다 각기 APC큐가 존재해서 callback 함수를 쌓는 개념이다.

- 또하나의 설명~ -> 비동기방식에서 완료되면 os에서 완료 루틴 호출을 받아야하는데 시점이 현재 lock을 걸고 중요한 작업을 하는 시점이면 문제가 생긴다. 그래서 비동기 입출력 함수 호출한 쓰레드를 Alertable Wait 상태로 만들면 완료루틴을 호출하면된다.

- 완료루틴 호출이 모두 끝나면 쓰레드는 Alertable Wait상태에서 나온다.

````
overlapped 모델 (completion Routine 콜백 기반)
	- 비동기 입출력 지원하는 소케 생성
	- 비동기 입출력 함수 호출 (완료 루틴(callback 함수)의 시작 주소를 넘김)
	- ..
	- lock을 걸어 놓고 처리를 하는 중에 완료 루틴을 호출하면 안된다 -> 비동기 입출력 함수 호출한 쓰레드를 Alertable Wait 상태로 만든다.
	- ex  : SleepEx ..... 여러가지 옵션 중하나를 선택해서 해당 쓰레드를  Alertable Wait로 만들면 완료루틴을 호출.
	- 비동기 io가 완료되면, 운영체제는 완료 루틴 호출
	- 완료루틴 호출이 모두 끝나면 쓰레드는 Alertable Wait상태(알림이 가능한 기다림상태)에서 나온다.
````

## callback 함수를 살펴보자.

````
void CALLBACK RecvCallback(DWORD error, DWORD recvLen, LPWSAOVERLAPPED overlapped, DWORD flag)
{
	cout << "Data Recv Len Callback = " << recvLen << endl;
}
````

- 위 콜백함수 인자를 살펴보면 우리에게 os가 함수에 대한 정보를 알려줄 만한 인자는 overlapped밖에 존재하지 않는다 이것을 잘 활용해보면 세션으로 타입변환을 시켜줄 수 있다. 세션 구조체 첫번째 인자로 overlapped로 만들어주면 세션 <=  overlapped로 타입변환이 가능하다


````

struct Session
{
	WSAOVERLAPPED overlapped = {};
	SOCKET socket = INVALID_SOCKET;
	char recvBuffer[BUFSIZE] = {};
	int32 recvBytes = 0;  //받았을 경우 저장	
};
````

## 서버 소스
````
#include "pch.h"
#include <iostream>
#include "CorePch.h"
#include <atomic>
#include <future>
#include "ThreadManager.h"

#include <winsock2.h>
#include <mswsock.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")

void HandleError(const char* cause)
{
	int32 errCode = ::WSAGetLastError();
	cout << cause << " ErrorCode : " << errCode << endl;
}

const int32 BUFSIZE = 1000;

struct Session
{
	WSAOVERLAPPED overlapped = {};
	SOCKET socket = INVALID_SOCKET;
	char recvBuffer[BUFSIZE] = {};
	int32 recvBytes = 0;  //받았을 경우 저장
	//int32 sendBytes = 0;  //보낸데이터 크기
	
};
//os가 우리에게 알려줄 정보들은 알려 줄 수 있는 것은  overlapped밖없다.
//overlapped handleheVENT밖에없다 우리에ㅔ게 도움될것은 
//LPWSAOVERLAPPED -> (OVERLAPPED의 포인터란느 의미)
void CALLBACK RecvCallback(DWORD error, DWORD recvLen, LPWSAOVERLAPPED overlapped, DWORD flag)
{
	cout << "Data Recv Len Callback = " << recvLen << endl;

	//Session에 처음에 WSAOVERLAPPED overlapped = {};를 넣어주면
	// overlappep를 받아도 Session으로 복원 할 수 있다.
	// Session에서 overlappep위치도 굉장히 중요하게된다.
}
//// void CompletionRoutine( 오류 발생시 0이 아닌값, 전송 바이트 수, 비동기 입출력 함수 호출시 넘겨준 WSAOVERLAPPED 구조체
		//주소값, , 0)
int main()
{
	WSAData wsaData;
	if (::WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		return 0;

	SOCKET listenSocket = ::socket(AF_INET, SOCK_STREAM, 0);
	if (listenSocket == INVALID_SOCKET)
		return 0;

	u_long on = 1;
	if (::ioctlsocket(listenSocket, FIONBIO, &on) == INVALID_SOCKET)
		return 0;

	SOCKADDR_IN serverAddr;
	::memset(&serverAddr, 0, sizeof(serverAddr));
	serverAddr.sin_family = AF_INET;
	serverAddr.sin_addr.s_addr = ::htonl(INADDR_ANY);
	serverAddr.sin_port = ::htons(7777);

	if (::bind(listenSocket, (SOCKADDR*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR)
		return 0;

	if (::listen(listenSocket, SOMAXCONN) == SOCKET_ERROR)
		return 0;

	cout << "Accept" << endl;
	/*
	overlapped 모델 (completion Routine 콜백 기반)
	- 비동기 입출력 지원하는 소케 생성
	- 비동기 입출력 함수 호출 (완료 루틴(callback 함수)의 시작 주소를 넘김)
	- ..
	- lock을 걸어 놓고 처리를 하는 중에 완료 루틴을 호출하면 안된다 -> 비동기 입출력 함수 호출한 쓰레드를 Alertable Wait 상태로 만든다.
	- ex  : SleepEx ..... 여러가지 옵션 중하나를 선택해서 해당 쓰레드를  Alertable Wait로 만들면 완료루틴을 호출.
	- 비동기 io가 완료되면, 운영체제는 완료 루틴 호출
	- 완료루틴 호출이 모두 끝나면 쓰레드는 Alertable Wait상태에서 나온다.
	*/
	while (true)
	{
		SOCKADDR_IN clientAddr;
		int32 addrLen = sizeof(clientAddr);

		SOCKET clientSocket;
		while (true)
		{
			clientSocket = ::accept(listenSocket, (sockaddr*)&clientAddr, &addrLen);
			if (clientSocket != INVALID_SOCKET) break;


			if (::WSAGetLastError() == WSAEWOULDBLOCK) continue;

			return 0;
		}
		Session session = Session{ clientSocket };
		WSAEVENT wsaEvent = ::WSACreateEvent();
		

		cout << "Client Connected" << endl;
		
		while (true)
		{
			WSABUF wsaBuf;
			wsaBuf.buf = session.recvBuffer;
			wsaBuf.len = BUFSIZ;

			DWORD recvLen = 0;
			DWORD flags = 0;
			//마지막인자가 callback을 의미한다. 
			if (::WSARecv(clientSocket, &wsaBuf, 1, &recvLen, &flags, &session.overlapped, RecvCallback) == SOCKET_ERROR)
			{
				if (::WSAGetLastError() == WSA_IO_PENDING)
				{
					
					//pending
					//Alertable Wait -> 받을 callback이 있는지 생길때까지 대기를 탄다
					::SleepEx(INFINITE, TRUE); 
					//SleepEx하는 순간 내부적 예약되는 callback을 다 호출한다.
					// 클라갯수만큼 이벤트가 필요없다는 장점이있다.

				}
				else break;
			}
			else
			{
				cout << "Data Recv Len = " << recvLen << endl;
			}
			

		}
		::closesocket(session.socket);
	}

	// 윈속 종료
	::WSACleanup();
}

````

- 참고 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kbm0996&logNo=221124634245
- 루키스님의 서버강의를 학습 후 작성하였습니다. 