# class Solution(object):
#     def backspaceCompare(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: bool
#         """


#         # 处理字符串
#         def pre(s):
#             array = ''
#             for element in s:
#                 if element == "#":
#                     array = array[:len(array)-1]
#                 else:
#                     array += element
#                 return array


#         # 判断是否相等
#         pre_S = pre(S)
#         pre_T = pre(T)
#         if pre_S == pre_T:
#             return True
#         else:
#             return False

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        a = getTrue(S)
        b = getTrue(T)

        if a == b:
            return True
        else:
            return False


def getTrue(s):
    outer = ''
    for char in s:
        if char == '#':
            outer = outer[:len(outer) - 1]
        else:
            outer += char
    print(outer)
    return outer