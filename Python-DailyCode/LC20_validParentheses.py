"""
———————————————————————
Python3 
LC20_validParentheses.py
———————————————————————
个人备注
2020-10-10
需要再次尝试
思路完全理解，利用进出栈及字典思路解题，代码还需熟悉
———————————————————————
题目出处
LC#20 有效的括号
简单
https://leetcode-cn.com/problems/valid-parentheses/

NC#52 括号序列
简单 栈 字符串
https://www.nowcoder.com/practice/37548e94a270412c8b9fb85643c8ccc2
———————————————————————
题目描述
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    1.左括号必须用相同类型的右括号闭合。
    2.左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
———————————————————————
"""

testCases = ['{[[[(]])]}', '{([(())])}', '', ')(', '([{}']

class Solution:
    """
    :type string:   str
    :rtype:         bool
    """
    def isValid(self, string):
        if len(string) % 2 == 1:
            return False #长度为奇数则False
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
            }
        stack = list()
        for char in string:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    # 对于反括号 空栈或栈内前一个括号不对应 则False
                    return False
                stack.pop()  #出栈
            else:
                stack.append(char) #压栈
        return not stack #成对的都进出栈抵消掉了 空栈则True

def main():
    for case in testCases:
        ret = Solution().isValid(case)
        print('case  : \'' + case +'\'')
        print('result: ' + str(ret))
        print()

if __name__ == '__main__':
    main()

