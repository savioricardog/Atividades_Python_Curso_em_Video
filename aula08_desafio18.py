import math
a1 = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a1))
c = math.cos(math.radians(a1))
t = math.tan(math.radians(a1))
print('O ângulo de {} tem o seno de {:.2f}' .format(a1, s))
print('O ângulo de {} tem o cosseno de {:.2f}' .format(a1, c))
print('O ângulo de {} tem a tangente de {:.2f}' .format(a1, t))