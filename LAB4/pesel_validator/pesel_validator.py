import re

class PeselValidator:
    # Metoda statyczna do sprawdzenia formatu PESEL
    @staticmethod
    def validate_format(pesel: str) -> bool:
        """
        Sprawdza poprawność formatu numeru PESEL.

        Args:
            pesel (str): Numer PESEL do walidacji.

        Returns:
            bool: True, jeśli numer PESEL składa się dokładnie z 11 cyfr, False w przeciwnym razie.

        """
        return bool(re.match(r'^\d{11}$', pesel))

    # Metoda statyczna do walidacji cyfry kontrolnej numeru PESEL.
    @staticmethod
    def validate_check_digit(pesel: str) -> bool:
        """
        Weryfikuje poprawność cyfry kontrolnej w numerze PESEL.

        Args:
            pesel (str): Numer PESEL do walidacji.

        Returns:
            bool: True, jeśli cyfra kontrolna jest poprawna, False w przeciwnym razie.

        Algorytm:
        1. Mnoży poszczególne cyfry przez ustalone wagi
        2. Sumuje wyniki mnożenia
        3. Oblicza cyfrę kontrolną
        4. Porównuje z ostatnią cyfrą numeru PESEL

        """
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        suma = sum(int(pesel[i]) * wagi[i] for i in range(10))
        cyfra_kontrolna = (10 - (suma % 10)) % 10
        return cyfra_kontrolna == int(pesel[10])

    # Metoda statyczna do walidacji daty urodzenia
    @staticmethod
    def validate_birth_date(pesel: str) -> bool:
        """
               Waliduje datę urodzenia zawartą w numerze PESEL.

               Args:
                   pesel (str): Numer PESEL do walidacji.

               Returns:
                   bool: True, jeśli data urodzenia jest poprawna, False w przeciwnym razie.

               Opis:
               - Dekoduje rok, miesiąc i dzień z numeru PESEL
               - Uwzględnia różne zakresy dat (1800-2299)
               - Sprawdza poprawność daty przy użyciu datetime
        """
        rok = int(pesel[0:2])
        miesiac = int(pesel[2:4])
        dzien = int(pesel[4:6])

        if miesiac > 80:
            rok += 1800
            miesiac -= 80
        elif miesiac > 60:
            rok += 2200
            miesiac -= 60
        elif miesiac > 40:
            rok += 2100
            miesiac -= 40
        elif miesiac > 20:
            rok += 2000
            miesiac -= 20
        else:
            rok += 1900

        try:
            import datetime
            datetime.date(rok, miesiac, dzien)
            return True
        except ValueError:
            return False

    # Metoda statyczna do określenia płci
    @staticmethod
    def get_gender(pesel: str) -> str:
        """
                Określa płeć na podstawie numeru PESEL.

                Args:
                    pesel (str): Numer PESEL do analizy.

                Returns:
                    str: 'male' lub 'female' w zależności od cyfry płci.

                Opis:
                - Sprawdza dziesiątą cyfrę numeru PESEL
                - Cyfry nieparzyste oznaczają płeć męską
                - Cyfry parzyste oznaczają płeć żeńską
        """
        cyfra_plci = int(pesel[9])
        return 'male' if cyfra_plci % 2 == 1 else 'female'

    # Główna metoda do kompleksowej walidacji PESEL
    @staticmethod
    def is_valid(pesel: str) -> bool:
        """
               Kompleksowa walidacja numeru PESEL.

               Args:
                   pesel (str): Numer PESEL do całkowitej weryfikacji.

               Returns:
                   bool: True, jeśli numer PESEL spełnia wszystkie kryteria walidacji, False w przeciwnym razie.

               Kryteria walidacji:
               1. Poprawny format (11 cyfr)
               2. Poprawna data urodzenia
               3. Poprawna cyfra kontrolna
        """
        return (
                PeselValidator.validate_format(pesel) and
                PeselValidator.validate_birth_date(pesel) and
                PeselValidator.validate_check_digit(pesel)
        )