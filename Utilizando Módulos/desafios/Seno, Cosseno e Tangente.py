import math
ângulo= float(input('Digite o ângulo que você deseja:'))
seno =math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO DE {:.2f}'.format(ângulo,seno))
cosseno=math.cos(math.radians(ângulo))
print('O ângulo de {} tem cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE DE {:.2F}'.format(ângulo,tangente))
