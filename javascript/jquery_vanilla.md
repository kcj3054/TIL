#### jquery vs vanilla

1. 바닐라를 사용한다면 -> getElementById를 이용해서 아이디를 매칭시킨후 .value를 하면 값을 가지고 올 수 있다 
 let city = document.getElementById("city").value;


 2. select 옵션이 몇가지 있을때 선택후 변경이 일어나는 것을 보여줄려면 일단 선택이 일어나면 기본적으로 
    - 상태id에 접근해서 그 상태의 display들을 none상태로 만들준 후 
    - 원하는 값의 화면을 display로 해준다 
            document.getElementById("region_02").style.display = "none";
            document.getElementById("region_064").style.display = "none";

            document.getElementById("region_" + city).style.display = "";


3. jquery를 사용 아주편리하게 할 수 있다
    - 1. $('#아이디').val() -> 이렇게 하면 그 아이디의 값을 가지고 온다 
    - 2. $('#region_02').hide(); => 해당 부분을 hide로 숨긴다 ~ 

####  중요 코드 
````
    <div class="container">
        <div>이름 : <input type="text" id="name"></div>
        <div>지역 :
            <select id="city" onchange="changeCity()">
                <!-- <option value="02">서울</option>
                <option value="064">제주</option> -->
            </select>
        </div>
        <div > 동네 : 
            <select name="" id="region_02">
                <option value="">강남</option>
                <option value="">서초</option>
            </select>
            <select name="" id="region_064" style="display: none;">
                <option value="">제주시</option>
                <option value="">서귀포시</option>
            </select>

        function changeCity( ) {
            let city = document.getElementById("city").value;
            document.getElementById("region_02").style.display = "none";
            document.getElementById("region_064").style.display = "none";

            document.getElementById("region_" + city).style.display = "";

            // let city = $('#city').val();
            // $('#region_02').hide();
            // $('#region_064').hide();
            // $('#region_' + city).show();

````