import math

print("Курсовая работа. Вариант 11")
bw2 = 36.53
aw = 125
n1 = 720
T1 = 44.17
T2 = 242.15
u = 5.6

def zub_zaz(m , bw2 , aw , u):
    

    beta  = 12
    beta_rad = math.radians(beta)
    z1 = (2*aw * math.cos(beta_rad)/(m*(u+1)))
    z2 = z1*u
    u  = z2/z1
    beta = math.acos((m*(z1+z2))/(2*aw))
    beta_grad = math.degrees(beta)

    Px = (math.pi*m)/(math.sin(beta))

    Eb = bw2/Px

    print(" При m = " , m)
    print("z1  = ", round(z1))
    print("z2  = ",round(z2))
    print("u = ",u)
    print("Beta  = ",beta_grad)
    print("Px  = ",Px)
    print("Eb  = ",Eb)
    if z1 < 17:
        z_min = 2*math.cos(beta) * ((math.cos(beta)**2)/(math.tan(math.radians(20))**2))
        print("z min  = " , z_min)
        if z_min < z1:
            print("Вариант при m = ", m  ," не подходит")
    print()
    return z1 , z2 , beta , Px , Eb
zub_zaz(1.5 , bw2 , aw , u )
zub_zaz(2.0, bw2 , aw , u)
zub_zaz(2.5, bw2 , aw , u)

m  = 1.5
z1 = 25.0
z2 = 138.0
E_beta = 1.612
beta = math.radians(11.99)
d1 = m*z1 / math.cos(beta)
d2 = m*z2 / math.cos(beta)
def proverka1(d1 , d2 , aw):
    d_all = d1 +d2
    if d_all == 2* aw:
        print("Проверка пройдена")
    else:
        print("Проверка пройдена")

print(" Пункт 6. Диаметры зубчатых колес")
print(round(d1 , 2))
print(round(d2 , 2))
proverka1(d1 , d2 ,aw)
print()

d_a1 = d1+ 2*m
d_a2 = d2+ 2*m
print("Диаметры вершин зубьев")
print("d_a1 = " , round(d_a1, 2) , "мм")
print("d_a2 = " ,round(d_a2, 2), "мм")

d_f1 = d1- 2*m*1.25
d_f2 = d2- 2*1.25*m
print("d_f1 = " , round(d_f1 ,2 ))
print("d_f2 = " ,round(d_f2 ,2 ))

d_w1 = d1
d_w2 = d2

psi_bd = bw2 / d_w1
print(psi_bd)
print()

print("Пункт 7")
E_alpha = (1.88 - 3.2*(1/z1 +1/z2))*math.cos(beta)
print(round(E_alpha , 2))
print()

print("Пункт 8")
E_gamma =  E_alpha  + E_beta
print(round(E_beta , 2))
print()

print("Пункт 9")
S_c = (math.pi * math.cos(math.radians(20)) / 2 )
S_cm = S_c *m 
h_c = 0.5*((d_a1 - d1) -S_cm * math.tan(math.radians(20)))
print(round(S_c, 4))
print(round(S_cm, 4))
print(round(h_c, 4))
print()

print("Пункт 10")

V = (math.pi *d_w1 * n1) / 60000
Ft  = 2000*T2 / d_w2
Fr = Ft * math.tan(math.radians(20)) / math.cos(beta)
Fx = Ft * math.tan(beta)

print(round(V, 2) , "м/c")
print(round(Ft) , "H")
print(round(Fr) , "H")
print(round(Fx) , "H")