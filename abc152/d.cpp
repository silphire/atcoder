#include <bits/stdc++.h>

using namespace std;

int c[10][10];

int main(void) {
    int n;
    cin >> n;
    
    for(int i = 1; i <= n; i++) {
        if(i % 10 == 0) continue;

        int y = i;
        while(y >= 10) {
            y /= 10;
        }

        c[y][i % 10]++;
    }

    long long ans = 0;
    for(int j = 1; j <= 9; j++) {
        for(int i = 1; i <= 9; i++) {
            ans += c[i][j] * c[j][i];
        }
    }

    cout << ans << endl;
    return 0;
}