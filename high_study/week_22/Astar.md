# 7주차 : A*

> **휴리스틱 추정값**을 적용해 최단 경로를 찾아내는 그래프 탐색 알고리즘
> 
- [참고 이미지](https://choiseokwon.tistory.com/210)

### Dijkstra와 무엇이 다른가?

- 출발지와 **목적지**가 존재
    - 즉, A star는 특정 **목적지와 가까울 것으로 예측되는 노드**를 우선적으로 탐색하고자 한다.
- 휴리스틱 추정값
    - 목적지와 가까운지 아닌지를 예측하는 추정치
- 간선이 아닌 **노드** 중심 탐색(heap에 들어가는 값 기준)

### 휴리스틱(heuristics) 추정값

![KakaoTalk_20220604_165750819.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b34556c4-8fdd-40f0-836f-be88eb79e593/KakaoTalk_20220604_165750819.gif)

> **휴리스틱**(heuristics) 또는 **발견법**(發見法)이란 
불충분한 시간이나 정보로 인하여 합리적인 판단을 할 수 없거나, 체계적이면서 합리적인 판단이 굳이 필요하지 않은 상황에서 사람들이 빠르게 사용할 수 있게 보다 용이하게 구성된 간편추론의 방법이다.
> 

*ref. [https://ko.wikipedia.org/wiki/휴리스틱_이론](https://ko.wikipedia.org/wiki/%ED%9C%B4%EB%A6%AC%EC%8A%A4%ED%8B%B1_%EC%9D%B4%EB%A1%A0)*

~~즉, 대충 찍어 맞춘 추정치~~

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f03024e2-f577-44be-9500-1f7e6342540a/Untitled.png)

- `g(n)`: dijkstra에서 사용하던 가중치
- `h(n)`: 휴리스틱 추정치

즉, 추정 가능해야 함 → 일반 그래프에서는 사용하기 어려움

따라서, 물리적인 거리가 있는 맵에서 사용함

Open, closed 노드의 갱신이 없음 ← 휴리스틱 때문에 가능