import numpy as np
import matplotlib.pyplot as plt
import math

# Sfera

# Masa
m_sphere = 1
# Promień
r_sphere = 2
# Moment bezwładności względem osi obrotu
ik_sphere = 2 / 3 * m_sphere * r_sphere ** 2
# Prędkość kątowa sfery wokół osi obrotu
w_sphere = 0
# Kąt obrotu sfery wokół osi obrotu
gamma_sphere = 0

# Kula

# Masa
m_ball = 1
# Promień
r_ball = 2
# Moment bezwładności względem osi obrotu
ik_ball = 2 / 5 * m_ball * r_ball ** 2
# Prędkość kątowa kuli wokół osi obrotu
w_ball = 0
# Kąt obrotu kuli wokół osi obrotu
gamma_ball = 0

# INNE ZMIENNE

# Kąt nachylenia pochyłości
alfa = np.deg2rad(45)  # kąt nachylenia pochyłości w radianach
# Wysokość pochyłości
h = 20
# Grawitacja
g = 10
# Położenie sfery wzdłuż pochyłości
sx_sphere = 0
# Prędkość sfery wzdłuż pochyłości
v_sphere = 0
# Położenie kuli wzdłuż pochyłości
sx_ball = 0
# Prędkość kuli wzdłuż pochyłości
v_ball = 0

# Wysokość obiektów nad ziemią (2, bo taki sam jak promień)
sy = 2
# Czas początkowy
t = 0  # aktualny czas w s
# Krok czasowy
dt = 0.1
# Czas końcowy
t_max = 5
# Liczba kroków
n = int(t_max / dt)

# ZMIENNE POMOCNICZE
b_start_sphere = 0
b_start_ball = 0

# Tablice do przechowywania
times = np.zeros(n)
values_Sx_sphere = np.zeros(n)
values_Sx_ball = np.zeros(n)
values_Sy_sphere = np.zeros(n)  # dodany wiersz
values_Sy_ball = np.zeros(n)  # dodany wiersz
values_gamma_sphere = np.zeros(n)
values_gamma_ball = np.zeros(n)


def linear_motion(ik, m, r, v, sx):
    # Przyspieszenie obiektu wzdłuż pochyłości
    acc = g * np.sin(alfa) / (1 + ik / (m * r ** 2))

    # Prędkość obiektu prostopadle do pochyłości
    vd = acc * dt / 2
    # Zmiana położenia obiektu wzdłuż pochyłości podczas jednego kroku czasowego
    dSx = (v + vd) * dt

    # Zmiana prędkości obiektu wzdłuż pochyłości podczas jednego kroku czasowego
    dV = acc * dt

    sx += dSx
    v += dV

    # Wysokość obiektu nad ziemią
    sy = r
    return sx, v, sy, acc


def rotational_movement(r, w, acc, b_start):
    # Przyspieszenie kątowe obiektu wokół jego osi obrotu
    eps = acc / r

    # Zmiana prędkości kątowej obiektu w jednym kroku czasowym
    dw = eps * dt

    # Zmiana kąta pomiędzy wektorem prędkości a pochyłością podczas jednego kroku czasowego
    db = (w + dw / 2) * dt

    # Kąt pomiędzy wektorem prędkości a pochyłością
    b = b_start + db

    # Kąt obrotu obiektu wokół jego osi obrotu
    gamma = math.pi / 2 - b

    # Prędkość kątowa obiektu wokół jego osi obrotu
    w += dw

    return gamma, w, db, b


# Punkt środkowy
for i in range(n):
    # Ruch sfery
    sx_sphere, v_sphere, sy, acc_sphere = linear_motion(ik_sphere, m_sphere, r_sphere, v_sphere, sx_sphere)
    gamma_sphere, w_sphere, db_sphere, b_start_sphere = rotational_movement(r_sphere, w_sphere, acc_sphere, b_start_sphere)

    # Ruch kuli
    sx_ball, v_ball, sy_ball, acc_ball = linear_motion(ik_ball, m_ball, r_ball, v_ball, sx_ball)
    gamma_ball, w_ball, db_ball, b_start_ball = rotational_movement(r_ball, w_ball, acc_ball, b_start_ball)

    # Zapisywanie wyników
    times[i] = t
    values_Sx_sphere[i] = sx_sphere
    values_Sx_ball[i] = sx_ball
    values_Sy_sphere[i] = sy
    values_Sy_ball[i] = sy_ball
    values_gamma_sphere[i] = gamma_sphere
    values_gamma_ball[i] = gamma_ball

    # Aktualizacja czasu
    t += dt

# WYKRESY

fig, axs = plt.subplots(2, 2)

# Sfera
axs[0, 0].plot(times, values_Sx_sphere)
axs[0, 0].set_xlabel('Czas (s)')
axs[0, 0].set_ylabel('sx Sfery (m)')
axs[0, 0].set_title('Ruch liniowy Sfery (sx)')

axs[1, 0].plot(times, values_Sy_sphere)
axs[1, 0].set_xlabel('Czas (s)')
axs[1, 0].set_ylabel('sy Sfery (m)')
axs[1, 0].set_title('Ruch liniowy Sfery (sy)')

# Kula
axs[0, 1].plot(times, values_Sx_ball)
axs[0, 1].set_xlabel('Czas (s)')
axs[0, 1].set_ylabel('sx Kuli (m)')
axs[0, 1].set_title('Ruch liniowy Kuli (sx)')

axs[1, 1].plot(times, values_Sy_ball)
axs[1, 1].set_xlabel('Czas (s)')
axs[1, 1].set_ylabel('sy Kuli (m)')
axs[1, 1].set_title('Ruch liniowy Kuli (sy)')

fig.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
