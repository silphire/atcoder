#include <bits/stdc++.h>

template<typename T>
T gcd(T a, T b) {
    if(a < b) {
        return gcd(b, a);
    }

    T c;
    while(c = a % b) {
        a = b;
        b = c;
    }
    return b;
}

template<typename T>
T lcm(T a, T b) {
    return a * b / gcd(a, b);
}

using namespace std;

int main(void) {
    long long a, b;
    cin >> a >> b;
    cout << lcm(a, b) << endl;
}