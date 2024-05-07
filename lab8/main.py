import numpy as np
import matplotlib.pyplot as plt


def draw_plots(final_tab, name):
    plt.figure(figsize=(8, 6))
    plt.plot(final_tab[:, 0], final_tab[:, 2], label=name, alpha=0.7)
    plt.xlabel("x")
    plt.ylabel("z")
    plt.legend()
    plt.title(name)
    plt.grid(True)
    plt.show()


# Funkcja licząca podany układ równań z zadania
def equations(tab, A=10, B=25, C=8 / 3):
    # Pobieramy wartości z tablicy wejściowej
    x, y, z = tab
    # Liczymy
    dx_dt = A * (y - x)
    dy_dt = -x * z + B * x - y
    dz_dt = x * y - C * z
    # Zwracamy
    return np.array([dx_dt, dy_dt, dz_dt])


# Euler
def calculate_euler(f, beginning_values, dt, start, end):
    # Tablica na punkty czasowe
    time = np.arange(start, end, dt)
    # Tworzymy tablicę, do której będą dodawane policzone wartości
    returned_tab = np.zeros((len(time), len(beginning_values)))
    # Inicjalizacja tablicy wyjściowej — wartościami tablic początkowych
    returned_tab[0] = beginning_values

    for i in range(1, len(time)):
        returned_tab[i] = returned_tab[i - 1] + dt * f(returned_tab[i - 1])
    return time, returned_tab


# Midpoint
def calculate_midpoint(f, parameter_values, dt, start, koniec):
    # Tablica punktów czasowych
    czas = np.arange(start, koniec, dt)
    # Tworzymy tablicę, do której będą dodawane policzone wartości
    returned_tab = np.zeros((len(czas), len(parameter_values)))
    # Inicjalizacja tablicy wyjściowej — wartościami tablic początkowych
    returned_tab[0] = parameter_values

    for i in range(1, len(czas)):
        k1 = dt * f(returned_tab[i - 1])
        k2 = dt * f(returned_tab[i - 1] + 0.5 * k1)
        returned_tab[i] = returned_tab[i - 1] + k2
    return czas, returned_tab


# RK4
def calculate_rk4(f, parameter_values, dt, start, koniec):
    # Tablica na punkty czasowe
    time = np.arange(start, koniec, dt)
    # Tworzymy tablicę, do której będą dodawane policzone wartości
    returned_tab = np.zeros((len(time), len(parameter_values)))
    # Inicjalizacja tablicy wyjściowej — wartościami tablic początkowych
    returned_tab[0] = parameter_values

    for i in range(1, len(time)):
        k1 = dt * f(returned_tab[i - 1])
        k2 = dt * f(returned_tab[i - 1] + 0.5 * k1)
        k3 = dt * f(returned_tab[i - 1] + 0.5 * k2)
        k4 = dt * f(returned_tab[i - 1] + k3)
        returned_tab[i] = returned_tab[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return time, returned_tab


def main():
    # Różne delty, bo dla 0,03 nie widać nic sensownego dla Eulera
    dt = 0.03
    dt_euler = 0.02

    start_time = 0
    end_time = 100

    # Początkowe wartości x, y, z
    beginning_values = np.array([1, 1, 1])

    # Zwrotka czasu i tablic wynikowych w celu zrobienia wykresów
    t_euler, final_euler = calculate_euler(equations, beginning_values, dt_euler, start_time, end_time)
    t_midpoint, final_midpoint = calculate_midpoint(equations, beginning_values, dt, start_time, end_time)
    t_rk4, final_rk4 = calculate_rk4(equations, beginning_values, dt, start_time, end_time)

    draw_plots(final_euler, "Euler")
    draw_plots(final_midpoint, "Midpoint")
    draw_plots(final_rk4, "RK4")


if __name__ == "__main__":
    main()
