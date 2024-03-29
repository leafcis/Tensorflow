# Perceptron

퍼셉트론은 신경망의 기원이 되는 알고리즘이다. 다수의 신호를 입력으로 받아 하나의 신호를 출력하게 되는데, 여기서 신호는 전류나 강물처럼 흐름이 있는 것이라고 생각하면 편하다.

전류가 전선을 타고 흐르는 전자를 내보내듯, 퍼셉트론 신호도 흐름을 만들고 정보를 앞으로 전달한다. 단, 실제 전류와 달리 퍼셉트론 신호는 1/0의 두 가지 값을 가질 수 있다.

1은 신호가 흐름, 0은 신호가 흐르지 않음.

아래 그림은 입력으로 2개의 신호를 받은 퍼셉트론이다. x1과 x2는 입력신호, y는 출력신호, w1과 w2는 가중치를 뜻한다.

그림의 원을 뉴런 혹은 노드라고 부르며, 입력 신호가 뉴런에 보내질 때는 각각 고유한 가중치가 곱해진다.

뉴런에서 보내온 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력하게 된다. 이를 '뉴런이 활성화한다'라고도 한다.

퍼셉트론의 동작 원리는 수식으로 나타내면 아래 그림과 같다.

퍼셉트론은 복수의 입력 신호 각각에 고유한 가중치를 부여한다. 가중치는 각 신호가 결과에 주는 영향력을 조절하는 요소로 작용한다. 즉, 가중치가 클수록 해당 신호가 그만큼 더 중요함을 뜻한다.

## AND 게이트

퍼셉트론을 활용하여 AND 게이트를 만들어보겠다.

| x1 | x2 | y |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

위 표는 AND 게이트의 진리표이다. 진리표란 입력 신호와 출력 신호의 대응 표를 뜻한다.

AND 게이트를 퍼셉트론으로 표현하려면, 위 진리표대로 작동하는 가중치와 한계 값을 정하면 된다.

위 (w1, w2, θ)를 만족하는 매개변수 조합은 (0.5, 0.5, 0.7), (1.0, 1.0, 1.0), (0.5, 0.5, 0.8)등 수많은 조합들이 있다.

매개변수를 x1 * w1 + x2 * w2 = θ를 만족하게만 만들어주면 된다.

### NAND 게이트와 OR 게이트

NAND는 Nor AND를 의미한다. 진리표로 나타내면 아래와 같다.

| x1 | x2 | y |
|---|---|---|
| 0 | 0 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |