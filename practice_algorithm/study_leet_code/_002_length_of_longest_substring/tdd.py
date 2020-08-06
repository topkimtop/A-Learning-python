import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.first_input = "abcabcbb"

    def test_final(self):
        actual = Solution().lengthOfLongestSubstring("abcabcbb")
        expected = 3
        self.assertEqual(expected, actual)

        actual = Solution().lengthOfLongestSubstring("bbbbb")
        expected = 1
        self.assertEqual(expected, 1)

        actual = Solution().lengthOfLongestSubstring("pwwkew")
        expected = 3
        self.assertEqual(expected, 3)

    # 덩어리로 확인할 수 없으니 문자열을 쪼개야 한다.
    # python은 문자열을 이미 배열로 가지고 있다.
    # dict와 다른 점 테스트
    def test_access_string_index_key(self):
        # input_data index 키에 원소를 넣을 수 없다.
        with self.assertRaises(TypeError):
            print('a' == self.first_input['a'])

    # integer 값을 넣어서 가져온다.
    def test_access_string_index(self):
        self.assertEqual('a', self.first_input[0])
        self.assertEqual('a', self.first_input[3])
        self.assertEqual('b', self.first_input[4])

    def test_get_first_pattern(self):
        actual = get_first_pattern(self.first_input)
        expected = 'abc'
        self.assertEqual(expected, actual)

        actual2 = get_first_pattern('bbbbbbb')
        expected2 = 'b'
        self.assertEqual(expected2, actual2)


def get_first_pattern(s: str) -> str:
    length = len(s)
    arr = []
    acc = s[0]
    result = (s[0], len(s[:].split(s[0])))
    max_len = 0
    for i in range(length - 1):
        l1, l2 = s[i], s[i + 1]
        if l1 == l2:
            continue

        if l1 != l2:
            acc += l2
            compare_tuple = (acc, len(s[i + 1:].split(acc)))
            print(result, compare_tuple)
            if len(result[0]) < len(compare_tuple[0]):
                if result[len(result) - 1] == compare_tuple[len(compare_tuple) - 1]:
                    acc = ""
                result = compare_tuple

    print(max_len)
    print(result)
    return result[0]

# ('a', 3) ('ab', 2)
# ('ab', 2) ('abc', 2)
# ('abc', 2) ('a', 2)
# ('abc', 2) ('ab', 1)
# ('abc', 2) ('abc', 1)
# ('abc', 2) ('abcb', 1)
# 0
# ('abcb', 1)
if __name__ == '__main__':
    unittest.main()
