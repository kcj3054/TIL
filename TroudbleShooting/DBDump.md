1. live 게임 환경에서 정기 점검 후 DB 데이터가 잘못들어간 부분이 있어서, 빠르게 그날 대응이 필요했었다. 그래서 지원팀에서 DB DUMP를 해주고 계셨는데, 키바나로 로그 확인 중 MYSQL DEADLOCK이 여러군데에서 발생하였다.  모두 기존의 쿼리문제인지 DUMP 문제인지 확인 하던 중  DUMP로 인해 데드락이 걸렸다는 것을 확인했다.
    - MYSQL DUMP를 MASTER DATA에 뜨게된다면, Table 단위로 Lock 발생하게 되는데 해당 시점에서 다른 쿼리랑 경합이 발생하며 deadlock이 발생한 것같다.! 