## windows redis 사용 

- windows에서는 redis를 사용하기위해서 windows redis를 사용하거나, ubuntu를 설치해서 redis를 사용하는 것도 존재한다.

- windows에서 ubuntu를 사용?
    - wsl(windows subsystem linux)를 이용하면 ubuntu를 사용할 수 있다.

    - 설치 방법 
        - windows 기능 켜기 끄기 에서 가상 머신을 on한다
        - cmd에서 wsl2로 설정한다. 
        - windowsAppStore에서 ubuntu를 설치 후 재시작하면 해당 화면을 볼 수 있다. 
        
        [](./ubuntu초기회면(windows).png)

- ubuntu에서 바로 redis를 설치해도 좋지만 docker위에서 사용한다면 더욱 편리하게 사용가능하다, docker에 대해서는 더욱 알아보는 것으로하자.