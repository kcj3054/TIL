## select 모델이란?

- 블로킹 논블로킹과는 상관없다.

- select이전에 수신버퍼에 데이터가 없는데 read를 하거나 송신버퍼가 꽉 찼는데 write를 한다는 문제가 발생했다 

- 위의 문제를 막기 위해서 소켓 함수 호출이 성공할 시점을 미리 알면서 불필요한 접근을 막을 수있다.

- select 모델은 socket set을 사용한다

````
// socket set
	 1) 읽기[ 2 ] 쓰기[ ] 예외(OOB)[ ] 관찰 대상 등록
	 OutOfBand는 send() 마지막 인자 MSG_OOB로 보내는 특별한 데이터
	 받는 쪽에서도 recv OOB 세팅을 해야 읽을 수 있음
	 2) select(readSet, writeSet, exceptSet); -> 관찰 시작
	 3) 적어도 하나의 소켓이 준비되면 리턴 -> 낙오자는 알아서 제거됨
	 4) 남은 소켓 체크해서 진행
````

- 몇가지 함수도 존재한다

````
 fd_set set;
	 FD_ZERO : 비운다
	 ex) FD_ZERO(set);
	 FD_SET : 소켓 s를 넣는다
	 ex) FD_SET(s, &set);
	 FD_CLR : 소켓 s를 제거
	 ex) FD_CLR(s, &set);
	 FD_ISSET : 소켓 s가 set에 들어있으면 0이 아닌 값을 리턴한다

````
- session을 사용하는데 클라가 서버에 접속을 했을 경우 session을 통해서 관리를한다 또한 동접수만큼 세션이 생긴다.

-  또 하나의 중요한 특징은 select를 한후에 낙오자는 알아서 제거된다는 것이다.

## 단점

- while을 계속해서 돌면서 계속 소켓 set을 초기화해주어야한다. 이러한 상황이 발생하는 이유는 select를 한 후에는 찌꺼지?낙오자는 제거가 되기때문에 새로 등록할 필요가 생긴 것이다 

- 또한 fd_set이 단일 set대상으로 64개만 등록 할 수 있다는 단점이있다. 


## 소스 

````
struct Session
{
	SOCKET socket = INVALID_SOCKET;
	char recvBuffer[BUFSIZE] = {};
	int32 recvBytes = 0;
	int32 sendBytes = 0;
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

	
	vector<Session> sessions;
	sessions.reserve(100);

	//읽기[ 2 ] 쓰기[ ]
	fd_set read;
	fd_set write;

	while (true)
	{
		//소켓 set 초기화
		FD_ZERO(&read);
		FD_ZERO(&write);

		//ListenSocket 등록 acept를 할 대상을 기다린다.
		FD_SET(listenSocket, &read);

		//소켓 등록
		for (Session& s : sessions)
		{
			//현재 에코 상황이라서 현재 먼저 받고 체크하고 보낼 것 체크
			// ???? 
			if (s.recvBytes <= s.sendBytes)
			{
				FD_SET(s.socket, &read);
			}
			else
			{
				//보낼 데이터가 있을 시., 나머지 소켓체크 부분
				//s.recvBytes = recvLen;
				//read로 읽은 후 받은 recvLen에 넣으면 
				//s.recvBytes > s.sendBytes인 상황이라서 write를 시전
				FD_SET(s.socket, &write);
			}
		}

		//read write 등록 후 select를 때려야한다
		//마지막 tmimeout 인자 설정 가능 
		//timeout을 설정하면 무한대기를 하지않는다.

		//기본적으로 동기 함수 
		int32 retVal = ::select(0, &read, &write, nullptr, nullptr);
		//select한 후 낙오자는 알아서 제거된다.  그래서 소켓을 계속해서 등록한다.


		//Listener 소켓 체크 
		if (FD_ISSET(listenSocket, &read))
		{
			SOCKADDR_IN clientAddr;
			int32 addrLen = sizeof(clientAddr);
			SOCKET clientSocket = ::accept(listenSocket, (SOCKADDR*)&clientAddr, &addrLen);

			if (clientSocket != INVALID_SOCKET)
			{
				cout << "Client Connected" << endl;
				sessions.push_back(Session{ clientSocket });
			}
		}

		//나머지 소켓 체크 
		for (Session& s : sessions)
		{
			//read 체크 
			if (FD_ISSET(s.socket, &read))
			{
				int32 recvLen = ::recv(s.socket, s.recvBuffer, BUFSIZ, 0);
				if (recvLen <= 0)
				{
					//0이하라는건 연결이 끊겼다는 의미 s
					//session 제거
					continue;
				}

				s.recvBytes = recvLen;
			}
			//wirte체크
			if (FD_ISSET(s.socket, &write))
			{
				//송신버퍼가 어느정도 비어있어서 데이터를 쓸 준비가 되었다.
				//블로킹 모드 -> 모든 데이터 다 보냄
				//논브로킹 모드 -> 일부만 보낼 수가 있음 (상대방 수신 버퍼 상황에따라)
				int32 sendLen = ::send(s.socket, &s.recvBuffer[s.sendBytes], s.recvBytes - s.sendBytes, 0);


				s.sendBytes += sendLen;
				//데이터를 다 보낸 상황
				if (s.recvBytes == s.sendBytes)
				{
					s.recvBytes = 0;
					s.sendBytes = 0;
				}
			}
		}

	}

