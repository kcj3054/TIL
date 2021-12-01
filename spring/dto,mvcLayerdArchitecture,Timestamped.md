

### dto가 무엇인가? 


- dto는 entity의 값을 들고다니는 것이다. 직접적인 엔터티의 값의 변경을 허용하지 않도록 하기위해서이다.


- dto를 만들 때 dto클래스명은 명시적으로 지어야한다 만약 요쳥 받는 것이 회원가입이라고 생각한다면, SignupRequrest로 명시하면서  SignupRequrest에 필요한 것들을 맴버로 두면 된다. 밑의 예시를 보자


````
@Setter
@Getter
public class SignupRequestDto {
    private String username;
    private String password;
    private String email;
    private boolean admin = false;
    private String adminToken = "";
}
````


- 이런식으로 dto는 @Getter, @Setter를 두면서 직접적인 엔터티에서는 @Setter를 두지 않는 것이 좋다. 


### mvc layerd architecture.


- 말 그대로 레이어드이다. 컨트럴로에서 요청이 들어오면 -> setvice로 넘기면서 -> service에서는 비지니스 로직을 수행하면서 userRepository에 넘기는 것이다 

- 컨트럴로에서는 setvice로 넘기니 setvice랑 연결이 되어있다  밑의 예시를 보자 ProductController는 productService를 주입했다. 


````

@RestController 
@RequiredArgsConstructor
public class ProductController {
   
    private final ProductService productService;

    // 등록된 전체 상품 목록 조회
    @GetMapping("/api/products")
    public Page<Product> getProducts(
            @RequestParam("page") int page,
            @RequestParam("size") int size,
            @RequestParam("sortBy") String sortBy,
            @RequestParam("isAsc") boolean isAsc,
            @AuthenticationPrincipal UserDetailsImpl userDetails
    ) {
        Long userId = userDetails.getUser().getId();
        page = page - 1;
        return productService.getProducts(userId, page , size, sortBy, isAsc);
    }
````


- 등등 service로직을 수행하는 부분에서는 repository를 의존한다.. 



### Timestamped

- domain에서 사용자나, 물품들은 최소 생성 시점이나, 변경 시점들을 명시할 필요가 있다 이를 편하게 하기위해서 추상 클래스인 Timestamped를 활용해서 상속을 받아 구현하면된다. 

````
@Setter
@Getter // get 함수를 자동 생성합니다.
@MappedSuperclass // 멤버 변수가 컬럼이 되도록 합니다.
@EntityListeners(AuditingEntityListener.class) // 변경되었을 때 자동으로 기록합니다.
public abstract class Timestamped {

    @CreatedDate // 최초 생성 시점
    private LocalDateTime createdAt;

    @LastModifiedDate // 마지막 변경 시점
    private LocalDateTime modifiedAt;
}
````

