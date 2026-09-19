import sympy as sp
A=sp.sympify(input("Введите коэффициент (А):"))
B=sp.sympify(input("Введите коэффициент (B):"))
C=sp.sympify(input("Введите коэффициент (C):"))
ob_vid=sp.sympify(input("Введите общий вид уравнения:"))
B_I=(B/2)**2
x,y=sp.symbols('x y',positive=True)
i_opr=B_I-A*C
print(f"значение иакова критерия ={i_opr}")
if i_opr.is_positive:
    print("уравнение относится к гиперболическому типу")
elif i_opr.is_negative:
    print("уравнение относится к элиптическому типу")
elif i_opr.is_zero:
    print("уравнение относится к параболическому типу")
else:
    print("тип уравнения определить невозможно")
Discriminant_h=B**2-4*A*C

    

t1 = (-B - sp.sqrt(Discriminant_h)) / (2 * A)
t2 = (-B + sp.sqrt(Discriminant_h)) / (2 * A)
if Discriminant_h.is_zero:
    integral_t1=sp.integrate(t1,x)
    ksi=y-integral_t1
    if ksi==x:
        eta=y
    else:
        eta=x
else:
    integral_t1=sp.integrate(t1,x)
    integral_t2=sp.integrate(t2,x)
    ksi=y-integral_t1
    eta=y-integral_t2
V_KSI,V_ETA=sp.symbols('V_KSI V_ETA')
V_KSI_KSI,V_ETA_ETA=sp.symbols('V_KSI_KSI V_ETA_ETA')
V_KSI_ETA=sp.symbols('V_KSI_ETA')
u_xx, u_xy, u_yy, u_x, u_y = sp.symbols('u_xx u_xy u_yy u_x u_y')
U_x=V_KSI*sp.diff(ksi,x)+V_ETA*sp.diff(eta,x)    
U_y=V_KSI*sp.diff(ksi,y)+V_ETA*sp.diff(eta,y)
U_XX=V_KSI_KSI*((sp.diff(ksi,x))**2)+2*V_KSI_ETA*sp.diff(ksi,x)*sp.diff(eta,x)+V_ETA_ETA*(sp.diff(eta,x))**2+V_KSI*sp.diff(ksi,x,2)+V_ETA*sp.diff(eta,x,2)
U_XY=V_KSI_KSI*sp.diff(ksi,x)*sp.diff(ksi,y)+V_KSI_ETA*(sp.diff(ksi,x)*sp.diff(eta,y)+sp.diff(ksi,y)*sp.diff(eta,x))+V_ETA_ETA*sp.diff(eta,x)*sp.diff(eta,y)+V_KSI*sp.diff(ksi,x,y)+V_ETA*sp.diff(eta,x,y)
U_YY=V_KSI_KSI*(sp.diff(ksi,y)**2)+2*V_KSI_ETA*sp.diff(ksi,y)*sp.diff(eta,y)+V_ETA_ETA*(sp.diff(eta,y)**2)+V_KSI*sp.diff(ksi,y,y)+V_ETA*sp.diff(eta,y,y)
equation = ob_vid.subs({u_xx: U_XX, u_xy: U_XY, u_yy: U_YY, u_x: U_x, u_y: U_y})
# Запускаем автомат тотального упрощения SymPy
# Он сам раскроет комплексные квадраты, уничтожит I и сожмёт подобные!
canonical_view = sp.simplify(equation)

# Собираем красивое уравнение и приравниваем к нулю
final_eq = sp.Eq(canonical_view, 0)
print(f"Канонический вид уравнения: {final_eq}")
