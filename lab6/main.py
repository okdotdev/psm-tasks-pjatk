import numpy as np
import matplotlib.pyplot as plt


# Funkcja wyliczająca przyspieszenie na podstawie pozycji
def calculate_acceleration(position, dx, n):
    acceleration = np.zeros(n + 1)
    for i in range(1, n):
        acceleration[i] = (position[i - 1] - 2 * position[i] + position[i + 1]) / dx ** 2
    return acceleration


# Funkcja wykonująca jeden krok symulacji
def step(position, speeds, accelerations, dt, dx, n):
    half_speeds = np.zeros(n + 1)
    for i in range(n + 1):
        half_speeds[i] = speeds[i] + 0.5 * accelerations[i] * dt
    new_positions = np.zeros(n + 1)
    for i in range(n + 1):
        new_positions[i] = position[i] + half_speeds[i] * dt
    new_accelerations = calculate_acceleration(new_positions, dx, n)
    new_speeds = np.zeros(n + 1)
    for i in range(n + 1):
        new_speeds[i] = half_speeds[i] + 0.5 * new_accelerations[i] * dt
    return new_positions, new_speeds, new_accelerations


# Funkcja wyliczająca energie na podstawie pozycji i prędkości
def calculate_energy(positions, accelerations, dx, n):
    ek = 0.0
    ep = 0.0
    for i in range(1, n):
        ek += 0.5 * dx * accelerations[i] ** 2
        ep += 0.5 * (positions[i + 1] - positions[i]) ** 2 / dx
    return ek, ep


def show_plot(ek_list, ep_list, ec_list):
    plt.plot(ek_list, label='Kinetic Energy')
    plt.plot(ep_list, label='Potential Energy')
    plt.plot(ec_list, label='Total Energy')
    plt.legend()
    plt.xlabel('Time(Step)')
    plt.ylabel('Energy')
    plt.show()


def main():
    length = np.pi  # długość obszaru
    n = 10  # liczba punktów siatki
    dx = length / n  # odstęp między punktami siatki
    dt = 0.2  # krok czasowy
    steps = 50  # liczba kroków czasowych

    # inicjalizacja pozycji
    positions = np.zeros(n + 1)
    for i in range(n + 1):
        positions[i] = np.sin(i * dx)

    # inicjalizacja prędkości
    speeds = np.zeros(n + 1)

    # listy energii
    ek_list = []
    ep_list = []
    ec_list = []

    acceleration = calculate_acceleration(positions, dx, n)

    # SYMULACJA
    for i in range(steps):
        positions, speeds, acceleration = step(positions, speeds, acceleration, dt, dx, n)
        en_kin, en_pot = calculate_energy(positions, speeds, dx, n)
        en_cal = en_kin + en_pot

        ek_list.append(en_kin)
        ep_list.append(en_pot)
        ec_list.append(en_cal)

    print(ek_list)
    print(ep_list)
    print(ec_list)

    show_plot(ek_list, ep_list, ec_list)


if __name__ == "__main__":
    main()
