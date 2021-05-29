from pytest import mark

from data_cleaning import DataCleaner


@mark.parametrize(
    "word, expected",
    [
        (" aaaa", "aaaa"),
        ("aaaa ", "aaaa"),
        (" aaaa ", "aaaa"),
        ("aaaa", "aaaa"),
    ]
)
def test_should_remove_empty_spaces(word: str, expected: str) -> None:
    clean_word = DataCleaner.remove_empty_space(word)

    assert clean_word == expected


@mark.parametrize(
    "word, expected",
    [
        ("18,90", 1890),
        ("23,43", 2343),
        ("23.32", 2332),
        ("-23.32", -2332),
    ]
)
def test_should_transform_to_int(word: str, expected: str) -> None:
    clean_word = DataCleaner.transform_str_to_int(word)

    assert clean_word == expected


@mark.parametrize(
    "word, expected",
    [
        ("18,90", "1890"),
        ("23,43", "2343"),
        ("23.32", "2332"),
        ("23.32 %", "2332"),
    ]
)
def test_should_remove_dots_and_commands(word: str, expected: str) -> None:
    clean_word = DataCleaner.remove_dots_and_commas_and_symbols(word)

    assert clean_word == expected
