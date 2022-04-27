## 기준이 여러개일 때 lower_bound, upperboudn

- 만약 기준이 (x, y)라고 할 때 
lower_bound도 똑같다 찾는 것이 x1이상인 것중 최소이면서 동일한 것이 여러개일 때 y값중 최소를 찾을 때 쓰면된다..

````
set<pair<int, int> > s;
    s.insert(make_pair(x1, y1));
    s.insert(make_pair(, ));
    s.insert(make_pair(, ));
    s.insert(make_pair(, ));
    s.insert(make_pair(, ));

    pair<int, int> best_pos = *s.lower_bound(make_pair(x, y));
````