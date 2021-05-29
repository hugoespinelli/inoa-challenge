

class DataCleaner:

    @staticmethod
    def remove_empty_space(value: str) -> str:
        return value.strip()

    @staticmethod
    def remove_dots_and_commas_and_symbols(value: str) -> str:
        return value\
            .replace(",", "")\
            .replace(".", "")\
            .replace("%", "")\
            .replace(" ", "")

    @staticmethod
    def transform_str_to_int(value: str) -> int:
        try:
            return int(DataCleaner.remove_dots_and_commas_and_symbols(value))
        except ValueError:
            return 0
