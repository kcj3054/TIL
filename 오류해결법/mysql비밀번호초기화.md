#### 방법
순서대로 하면된다 

1. mysql -u root -p mysql  (mysql에 로그인)
당연히 안된다 그래서 service에서 mysql 정지 시킨 후 

2. cd C:\APM_Setup\Server\MySQL5\bin로 bin으로 이동

3. mysqld.exe --skip-grant
이 명렁어를 주고 다른 cmd를 열어서

4. mysql -u root로 mysql 로그인

5. mysql -u root

6. use mysql

7. select * from user;

8. 비밀번호 변경 
update user set password=password('1234') where user='root';

9. 적용 flush privileges;

10. 종료exit


#### 하다가 발생한 에러들..
cf : mysql에서 잘못된 명령어를 쳤을경우
-
-
-
로 들어오게 된다 이럴때 빠져나가는 방법은 ;를 치면된다.