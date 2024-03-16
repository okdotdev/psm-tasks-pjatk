from typing import List
import pandas as pd
import matplotlib.pyplot as plt

# Lista globalna przechowująca współrzędne
basic_coordinate_x_list = []
basic_coordinate_y_list = []

advanced_coordinate_x_list = []
advanced_coordinate_y_list = []


class Euler:
    def __init__(self, coordinate_x: float, coordinate_y: float,
                 velocity_x: float, velocity_y: float,
                 acceleration_x: float, acceleration_y: float,
                 change_position_x: float, change_position_y: float,
                 change_velocity_x: float, change_velocity_y: float,
                 time: int):
        """
        Inicjalizuje obiekt klasy Euler.

        :param coordinate_x: Współrzędna x.
        :param coordinate_y: Współrzędna y.
        :param velocity_x: Prędkość w kierunku x.
        :param velocity_y: Prędkość w kierunku y.
        :param acceleration_x: Przyspieszenie w kierunku x.
        :param acceleration_y: Przyspieszenie w kierunku y.
        :param change_position_x: Zmiana pozycji w kierunku x.
        :param change_position_y: Zmiana pozycji w kierunku y.
        :param change_velocity_x: Zmiana prędkości w kierunku x.
        :param change_velocity_y: Zmiana prędkości w kierunku y.
        :param time: Czas.
        """
        self.time = time
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.change_position_x = change_position_x
        self.change_position_y = change_position_y
        self.change_velocity_x = change_velocity_x
        self.change_velocity_y = change_velocity_y


def create_euler_objects(time_derivative, gravity_x, vertical_gravity_y,
                         mass, medium_resistance, time, is_basic=True):
    """
    Tworzy obiekty klasy Euler.

    :param time_derivative: Pochodna czasu.
    :param gravity_x: Grawitacja w kierunku poziomym.
    :param vertical_gravity_y: Grawitacja w kierunku pionowym.
    :param mass: Masa cząstki.
    :param medium_resistance: Współczynnik oporu medium.
    :param time: Czas.
    :param is_basic: Flaga określająca, czy metoda to metoda podstawowa czy ulepszona. Domyślnie True (metoda podstawowa).
    :return: Lista obiektów klasy Euler.
    """
    euler_list: List[Euler] = []
    coordinate_x = 0
    coordinate_y = 0
    velocity_x = 10
    velocity_y = 10

    for i in range(0, 200, int(time_derivative * 100)):
        if is_basic:
            basic_coordinate_x_list.append(coordinate_x)
            basic_coordinate_y_list.append(coordinate_y)
        else:
            advanced_coordinate_x_list.append(coordinate_x)
            advanced_coordinate_y_list.append(coordinate_y)

        acceleration_x = (mass * gravity_x - medium_resistance * velocity_x) / mass
        acceleration_y = (mass * vertical_gravity_y - medium_resistance * velocity_y) / mass

        change_position_x = time_derivative * velocity_x
        change_position_y = time_derivative * velocity_y

        change_velocity_x = time_derivative * acceleration_x
        change_velocity_y = time_derivative * acceleration_y

        coordinate_x += change_position_x
        coordinate_y += change_position_y

        velocity_x += change_velocity_x
        velocity_y += change_velocity_y

        euler_list.append(
            Euler(coordinate_x, coordinate_y, velocity_x, velocity_y,
                  acceleration_x, acceleration_y,
                  change_position_x, change_position_y,
                  change_velocity_x, change_velocity_y, time))

        time += 1

    return euler_list


def print_euler_dataframe(euler_list):
    """
    Wyświetla ramkę danych z listy obiektów klasy Euler.

    :param euler_list: Lista obiektów klasy Euler.
    """
    df_euler = pd.DataFrame([e.__dict__ for e in euler_list])
    print(df_euler.to_string(index=False))


if __name__ == '__main__':
    time_derivative = float(input("Podaj pochodną czasu: "))  # 0.01
    grav_x = float(input("Podaj grawitację w kierunku poziomym: "))  # 0
    grav_y = float(input("Podaj grawitację w kierunku pionowym: "))  # -10
    mass = float(input("Podaj masę cząstki: "))  # 1
    resistance = float(input("Podaj współczynnik oporu medium w zakresie od 0 do 1: "))  # 0.2
    print()

    time = 1

    print("Podstawowa")
    basic_euler_list = create_euler_objects(time_derivative, grav_x, grav_y, mass, resistance, time)
    print_euler_dataframe(basic_euler_list)
    print()

    print("Ulepszona")
    improved_euler_list = create_euler_objects(time_derivative, grav_x, grav_y, mass, resistance, time, is_basic=False)
    print_euler_dataframe(improved_euler_list)

    # Rysowanie wykresu
    plt.plot(basic_coordinate_x_list, basic_coordinate_y_list, label="Podstawowa")
    plt.plot(advanced_coordinate_x_list, advanced_coordinate_y_list, label="Ulepszona")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("dt: " + str(time_derivative) +
              "; gx: " + str(grav_x) +
              "; gy: " + str(grav_y) +
              "; masa: " + str(mass) +
              "; k: " + str(resistance))
    plt.legend()
    plt.show()
