import math


def my_sin_taylor(x, n_terms):
    """
    Moja implementacja funkcji sin z użyciem rozwinięcia Taylora
    :param x: Kąt w radianach
    :param n_terms: Liczba wyrazów szeregu Taylora
    :return: Przybliżona wartość sinusa dla danego kąta i liczby wyrazów
    """
    # Normalizacja kąta do przedziału 0..2π
    normalized_x = normalize_x(x)
    # Pierwszy wyraz szeregu to x
    _sum = normalized_x

    # Obliczenia dla kolejnych wyrazów szeregu
    for p in range(2, n_terms + 1):
        part = sin_part(normalized_x, p)
        _sum += part

    return _sum


def sin_part(x, n):
    """
       Oblicza wartość kolejnego wyrazu szeregu Taylora dla sin(x)
       :param x: Znormalizowany kąt
       :param n: Numer wyrazu szeregu
       :return: Wartość wyrazu szeregu Taylora
    """

    # Obliczenie potęgi dla m (indeksu wyrazu szeregu)
    m = 2 * n - 1

    # Ustalanie znaku wyrazu szeregu (co drugi wyraz ma odwrotny znak)
    sign = -1 if n % 2 == 0 else 1

    # Obliczanie licznika i mianownika
    numerator = x ** m
    denominator = my_factorial(m)

    return sign * (numerator / denominator)


def normalize_x(x):
    """
     Przypisuje kąt x do jednej z ćwiartek
    :param x: Kąt w radianach
    :return: Znormalizowany kąt
    """

    modulo_x = x % (2 * math.pi)

    if modulo_x <= 0.5 * math.pi:
        return modulo_x
    elif modulo_x <= math.pi:
        return math.pi - modulo_x
    elif modulo_x <= 1.5 * math.pi:
        return modulo_x - 2 * math.pi
    else:
        return 2 * math.pi - modulo_x


def my_factorial(n):
    """
    Moja implementacja funkcji obliczającej silnię.
    :param n: Liczba całkowita
    :return: Silnia liczby n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * my_factorial(n - 1)


def main():
    # badane kąty
    angles = [0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi]

    # liczba wyrazów szeregu
    n_terms = 10

    for angle in angles:
        # przybliżenie sinusa z użyciem rozwinięcia Taylora
        sin_approximation = my_sin_taylor(angle, n_terms)

        # przybliżenie sinusa używając wbudowanej biblioteki Pythona
        sin_library = math.sin(angle)
        abs_difference = abs(sin_approximation - sin_library)

        print(
            f"Angle: {angle:.4f} radians, Sin Approximation: {sin_approximation:.20f}, Sin Library: {sin_library:.20f}, "
            f"Absolute Difference: {abs_difference:.20f}")


if __name__ == "__main__":
    main()
