#!/usr/bin/env python3
"""
Zadania testowe dla ANSTA: https://www.ansta.pl/kariera/programista/
"""

import itertools
from decimal import Decimal
from typing import Iterable

def list_postal_codes(begin: str, end: str) -> Iterable[str]:
    """
    zadanie 1. generator kodów pocztowych
    przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
    """
    if begin > end:
        return list_postal_codes(end, begin)
    begin_int = int(begin.replace("-", ""))
    end_int = int(end.replace("-", ""))
    return [
        "%02d-%03d" % (code // 1000, code % 1000)
        for code in range(begin_int + 1, end_int)
    ]

def list_missing(elements: Iterable[int], last: int) -> Iterable[int]:
    """
    zadanie 2. podana jest lista zawierająca elementy o wartościach 1-n.
    napisz funkcję która sprawdzi jakich elementów brakuje

    1-n = [1,2,3,4,5,...,10] np. n=10 wejście: [2,3,7,4,9], 10 wyjście:
    [1,5,6,8,10]
    """
    return [e for e in range(1, last + 1) if e not in elements]

def list_decimal() -> Iterable[Decimal]:
    """
    zadanie 3. należy wygenerować listę liczb od 2 do 5.5 ze skokiem co 0.5,
    dane wynikowe muszą być typu decimal.
    """
    begin = Decimal("2")
    end = Decimal("5.5")
    step = Decimal("0.5")
    return list(itertools.takewhile(lambda d: d <= end, itertools.count(begin, step)))
