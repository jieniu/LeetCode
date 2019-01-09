/*
 * 这是不使用外部空间的方式
 * 1. 首先过滤掉明显不是回文的bad case：负数 和 >=10 以上的可以被10整除的数
 * 2. 个位数都是回文
 * 3. 假设把整个数反转，如果反转后的数和原数相等，则可以判断是回文，但这样做可能导致整型溢出
 * 4. 沿着 3 的思路，如果只把数的低一半位反转，和高一半位对比，且最后相等，则也可以验证是回文
 */
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x >= 10 && x % 10 == 0)) {
            return false;
        }
        if (x < 10) {
            return true;
        }
        
        int last_reverse = 0;
        int reverse = 0;
        int left = x;
        while (reverse < left) {
            int remainder = left % 10;
            left = left / 10;
            
            last_reverse = reverse;
            reverse = reverse * 10 + remainder;
        }
        
        if (reverse == left || last_reverse == left) {
            return true;
        }
          
        return false;
    }
};
