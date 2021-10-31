#### 클라우드란?

인터넷을 통해 연결된 원격컴퓨터를 활용하는 기술이다.  
개인용컴퓨터보다 성능이 뛰어난 컴퓨터자원을 다른 곳에서 빌려서 쓸 수 있는 기술이다.

-   Iaas (Infrastructure-as-a-Service) : 물리적 서버, 네트워크, 스토리지를 가상화하여 다수의 고객을 대상으로 유연하게 제공하는 인프라 서비스
-   Saas (software-as-a-service) : 구글의 gmail이나 ms office와 같은 응용프로그램을 인터넷을 통해 제공해주는 서비스
-   EC2(Elastic Compute Cloud) : 서비스 형태에 따라서 적합한 사양을 선택할 수 있으며, 사용량만큼 비용을 지불할 수 있다
    -   ec2와 같은 가상화 서버를 인스턴스라고 부른다,
-   Amazon Auto Scaling : 서버의 조건에 따라 서버를 추가/삭제 할 수 있게 해주는 서비스로 서버 사용량이 많은 경우 추가로 생성하고, 사용하지 않는 경우 서버를 자동으로 삭제 가능
-   Amazon WorkSpace : 데스크톱 가상화 서비스로 사내 pc를 가상화해서 문서 및 데이터를 개인 pc에 보관하지 않고, 서버에 보관해서 관리 할 수 있게 해준다
-   Amazon Route 53 : 사용자의 요청을 aws에서 실행되는 다양한 인프라에 효과적으로 연결 가능, 가용성과 확장성이 우수한 DNS웹서비스이다.
-   VPC(Virtual Private Cloud) : 가상의 네트워크 인프라를 클라우드 내에 생성/ 구성해서 네트워크ㅡ를 이용한 접근 제어 vpc연결, 인터넷 게이트웨이 등의 서비스 제공과 다른 vpc와 다른 리전에 있는 vpc와 peering을 통해 보안성이 높은 네트워크 서비스 가능
    -   큰 규모의 조직이 여러 곳에 분산되어 있는 컴퓨터들을 연결하는, 보안성이 높은 사설 네트워크를 만들거나, 원격지 간에 네트워크를 서로 연결하고 암호화를 적용하여 안정적이고 보완성이 높은 서비스를 제공가능
    -   vpc는 사용자의 aws 계정을 위한 전용의 가상 네트워크를 말한다.
    -   vpc의 구성요소
        -   프라이빗 주소(인터넷을 통해 연결 할 수 없는, vpc내부에서만 사용할 수 있는 ip주소, 동일한 네트워크에서 인스턴스간  
            통신에 사용할 수 있다)
        -   퍼블릭 ip주소는 인터넷을 통해 연결할 수 있는 ip주소, 인스턴스와 인터넷 간의 통신을 위해 사용할 수 있다.

[##_Image|kage@X3GZC/btrjxcgrKpj/0d6YmNcBE2N6eNsYk2Gi50/img.png|alignCenter|width="100%" data-origin-width="1035" data-origin-height="488" data-ke-mobilestyle="widthOrigin"|||_##]

-   ELB(load Balancer) : 서버에 사용량이 증가할 경우 트래픽에 대한 부하 분산을 통해 네트워크 트래픽을 인스턴스로 전달
-   S3(Simple Storage Service) : 범용 스토리지, 데이터보관도가능하고 정적 웹 사이트 호스팅도 가능하고 여러가지 가능
-   RDS(Relational Database Services) : 관계형db를 직접 사용하지 않고 아마존에서 제공하는 데이터베이스 서비스 이용가능
-   ElasticCache : In-Memory 기반의 Cache 서비스로 , 높은 응답 속도와 신뢰성을 필요로하는 서비스에 적합한 서비스

출처 : 아마존 웹서비스 책