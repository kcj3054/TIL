1. public ip, private pi
- server가 클라이언트로 주소를 제공하는 단계에서 client와 server는 망이 다르기에 공인 ip로 작성해야하지만, 사설 ip로 데이터를 삽입 한 후 장비 세팅 시 문제가 발생했던 적이 있었습니다.

    - 위 문제를 해결하기 전에 방화벽이 막혀있는 테스트하기 위해서 대상 머신으로 telnet을 시도하거나, 클라이언트가 연결한 대상 서버의 port가 open 되어있는지 확인 하기 위해서 netstat -na | grep "LISTENING" 을 이용하여 PORT확인도 시도하면서 잘못된 부분들을 STEP BY STEP으로 확인해 나갔습니다. 