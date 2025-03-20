print("Digite os pontos do plano cartesiano - P1(x,y) e P2(x,y):")
x1 = float(input("x1: "))
x2 = float(input("x2: "))
y1 = float(input("y1: "))
y2 = float(input("y2: "))

dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

print(f"Distancia: {dist}")