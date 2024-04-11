import math
import numpy as np
import matplotlib.pyplot as plt


def find_extreme_values(position):
    max_x = np.max(np.abs(position[:, 0]))
    max_y = np.max(np.abs(position[:, 1]))
    return max_x, max_y


def draw_plots(position, max_x, max_y, title, label):
    plt.figure()
    plt.plot(position[:, 0], position[:, 1], label=label)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title(title)
    plt.xlim(-max_x, max_x)
    plt.ylim(-max_y, max_y)
    plt.legend()
    plt.grid()
    plt.show()


def main():
    g = 6.6743e-11
    dt = 7200
    n = math.ceil(31556926 / dt)
    mk = 7.347e22

    # Wartości księżyca
    mz = 5.972e24
    rzk = 384000000
    v_k = math.sqrt(g * mz / rzk)

    # Wartości  słońca
    ms = 1.989e30
    rzs = 1.5e11
    v_s = math.sqrt(g * ms / rzs)

    # Dane wejściowe
    xk, yk, vx, vy = 0, rzk, v_k, 0
    xz, yz, s_vx, s_vy = 0, rzs, v_s, 0

    # Tablice
    moon_r = np.zeros(n)
    moon_theta = np.zeros(n)
    earth_x = np.zeros(n)
    earth_y = np.zeros(n)

    # Iteracja w krokach
    for i in range(n):
        # Obliczamy pozycje księżyca i prędkość
        moon_r[i] = np.sqrt((xk + xz) ** 2 + (yk + yz) ** 2)
        moon_theta[i] = np.arctan2(yk + yz, xk + xz)
        earth_x[i], earth_y[i] = xz, yz

        # Aktualizacja prędkości i pozycji księżyca
        wx, wy = 0 - xk, 0 - yk
        dzk = math.sqrt(wx ** 2 + wy ** 2)
        ux, uy = wx / dzk, wy / dzk
        a = g * mz / dzk ** 2
        ax, ay = ux * a, uy * a

        # Aktualizacja prędkości i pozycji księżyca — midpoint
        m_xk, m_yk = xk + vx * dt / 2, yk + vy * dt / 2
        m_vx, m_vy = vx + ax * dt / 2, vy + ay * dt / 2
        dx, dy = m_vx * dt, m_vy * dt
        dvx, dvy = ax * dt, ay * dt

        xk, yk = xk + dx, yk + dy
        vx, vy = vx + dvx, vy + dvy

        # Aktualizacja prędkości i pozycji ziemi
        s_wx, s_wy = 0 - xz, 0 - yz
        dzs = math.sqrt(s_wx ** 2 + s_wy ** 2)
        s_ux, s_uy = s_wx / dzs, s_wy / dzs
        s_a = g * ms / dzs ** 2
        s_ax, s_ay = s_ux * s_a, s_uy * s_a

        # Aktualizacja prędkości i pozycji księżyca — midpoint
        m_xz, m_yz = xz + s_vx * dt / 2, yz + s_vy * dt / 2
        m_s_vx, m_s_vy = s_vx + s_ax * dt / 2, s_vy + s_ay * dt / 2
        s_dx, s_dy = m_s_vx * dt, m_s_vy * dt
        s_dvx, s_dvy = s_ax * dt, s_ay * dt

        xz, yz = xz + s_dx, yz + s_dy
        s_vx, s_vy = s_vx + s_dvx, s_vy + s_dvy

    moon_x = rzk * np.cos(moon_theta)
    moon_y = rzk * np.sin(moon_theta)

    moon_position = np.column_stack((moon_x, moon_y))
    earth_position = np.column_stack((earth_x, earth_y))

    moon_extreme_values = find_extreme_values(moon_position)
    earth_extreme_values = find_extreme_values(earth_position)

    moon_max_x = moon_extreme_values[0]
    mooon_max_y = moon_extreme_values[1]
    earth_max_x = earth_extreme_values[0]
    earth_max_y = earth_extreme_values[1]

    draw_plots(moon_position, moon_max_x, mooon_max_y, "Orbita księżyc", "Księżyc")
    draw_plots(earth_position, earth_max_x, earth_max_y, "Orbita ziemi", "Ziemia")


if __name__ == "__main__":
    main()
