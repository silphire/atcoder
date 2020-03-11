#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int a, b;
    cin >> a >> b;
    
    string ab(b, a + '0');
    string ba(a, b + '0');
    cout << (a < b ? ab : ba) << endl;
    return 0;
}