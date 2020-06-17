import math

ang = float(input("Informe o grau do triângulo: "))
sin = math.sin(math.radians(ang))  # Pra calcular o seno, cosseno e tangente, é preciso passas para radiano
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("O SENO do ângulo de {}° é = {:.2f} ".format(ang, sin))
print("O COSSENO do ângulo de {}° é = {:.2f}".format(ang, cos))
print("A TANGENTE do ângulo de {}° é = {:.2f}".format(ang, tan))
