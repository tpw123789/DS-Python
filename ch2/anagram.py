"""異序詞"""


def anagram_solution1(s1, s2):
    """清點法 O(n^2)"""
    # 第二個字串轉陣列
    s2_list = list(s2)
    position1 = 0
    still_ok = True

    while position1 < len(s1) and still_ok:
        position2 = 0
        found = False
        while position2 < len(s2_list) and not found:
            if s1[position1] == s2_list[position2]:
                # 找到相同字元
                found = True
            else:
                position2 += 1

        if found:
            s2_list[position2] = None
        else:
            still_ok = False

        position1 += 1

        return still_ok


def anagram_solution2(s1, s2):
    """排序法 O(n) 實際上使用sort()有代價 時間複雜度是O(n^2)或O(nlogn)"""
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()

    position = 0
    matches = True
    while position < len(s1) and matches:
        if s1_list[position] == s2_list[position]:
            position += 1
        else:
            matches = False
        return matches


def anagram_solution3(s1, s2):
    """記數法 O(n)"""
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        position = ord(s1[i]) - ord('a')
        # 出現英文字母+1
        c1[position] = c1[position] + 1

    for i in range(len(s2)):
        position = ord(s2[i]) - ord('a')
        c2[position] = c2[position] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok

