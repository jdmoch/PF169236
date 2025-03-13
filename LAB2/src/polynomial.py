class Polynomial:
    """
    Klasa reprezentująca wielomian.
    Współczynniki są przechowywane w liście coeff, gdzie:
    - pierwszy element to współczynnik przy najwyższej potędze
    - ostatni element to wyraz wolny

    Przykład: 3x^2 + 2x + 1 będzie reprezentowane jako [3, 2, 1]
    """

    def __init__(self, coefficients):
        """
        Inicjalizacja wielomianu z listy współczynników.

        Args:
            coefficients: Lista współczynników, pierwszy element to współczynnik przy najwyższej potędze
        """
        # Kopiujemy listę, aby uniknąć przypadkowych modyfikacji zewnętrznych
        self.coeff = list(coefficients)

        # Usuwamy zbędne zera z lewej strony
        self._remove_leading_zeros()

        # Jeśli lista jest pusta, to ustawiamy wielomian zerowy [0]
        if not self.coeff:
            self.coeff = [0]

    def _remove_leading_zeros(self):
        """Usuwa zbędne zera z lewej strony (przy najwyższych potęgach)."""
        while len(self.coeff) > 1 and self.coeff[0] == 0:
            self.coeff.pop(0)

    def degree(self):
        """Zwraca stopień wielomianu."""
        return len(self.coeff) - 1

    def evaluate(self, x):
        """
        Oblicza wartość wielomianu dla danego x za pomocą schematu Hornera.

        Args:
            x: Wartość, dla której obliczamy wielomian

        Returns:
            Wartość wielomianu w punkcie x
        """
        result = 0
        for coef in self.coeff:
            result = result * x + coef
        return result

    def __str__(self):

        """Zwraca czytelną reprezentację wielomianu jako string."""

        if len(self.coeff) == 1:
            return str(self.coeff[0])

        result = []
        degree = len(self.coeff) - 1

        for i, coef in enumerate(self.coeff):
            current_degree = degree - i

            if coef == 0:
                continue

            term = ""

            # Odpowiedni zapis
            if current_degree == 0:
                term = str(abs(coef))
            elif abs(coef) == 1:
                term = "x" if current_degree == 1 else f"x^{current_degree}"
            else:
                term = str(abs(coef)) + ("x" if current_degree == 1 else f"x^{current_degree}")

            # Dodanie plus lub minus
            if coef < 0:
                term = "- " + term if result else "-" + term
            else:
                term = ("+ " if result else "") + term

            result.append(term)

        return " ".join(result) if result else "0"

    def __repr__(self):
        """Zwraca reprezentację wielomianu do debugowania."""
        return f"Polynomial({self.coeff})"

    def __eq__(self, other):
        """
        Porównuje dwa wielomiany.

        Args:
            other: Inny wielomian lub liczba do porównania

        Returns:
            True jeśli wielomiany są równe, False w przeciwnym przypadku
        """
        if isinstance(other, Polynomial):
            return self.coeff == other.coeff
        elif isinstance(other, (int, float)):
            return len(self.coeff) == 1 and self.coeff[0] == other
        return False

    def __add__(self, other):
        """
        Dodaje dwa wielomiany lub wielomian i liczbę.

        Args:
            other: Inny wielomian lub liczba do dodania

        Returns:
            Nowy wielomian będący sumą
        """
        if isinstance(other, Polynomial):
            # Dodanie dwóch wielomianów
            result_degree = max(len(self.coeff), len(other.coeff))
            result = [0] * result_degree

            # Dodanie współczynnika od tyłu
            for i in range(1, len(self.coeff) + 1):
                result[-i] += self.coeff[-i]

            for i in range(1, len(other.coeff) + 1):
                result[-i] += other.coeff[-i]

            return Polynomial(result)
        elif isinstance(other, (int, float)):

            # Dodanie wielomianu i liczby
            result = self.coeff.copy()
            result[-1] += other
            return Polynomial(result)


    def __radd__(self, other):
        """
        Obsługuje dodawanie z liczbą po lewej stronie.

        Args:
            other: Liczba do dodania po lewej stronie

        Returns:
            Nowy wielomian będący sumą
        """
        return self + other

    def __sub__(self, other):
        """
        Odejmuje wielomian lub liczbę od tego wielomianu.

        Args:
            other: Wielomian lub liczba do odjęcia

        Returns:
            Nowy wielomian będący różnicą
        """
        if isinstance(other, Polynomial):
            # Odejmuje wielomian od wielomianu
            result_coeffs = [0] * max(len(self.coeff), len(other.coeff))

            # Kopiuje współczynniki z pierwszego wielomianu
            for i in range(len(self.coeff)):
                pos = len(result_coeffs) - len(self.coeff) + i
                result_coeffs[pos] = self.coeff[i]

            # Odejmuje współczynniki z drugiego wielomianu
            for i in range(len(other.coeff)):
                pos = len(result_coeffs) - len(other.coeff) + i
                result_coeffs[pos] -= other.coeff[i]

            return Polynomial(result_coeffs)

        elif isinstance(other, (int, float)):
            # Odejmuje liczbę od wielomianu
            result_coeffs = self.coeff.copy()
            result_coeffs[-1] -= other
            return Polynomial(result_coeffs)
        else:
            return NotImplemented

    def __rsub__(self, other):
        """
        Obsługuje odejmowanie wielomianu od liczby (liczba po lewej stronie).

        Args:
            other: Liczba, od której odejmujemy wielomian

        Returns:
            Nowy wielomian będący różnicą
        """
        result = (-1) * self
        result.coeff[-1] += other
        return result

    def __mul__(self, other):
        """
        Mnoży wielomian przez inny wielomian lub liczbę.

        Args:
            other: Wielomian lub liczba do pomnożenia

        Returns:
            Nowy wielomian będący iloczynem
        """
        if isinstance(other, Polynomial):
            # Mnoży dwa wielomiany
            result_degree = len(self.coeff) + len(other.coeff) - 1
            result = [0] * result_degree

            for i in range(len(self.coeff)):
                for j in range(len(other.coeff)):
                    idx = i + j
                    result[idx] += self.coeff[i] * other.coeff[j]

            return Polynomial(result)
        elif isinstance(other, (int, float)):
            # Mnoży wielomian przez liczbę
            if other == 0:
                return Polynomial([0])

            result = [coef * other for coef in self.coeff]
            return Polynomial(result)

    def __rmul__(self, other):
        """
        Obsługuje mnożenie liczby przez wielomian (liczba po lewej stronie).

        Args:
            other: Liczba do pomnożenia po lewej stronie

        Returns:
            Nowy wielomian będący iloczynem
        """
        return self * other