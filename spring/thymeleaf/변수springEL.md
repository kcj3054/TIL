#### ${}

#### 변수 표현식 : ${...}

예시 코드 
````
package com.example.demo.domain.basic;

import lombok.Data;
import org.dom4j.rule.Mode;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Data
@Controller
public class basicController {

    public String variable(Model model) {
        User userA = new User("kcj1", 222);
        User userB = new User("kcj2", 333);

        List<User> list = new ArrayList<>();

        list.add(userA);
        list.add(userB);

        Map<String, User> map = new HashMap<>();
        map.put("userA", userA);
        map.put("userB", userB);

        model.addAttribute("user", userA);
        model.addAttribute("users", list);
        model.addAttribute("userMap", map);

        return "basic/variable";
    }


    @Data
    static class User{
        private String username;
        private int age;

        public User(String username, int age) {
            this.username = username;
            this.age = age;
        }
    }

}

````

        model.addAttribute("user", userA);
        model.addAttribute("users", list);
        model.addAttribute("userMap", map);

위에서 model에 3가지를 넣고 있다 
이것을 thymeleaf에서 접근하는 방법 

#### object

<li>${user.username} = <span th:text="${user.username}"></span></li>


#### list

<li>${users[0].username} = <span th:text="${users[0].username}">

#### map

<li>${userMap['userA'].username} = <span th:text="${userMap['userA'].username}"></span></li>



# 기본 객체들 
