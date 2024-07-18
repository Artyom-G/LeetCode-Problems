//Time Complexity: O(n)
//Space Complexity: O(1) Extra
//Approach: Bit Manipulation
class Solution {
public:
    string addBinary(string a, string b) {
        int an = a.size();
        int bn = b.size();
        int max_len = max(an, bn);
        string res(max_len, '0');
        int carry = 0;

        for (int i = 0; i < max_len; ++i) {
            int a_bit = (i < an) ? a[an - 1 - i] - '0' : 0;
            int b_bit = (i < bn) ? b[bn - 1 - i] - '0' : 0;
            int sum = a_bit + b_bit + carry;
            res[max_len - 1 - i] = (sum % 2) + '0';
            carry = sum / 2;
        }

        if (carry) {
            res.insert(res.begin(), '1');
        }

        return res;
    }
};
