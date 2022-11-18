import math

print("Курсовая работа. Вариант 11")
F1 = 4.9
F2 = 2.9 
V_1 = 1.59 #Скорость из дано 
D = 0.25 
B = 0.5
Lh = 9 * 10**3
eff = 0.99 * 0.98 *0.99 * 0.995**3
print("Выбор двигателя")
P4 = (F1 - F2)*V_1
P_ed = P4 / eff
print(round(P4 , 2))
print(round(P_ed ,2 ))
P_ed = 4
print("Выбираем двигатель мощностью 4 кВт")
n_pr = (60*V_1) / (math.pi * D)
print(round(n_pr ,2 ))


T1 = 44.17 #T1
T2 = 242.15 #T2
u = 5.6 
n1 = 720
print(" Пункт 1")
V_2 = (n1 * T1**(1/3))/2000 #Ожидаемая окужная скорость
print(round(V_2,2))


mu3 = 0.51
mu6 = 0.42
mu9 = 0.40
print(" Пункт 2")
N_1 = 60*1 * n1 *Lh 
N_2 = N_1 / u
print(N_1)
print(N_2)
N_HE1 = N_1 * mu3
N_HE2 = N_HE1 / u 
print(N_HE1)
print(N_HE2)

N_HG1 = 8.44
N_HG2 = 1.71 
print(N_HG1)
print(N_HG2)

Z_N1 = (N_HG1 / N_HE1)**(1/20)
Z_N2 = (N_HG2 / N_HE2)**(1/20)
print("Z_N1 = " , Z_N1)
print("Z_N2 = " , Z_N2)

Gamma_Hlim1 = 1050  
Gamma_Hlim2 = 570

S_H1 = 1.1
S_H2 = 1.1

O_H1 = (Gamma_Hlim1 * Z_N1)/ S_H1 *0.9
O_H2 = (Gamma_Hlim2 * Z_N2)/ S_H2 *0.9

print("O_H1 = " , O_H1)
print("O_H2 = " , O_H2)
print()
print("Расчетное допускаемое напряжение")
Gamma_H1 = 0.45*(O_H1 * O_H1)
Gamma_H2 = 1.25 * Gamma_Hlim2
print(Gamma_H1)
print(Gamma_H2)
print("Выбираем наименьшее " , Gamma_H2)
Gamma_H = Gamma_H2



d_w1 =  675*(((T2 * 1.05)/(0.9*(Gamma_H**2)))*(u+1)/(u**2))**(1/3)
print("Начальный диаметр шестерни" , round(d_w1 , 2))
psi_bd = 0.9
b_w1 = psi_bd *d_w1
print()
print("b_w расчет = " , round(b_w1))
a_w1 = (d_w1*(u+1))/2
print("a_w = " , a_w1)

aw = 112
print("a_w = " , aw) # 4 процента есть
bw2 = b_w1*(a_w1/aw)
bw2 = round(bw2)
#bw2 = 36.53
print("bw треб = " , round(bw2))
print(aw)

b_w1 = bw2 +5 
print("b_w1 = ",round(b_w1))
print()


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
print(" Пункт 6. Диаметры зубчатых колес")
zub_zaz(1.5 , bw2 , aw , u )
zub_zaz(2.0, bw2 , aw , u)
zub_zaz(2.5, bw2 , aw , u)

m  = 1.5 #Проверирть этот пункт
z1 = 22 #Проверирть этот пункт
z2 = 124 #Проверирть этот пункт
E_beta = 1.279 #Проверирть этот пункт
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
print()

print("Пункт 12")
Z_H = 2.44
Z_E = (1/E_alpha)**(1/2)

K_Halpha0 = 1+ 0.5(8-5)*(1/((Z_E**2)-1))
K_Hw = 0.36
K_Halpha  = 1+ (K_Halpha0 -1)*K_Hw
Gamma_H = 190
K_A = 1
K_Hv = 1.04
K_Hbeta = 1.03
K_H = K_A * K_Hv * K_Hbeta *K_Halpha