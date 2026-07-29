import pytest

from app.analyzers.entropy_analyzer import EntropyAnalyzer



def test_empty_data_returns_zero_entropy():

    data = b''
    analyzer = EntropyAnalyzer()
    result = analyzer.calculate(data)

    assert result == 0.0


def test_identical_bytes_have_zero_entropy():

    data = b'AAAAAAAAA'
    analyzer = EntropyAnalyzer()
    result = analyzer.calculate(data)

    assert result == 0.0


def test_known_entropy_calculation():

    data = b'AAABBC'
    analyzer = EntropyAnalyzer()
    result = analyzer.calculate(data)

    assert result == pytest.approx(1.4591, rel=1e-3)


def test_all_possible_bytes_have_max_entropy():

    data = bytes(range(256))
    analyzer = EntropyAnalyzer()
    result = analyzer.calculate(data)

    assert result == pytest.approx(8.0)