#include <bits/stdc++.h>

using namespace std;

#define N 10000000
__int128 f[N + 1];

int main(void) {
    int n;
    cin >> n;

    int i, j;
    for(i = 1; i <= N; i++) {
        for(j = i; j <= N; j += i) {
            f[j]++;
        }
    }

    __int128 x = 0;
    for(i = 1; i <= n; i++) {
        x += (__int128)i * f[i];
    }
    cout << (unsigned long long)x << endl;

    return 0;
}