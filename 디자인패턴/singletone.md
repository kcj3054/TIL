#### singleton이란 ?

객체를 무분별하게 많이 생성하지 않고 제한된 객체를 생성 후 관리하는 것이다.
메모리 관리에 효율적이다.


#### 예시 
````
package simgleton;

public class Database {

    private String name;
    private static Database singleton;

    //Database 생성자를 private으로 하면 외부에서 마음대로 Dabase 객체를 만들 수 없다
    private Database(String name) {
        this.name = name;
    }
    public static Database getInstance(String name) {
        if(singleton == null) {
            singleton = new Database(name);
        }
        return  singleton;
    }

    public String getName() {
        return name;
    }


}
````

위의 생성자를 private를 하는 이유는 외부에서 마음대로 객체를 생성하지 못하도록 막기 위해서이다.

getInstance를 통해서 싱글톤이 null이면 만들고 그렇지 않으면  계속해서 만들어진 singleton을 관리한다. 


