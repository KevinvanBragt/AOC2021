from input.input_parser import InputParser, OutputTypes


class Day8:

    @staticmethod
    def solve() -> int:
        data = [[x.split() for x in line.split('|')] for line in InputParser.get_input("day8", OutputTypes.List)]
        counter = 0
        for line in data:
            translations = Day8.decode(line[0])
            print(translations)
            value = Day8.decode_line_with_values(line[1], translations)
            counter += value

        return counter

    @staticmethod
    def decode_line_with_values(line: [str], translations_dict: dict):
        value_of_line = ""
        for pattern in line:
            if pattern is None:
                print("ERROR")
            value = Day8.decode_single_pattern(Day8.sort_pattern(pattern), translations_dict)
            value_of_line += str(value)
        return int(value_of_line)

    @staticmethod
    def decode_single_pattern(pattern: str, translations_dict: dict) -> int:
        for key, value in translations_dict.items():
            if value == pattern:
                return int(key)

    @staticmethod
    def get_pattern_for_value(decode_translations: dict[str: int], searchvalue: int):
        return decode_translations[str(searchvalue)]

    @staticmethod
    def decode(coded_strings: [str]):
        translations = {'0': None, '1': None,
                        '2': None, '3': None,
                        '4': None, '5': None,
                        '6': None, '7': None,
                        '8': None, '9': None}

        for pattern in coded_strings:
            sorted_pattern = Day8.sort_pattern(pattern)
            match len(sorted_pattern):
                case 2:
                    translations['1'] = sorted_pattern
                case 3:
                    translations['7'] = sorted_pattern
                case 4:
                    translations['4'] = sorted_pattern
                case 7:
                    translations['8'] = sorted_pattern

        for pattern in coded_strings:
            sorted_pattern = Day8.sort_pattern(pattern)
            match len(sorted_pattern):
                case 5:
                    if translations['4'] and Day8.count_intersect(sorted_pattern, translations['4']) == 2:
                        translations['2'] = sorted_pattern
                    elif translations['1'] and Day8.count_intersect(sorted_pattern, translations['1']) == 2:
                        translations['3'] = sorted_pattern
                    else:
                        translations['5'] = sorted_pattern

        for pattern in coded_strings:
            sorted_pattern = Day8.sort_pattern(pattern)
            match len(sorted_pattern):
                case 6:
                    if translations['5'] and Day8.count_intersect(sorted_pattern, translations['5']) == 4:
                        translations['0'] = sorted_pattern
                    elif translations['5'] and Day8.count_intersect(sorted_pattern, translations['3']) == 5:
                        translations['9'] = sorted_pattern
                    else:
                        translations['6'] = sorted_pattern

        return translations

    @staticmethod
    def sort_pattern(pattern: str):
        x = list(pattern)
        x.sort()
        result = "".join(x)
        return result

    @staticmethod
    def count_intersect(a, b):
        return len([value for value in a if value in b])
