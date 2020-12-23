def algo_rabin_karp(search_pattern, input_text, prime_number, number_of_characters=256):
    text_length = len(input_text)
    pattern_length = len(search_pattern)
    pattern_hash = 0
    text_hash = 0
    pattern_indexes = []

    for i in range(pattern_length):
        pattern_hash = (number_of_characters * pattern_hash + ord(search_pattern[i])) % prime_number
        text_hash = (number_of_characters * text_hash + ord(input_text[i])) % prime_number
    rest_of_string = text_length - pattern_length

    for i in range(rest_of_string + 1):
        if pattern_hash == text_hash:
            if str(i) == str(i + len(search_pattern) - 1):
                pattern_indexes.append('Pattern "' + search_pattern + '" found at index '
                                       + str(i))
            else:
                pattern_indexes.append('Pattern "' + search_pattern + '" found at index '
                                       + str(i) + '-' + str(i + len(search_pattern) - 1))

        if i < rest_of_string:
            text_hash = (number_of_characters * text_hash - ord(input_text[i]) * pow(number_of_characters, pattern_length)
                         + ord(input_text[i + pattern_length])) % prime_number
    if not pattern_indexes:
        pattern_indexes = "No patterns in text found"
    return pattern_indexes


if __name__ == '__main__':
    test_prime_number = 997
    with open('rabin_karp.in', 'r') as input_file:
        text_from_input, pattern_from_input = [line.rstrip() for line in input_file]

    result = algo_rabin_karp(pattern_from_input, text_from_input, test_prime_number)
    print(result)

    with open('rabin_karp.out', 'w') as file:
        file.write(str(result))
