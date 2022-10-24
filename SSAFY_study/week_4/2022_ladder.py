'''
분할탐색
'''
class Predict:
    def __init__(self, l):
        self.l = l
        self.l_square = l ** 2
        self.a = (x_square - self.l_square) ** 0.5
        self.b = (y_square - self.l_square) ** 0.5
        self.c = self.a * self.b/(self.a + self.b) if self.a + self.b != 0 else float('INF')


x, y, c = map(float, input().split())
x_square = x ** 2
y_square = y ** 2
predict_a = Predict(0)
predict_b = Predict(min(x, y))
while abs(predict_a.l-predict_b.l) >= 0.0001:
    predict_c = Predict((predict_a.l + predict_b.l)/2)
    if predict_c.c <= c:
        predict_b = predict_c
    else:
        predict_a = predict_c
print(f'{predict_a.l:.3f}')
