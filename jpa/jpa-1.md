````
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

//        Member member = new Member();
//        member.setId(2L);
//        member.setName("kcj");//
//        em.persist(member);
        List<Member> resultList = em.createQuery("select m from Member as m", Member.class)
                .setFirstResult(5)
                .setMaxResults(8)
                .getResultList();
        for (Member member : resultList) {
            System.out.println(member.getName());
        }

        tx.commit();
        em.close();
        emf.close();
````



- jpa는 특정 데이터베이스 종속 되지않는다


- List<Member> resultList = em.createQuery("select m from Member as m", Member.class) 에서 보듯이 테이블을 대상으로 sql을 하는 것이 아니라 객체를 대상으로 sql을한다.


- jpa는 트랙센션 단위로 물고늘어진다..

- jpa는 엔터티 매니저 팩토리안에서 엔터티 매니저가 만들어지면서 한 트랙젝션당 매니저하나 만들어서 사용해버리고 지운다.


- 엔터티 매니저는 스레드간 공유하면 안된다. 

