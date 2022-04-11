## Overlapped모델(이벤트기반)

- Overlapped IO는 비동기 + 논블로킹이다. 

- 단계를 살펴보자
	- 1. Overlapped  함수를 건다(WSARecv, WSASend)
    - 2. Overlapped 함수가 성공했는지 확인 후 성공했으면 처리를 하고 실패를 했으면 pending인지 아니면 진짜 실패인지 체크 
    - 3. 성공했을 때 이벤트 방식으로 하거나 call back방식으로 처리 할 수 있다 이번에는 이벤트 방식..
    
    
- Overlapped모델 상세 옵션을 살펴보겠습니다 

````
cf : Scatter - Gather라는 것이 있는데 이것은 흩어져있는 패킷들을 모아서 전송할 수 있어서 성능적으로 우수하다.

WSASend, WSARecv의 인자들을 보겠습니다.
	1) 비동기 입출력 소켓
	2) wsaBUF 배열의 시작 주소 + 개수
	3) 보내거나 받은 바이트 수 
	4) 상세 옵션인데 0
	5) WSAOVERLAPPED : 구조체 주소값
	6) 입출력이 완료되면 OS가 호출할 콜백함수 
ex : WSARecv(clientSocket, &wsaBuf, 1, &recvLen, &flags, &session.overlapped,nullptr) == SOCKET_ERROR)
````


- 이벤트기반 overlapped 모델은

	- 비동기 입출력 지원하는 소켓 생성 + 통지 받기 위한 이벤트 객체 생성
    - 비동기 입출력 함수 호출 
    - 비동기 작업이 완료되지 않으면 WSA_IO_PENDING 
    - 운영체제는 이벤트 개체를 signaled 상태로 만들어서 완료 상태 알려줌
    - WSAWaitForMutilpleEvents 함수 호출해서 이벤트 객체의 signal 판별
    - WSAGetOverlappedResult 호출해서 비동기 입출력 결과 확인 및 데이터 처리 

- WSAGetOverlappedResult인자
````
/*WSAGetOverlappedResult
	* 1)비동기 소켓
	* 2) 넘겨준 overlapped 구조체
	* 3) 전송된 바이트 수
	* 4) 비동기 입출력 작업이 끝날때까지 대기할지?
	* 5) 비동기 입출력 작업 관련 부가정보 거의 사용안함 
ex : :: WSAGetOverlappedResult(session.socket, &session.overlapped, &recvLen, FALSE, &flags);
````


### server쪽 소스
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
	SOCKET socket = INVALID_SOCKET;
	char recvBuffer[BUFSIZE] = {};
	int32 recvBytes = 0;  //받았을 경우 저장
	//int32 sendBytes = 0;  //보낸데이터 크기
	WSAOVERLAPPED overlapped = {};
};

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
		session.overlapped.hEvent = wsaEvent;

		cout << "Client Connected" << endl;

		while (true)
		{
			WSABUF wsaBuf;
			wsaBuf.buf = session.recvBuffer;
			wsaBuf.len = BUFSIZ;

			DWORD recvLen = 0;
			DWORD flags = 0;

			if (::WSARecv(clientSocket, &wsaBuf, 1, &recvLen, &flags, &session.overlapped,nullptr) == SOCKET_ERROR)
			{
				if (::WSAGetLastError() == WSA_IO_PENDING)
				{
					//pending
					//wsaWaitFourMulipleEvent  하나라도 완료될때까지 기다리겠다
					::WSAWaitForMultipleEvents(1, &wsaEvent, true, WSA_INFINITE, FALSE);

					//WSAGetOverlappedResult 완료되는 시점에 결과를 보겠다~
					::WSAGetOverlappedResult(session.socket, &session.overlapped, &recvLen, FALSE, &flags);

				}
				else break;
			}

			cout << "Data Recv Len = " << recvLen << endl;

		}
		::closesocket(session.socket);
		::WSACloseEvent(wsaEvent)
	}

	// 윈속 종료
	::WSACleanup();
}


````

### 클라이언트쪽 소스
````
#include "pch.h"
#include <iostream>

#include <winsock2.h>
#include <mswsock.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")

void HandleError(const char* cause)
{
	int32 errCode = ::WSAGetLastError();
	cout << cause << " ErrorCode : " << errCode << endl;
}

int main()
{
	WSAData wsaData;
	if (::WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		return 0;

	SOCKET clientSocket = ::socket(AF_INET, SOCK_STREAM, 0);
	if (clientSocket == INVALID_SOCKET)
		return 0;

	u_long on = 1;
	if (::ioctlsocket(clientSocket, FIONBIO, &on) == INVALID_SOCKET)
		return 0;

	SOCKADDR_IN serverAddr;
	::memset(&serverAddr, 0, sizeof(serverAddr));
	serverAddr.sin_family = AF_INET;
	::inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr);
	serverAddr.sin_port = ::htons(7777);

	// Connect
	while (true)
	{
		if (::connect(clientSocket, (SOCKADDR*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR)
		{
			// 원래 블록했어야 했는데... 너가 논블로킹으로 하라며?
			if (::WSAGetLastError() == WSAEWOULDBLOCK)
				continue;
			// 이미 연결된 상태라면 break
			if (::WSAGetLastError() == WSAEISCONN)
				break;
			// Error
			break;
		}
	}

	cout << "Connected to Server!" << endl;

	char sendBuffer[100] = "Hello World";
	WSAEVENT wsaEvent = ::WSACreateEvent();
	WSAOVERLAPPED overlapped = {};
	overlapped.hEvent = wsaEvent;

	// Send
	while (true)
	{
		WSABUF wsaBuf;
		wsaBuf.buf = sendBuffer;
		wsaBuf.len = 100;

		DWORD sendLen = 0;
		DWORD flags = 0;

		if (::WSASend(clientSocket, &wsaBuf, 1, &sendLen, flags, &overlapped, nullptr) == SOCKET_ERROR)
		{
			if(::WSAGetLastError() == WSA_IO_PENDING)
			{
				//pending
				::WSAWaitForMultipleEvents(1, &wsaEvent, TRUE, WSA_INFINITE, FALSE);
				::WSAGetOverlappedResult(clientSocket, &overlapped, &sendLen, FALSE, &flags);
			}
		}
		cout << "Send Data Len = " << sizeof(sendBuffer) << endl;

		
	}

	// 소켓 리소스 반환
	::closesocket(clientSocket);

	// 윈속 종료
	::WSACleanup();
}
````

- WSASend, WSARecv만 비동기 논블로킹으로 하였습니다. 

- 소켓에 overlapped를 넣고 거기에 event에 wsaEvent를 넣은 이유는 완료를 Event를 통해서 받겠다는 의지앋.


- 루키스님의 서버강의를 학습 후 작성하였습니다. 