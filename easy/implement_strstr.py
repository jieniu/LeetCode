'''
Implement strStr().

Return the index of the first occurrence of needle in
haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


def str_str(haystack, needle):
    '''str_str
    Return the index of the first occurrence of needle in
    haystack, or -1 if needle is not part of haystack.
    '''
    if needle == "":
        return 0

    for i, _ in enumerate(haystack):
        if len(haystack) - i < len(needle):
            break

        if haystack[i] == needle[0]:
            j = 1
            i += 1
            while j < len(needle):
                if haystack[i] != needle[j]:
                    break
                j += 1
                i += 1
            if j == len(needle):
                return i - len(needle)
        i += 1

    return -1


def main():
    """entrance"""
    assert str_str("hello", "ll") == 2, str_str("hello", "ll")
    assert str_str("aaaaa", "a") == 0, str_str("aaaaa", "a")
    assert str_str("aaaaa", "bba") == -1, str_str("aaaaa", "bbaa")
    assert str_str("abcaba", "aba") == 3, str_str("abcaba", "aba")
    assert str_str("abcaba", "abcaba") == 0, str_str("abcaba", "abcaba")
    assert str_str("", "") == 0, str_str("", "")
    assert str_str("abc", "") == 0, str_str("abc", "")
    assert str_str("", "abc") == -1


if __name__ == "__main__":
    main()
