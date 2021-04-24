find_set과 union을 사용하는 문제!

 

각 노드마다 부모를 가리키키는 리스트를 만들어주고

union연산을 통해 두 집합을 통합시킨다. 뒤에 오는 인자(y)가 부모노드가 된다.

여기서 find_set연산을 하는데, 노드X가 부모노드값과 같으면 노드 x값이 리턴이 되고 아니라면 다시 find_set함수로 들어가서 부모노드를 찾아 리턴시켜준다.

------

예시로

union(1,2)을 보면 parent =[0,1,2] 이다.

parent[find_set(2)] = find_set(1)

 

find_set(2)은

if 2 == parent[2]:

 return 2

 

대입하면

union(1,2):

parent[2] = find_set(1) 이 되고

 

find_set(1)은 리턴 1이므로 parent[2] = 1이 되어 

 

parent =[0,1,1]이 된다.

이런식으로 부모노드를 갱신해주어 부모노드의 개수를 출력해주면 되는 문제이다.