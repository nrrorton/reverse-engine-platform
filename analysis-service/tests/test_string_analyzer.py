from pathlib import Path

from app.analyzers.string_analyzer import StringAnalyzer



def test_extract_ascii_strings(tmp_path: Path):

    binary_file = tmp_path / 'sample.bin'

    binary_file.write_bytes(
        b'\x00Hello\x00World123\xFF'
    )

    analyzer = StringAnalyzer(minimum_length=4)

    result = analyzer.analyze(binary_file)

    values = [string.value for string in result.strings]

    assert values == ['Hello', 'World123']


def test_extract_string_at_eof(tmp_path: Path):

    binary_file = tmp_path / 'sample.bin'

    binary_file.write_bytes(
        b'\x00Hello'
    )

    analyzer = StringAnalyzer()
    result = analyzer.analyze(binary_file)

    assert result.strings[0].value == 'Hello'


def test_ignore_short_strings(tmp_path: Path):

    binary_file = tmp_path / 'sample.bin'

    binary_file.write_bytes(
        b'\x00abc\x00Hello'
    )

    analyzer = StringAnalyzer()
    result = analyzer.analyze(binary_file)

    values = [string.value for string in result.strings]

    assert values == ['Hello']


def test_empty_file_returns_no_strings(tmp_path: Path):

    binary_file = tmp_path / 'empty.bin'

    binary_file.write_bytes(
        b''
    )

    analyzer = StringAnalyzer()
    result = analyzer.analyze(binary_file)

    assert result.count == 0


def test_multiple_delimiters_wont_produce_empty_string(tmp_path: Path):

    binary_file = tmp_path / 'sample.bin'

    binary_file.write_bytes(
        b'\x00\x00\x00Hello\x00\x00World\x00'
    )

    analyzer = StringAnalyzer()
    result = analyzer.analyze(binary_file)

    values = [string.value for string in result.strings]

    assert values == ['Hello', 'World']


def test_larger_file(tmp_path: Path):

    binary_file = tmp_path / 'sample.bin'

    binary_file.write_bytes(
        b'\x00' * 5000 + b'InterestingString' + b'\x00' * 5000
    )

    analyzer = StringAnalyzer()
    result = analyzer.analyze(binary_file)

    values = [string.value for string in result.strings]

    assert values == ['InterestingString']