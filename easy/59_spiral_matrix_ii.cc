//https://leetcode.com/problems/spiral-matrix-ii/description/
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int startx = 0;
        int starty = 0;
        int offset = 1;
        vector<vector<int>> ret(n, vector<int>(n));
        int count = 0;
        
        for (int k = 0; k < n/2; k++) {
            int i = startx;
            int j = starty;
            for (; j < n - offset; j++) {
                ret[i][j] = ++count;
            }
            for (; i < n - offset; i++) {
                ret[i][j] = ++count;
            }
            for (; j > offset - 1; j--) {
                ret[i][j] = ++count;
            }
            for (; i > offset - 1; i--) {
                ret[i][j] = ++count;
            }

            startx++;
            starty++;
            offset++;
        }

        if (1 == n % 2) {
            ret[startx][starty] = ++count;
        }
        return ret;
    }
};
