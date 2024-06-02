## WSAEventSelect 모델

-   이번 모델과 select모델의 차이점을 먼저 짚자
    -   select모델은 동기방식이지만, WSAEventSelect는 비동기 방식으로 완료됨을 이벤트 객체를 통해서 전달받는다
    -   그리고 select는 매번 전체 reset을 해주어야했지만 이번은 그렇지않다.
-   그렇지만 WSAEventSelect도 동일하게 최대 갯수 제한이 있다.

-   소켓과 관련된 네트워크 이벤트를 \[이벤트 객체\]를 통해 감지 받는다 (비동기 방식)

-   이벤트 객체 관련 함수들

```
생성 : WSACreateEvent 
삭제 : WSACloseEvent
신호 상태 감지 : WSAWaitForMultipleEvents
구체적인 네트워크 알아내기 : WSAEnumNetworkEvents
```

-   신호 상태 감지는 기다리다가 어떤 이벤트가 완료되면 감지하는 것이다
-   구체적인 네트워크 알아내는 것은 WSAEventSelect를 설정할 때 |로 여러가지 상태를 다 받았기에 어떤 네트워크인지 알아내는 것이다.
-   또한 이벤트는 세션과 1대1대응을 시켜준다.

-   msdn 자료를 참고한 것  
    \`\`\`\`
-   WSAWaitForMultipleEvents
    
    -   DWORD WSAAPI WSAWaitForMultipleEvents(  
        \[in\] DWORD cEvents,  
        \[in\] const WSAEVENT \*lphEvents,  
        \[in\] BOOL fWaitAll,  
        \[in\] DWORD dwTimeout,  
        \[in\] BOOL fAlertable  
        );  
        여기서 cEvents 이벤트 갯수,  
        lphEvents event...  
        fWaitAll 모두를 기다릴 것인지 아닌지  
        dwTimeout 시간..  
        DWORD WSAAPI -> 맨처음으로 완료된 인덱스를 뱉는다.
    
    -   /
    -   /\*
    -   WSAWaitForMutipleEvents
    -   !) socket
    -   2) eventObject : socket과 연동된 이벤트 객체 핸들을 넘겨주면, 이벤트 객체를
    -   non - signaled로
    -   3) networkEvent : 네트워크 이벤트 / 오류정보가 저장
    -   /
    

## 소스

```

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


    vector<WSAEVENT> wsaEvents;
    vector<Session> sessions;
    sessions.reserve(100);

    WSAEVENT listenEvent = ::WSACreateEvent();
    //session과 Event를 맞춰주기 위한 것
    wsaEvents.push_back(listenEvent);
    sessions.push_back(Session{ listenSocket });

    //WSAEventSelect관찰하겠다.
    if (::WSAEventSelect(listenSocket, listenEvent, FD_ACCEPT | FD_CLOSE) == SOCKET_ERROR)
        return 0;


    while (true)
    {
        //[][][][][][] 가장 먼저 완료되는 인덱스르 받게된다.
        // 
        //결과물을 보기 위해서 WSAWaitForMutipleEvents
        // 그중하나라도 완료되면 확인하자
        int32 index = ::WSAWaitForMultipleEvents(wsaEvents.size(), &wsaEvents[0], false,
        WSA_INFINITE, false);

        index -= WSA_WAIT_EVENT_0;

        // 해당 이벤트가 어떤 것인지 확인 (WSAEventSelect에서 FD_ACCEPT | FD_CLOSE로 해주어서)
        WSANETWORKEVENTS networkEvent;  // 관찰할려는 대상
        ::WSAEnumNetworkEvents(sessions[index].socket, wsaEvents[index], &networkEvent);

        //Listener 소켓 체크
        if (networkEvent.lNetworkEvents & FD_ACCEPT != 0)
        {
            SOCKADDR_IN clientAddr;
            int32 addrLen = sizeof(clientAddr);

            SOCKET clientSocket = ::accept(listenSocket, (sockaddr*)&clientAddr, &addrLen);

            if (clientSocket != INVALID_SOCKET)
            {
                cout << "client connected" << endl;

                WSAEVENT clientEvnet = ::WSACreateEvent();


                wsaEvents.push_back(clientEvnet);
                sessions.push_back(Session{ clientSocket });
                ::WSAEventSelect(clientSocket, clientEvnet, FD_READ | FD_WRITE | FD_CLOSE);


            }
        }

        //Client Session 소켓 체크 
        if (networkEvent.lNetworkEvents & FD_READ || networkEvent.lNetworkEvents & FD_WRITE)
        {
            Session& s = sessions[index];


            //Read
            if (s.recvBytes == 0)  //아직 받은게 없다 받아라
            {
                int32 recvLen = ::recv(s.socket, s.recvBuffer, BUFSIZ, 0);
                s.recvBytes = recvLen;
            }

            //Write
            if (s.recvBytes >= s.sendBytes)  // 많이 받았네 보내라
            {
                int32 sendLen = ::send(s.socket, &s.recvBuffer[s.sendBytes], s.recvBytes - s.sendBytes, 0);

                s.sendBytes += sendLen;

                if (s.recvBytes == s.sendBytes)
                {
                    s.recvBytes = 0;
                    s.sendBytes = 0;
                }

                cout << "Send Data = " << sendLen << endl;
            }
        }
        //FD_CLOSE 처리 
    }

    // 윈속 종료
    ::WSACleanup();
}
```

-   전체 소스는 select과 비슷하다
-   WSAWaitForMultipleEvents에서 반환 값은 여러가지 이벤트 중에서 가장 먼저 완료되는 것을 인덱스로 받는다.
-   받았지만 해당 이벤트가 어떤 이벤트인지 알기 위해서 WSAEnumNetworkEvents로 상태를 확인한다.

-   클라이언트 소켓 체크 부분

```
//Client Session 소켓 체크 
        if (networkEvent.lNetworkEvents & FD_READ || networkEvent.lNetworkEvents & FD_WRITE)
        {
            Session& s = sessions[index];
            //Read
            if (s.recvBytes == 0)  //아직 받은게 없다 받아라
            {
                int32 recvLen = ::recv(s.socket, s.recvBuffer, BUFSIZ, 0);
                s.recvBytes = recvLen;
            }

            //Write
            if (s.recvBytes >= s.sendBytes)  // 많이 받았네 보내라
            {
                int32 sendLen = ::send(s.socket, &s.recvBuffer[s.sendBytes], s.recvBytes - s.sendBytes, 0);

                s.sendBytes += sendLen;

                if (s.recvBytes == s.sendBytes)
                {
                    s.recvBytes = 0;
                    s.sendBytes = 0;
                }

                cout << "Send Data = " << sendLen << endl;
            }
        }
```

-   해당 이벤트가 read인지 write인지 확인하며 해당 세션을 보면서 s.recvBytes == 0 이라는 것은 현재 받은 데이터가 없으니 데이터를 받으라는 뜻이다.
-   write쪽은 현재 recvBytes를 보고 recvBytes가 sendBytes보다 크다면 이제 보낼 차례인 것이다 (에코 상태에서는...)

-   [https://docs.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-wsawaitformultipleevents](https://docs.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-wsawaitformultipleevents)
-   루키스님의 서버강의를 학습 후 msdn을 통해 보충 후 작성하였습니다.