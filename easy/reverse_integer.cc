#include <iostream>
#include <climits>
using namespace std;

int integer_reverse(long x) {
    int result = 0;
    while (x != 0) {
        int remainder = x % 10;
        x = x / 10;

        if (result > INT_MAX/10 || (result == INT_MAX/10 && remainder > 7))
            return 0;

        if (result < INT_MIN/10 || (result == INT_MIN/10 && remainder < -8))
            return 0;
        
        result = result * 10 + remainder;
    }

    return result;
}

int main() {
    int result = integer_reverse(-9463847412); 
    cout << result << endl;
    result = integer_reverse(-8463847412); 
    cout << result << endl;
    result = integer_reverse(7463847412); 
    cout << result << endl;
    result = integer_reverse(8463847412); 
    cout << result << endl;
    
    return 0;
}