	// 윈속 종료
	::WSACleanup();
}


````


- select함수는 동기일까 비동기일까? 기본적으로 동기함수이다 왜냐하면 select함수 반환쪽을보면 값을 반환 받고 이후에 로직이 수행되는 현상이라서 동기방식이다.  -> int32 retVal = ::select(0, &read, &write, nullptr, nullptr);

### 소켓 등록, 체크 부분

````
//소켓 등록
		for (Session& s : sessions)
		{
			//현재 에코 상황이라서 현재 먼저 받고 체크하고 보낼 것 체크
			if (s.recvBytes <= s.sendBytes)
			{
				FD_SET(s.socket, &read);
			}
			else
			{
				//보낼 데이터가 있을 시., 나머지 소켓체크 부분
				//s.recvBytes = recvLen;
				//read로 읽은 후 받은 recvLen에 넣으면 
				//s.recvBytes > s.sendBytes인 상황이라서 write를 시전
				FD_SET(s.socket, &write);
			}
		}
````

- 이 부분에서 if (s.recvBytes <= s.sendBytes)일 경우 왜 read를 해야할 지 의문이었다 이유는 를 살펴보면 소켓체크할 때를 살펴보아야한다

````
//나머지 소켓 체크 
		for (Session& s : sessions)
		{
			//read 체크 
			if (FD_ISSET(s.socket, &read))
			{
				int32 recvLen = ::recv(s.socket, s.recvBuffer, BUFSIZ, 0);
				if (recvLen <= 0)
				{
					//0이하라는건 연결이 끊겼다는 의미 s
					//session 제거
					continue;
				}

				s.recvBytes = recvLen;
			}
			//wirte체크
			if (FD_ISSET(s.socket, &write))
			{
				//송신버퍼가 어느정도 비어있어서 데이터를 쓸 준비가 되었다.
				//블로킹 모드 -> 모든 데이터 다 보냄
				//논브로킹 모드 -> 일부만 보낼 수가 있음 (상대방 수신 버퍼 상황에따라)
				int32 sendLen = ::send(s.socket, &s.recvBuffer[s.sendBytes], s.recvBytes - s.sendBytes, 0);


				s.sendBytes += sendLen;
				//데이터를 다 보낸 상황
				if (s.recvBytes == s.sendBytes)
				{
					s.recvBytes = 0;
					s.sendBytes = 0;
				}
			}
		}
````


- 여기서 read 체크할 때 받은길이를 recvLen에 넣고 s.recvBytes = recvLen에 저장을 한다 해서 recvBytes가 차게 되고 (s.recvBytes > s.sendBytes)현상이 되면 받았다는 뜻이니 이제 나의 차례에서는 'write'를 시전하면되는 것이다. 


### Session 구조체 더 보기 

````
struct Session
{
	SOCKET socket = INVALID_SOCKET;
	char recvBuffer[BUFSIZE] = {};
	int32 recvBytes = 0;  //받았을 경우 저장
	int32 sendBytes = 0;  //보낸데이터 크기
};

````

- int32 recvBytes = 0;  //받았을 경우 저장,   int32 sendBytes = 0;  //보낸데이터 크기


- 루키스님의 서버 강의를 학습 후 작성하였습니다.