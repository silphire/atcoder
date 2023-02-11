#include <bits/stdc++.h>
using namespace std;

int xx[11];

int main(void) {
    int i, j;
    int n, m;
    cin >> n >> m;
    for(i = 0; i < m; i++) {
        int c;
        cin >> c;
        int x = 0;
        for(j = 0; j < c; j++) {
            int a;
            cin >> a;
            x |= 1 << (a - 1);
        }
        xx[i] = x;
    }

    int ans = 0;
    for(i = 1; i < 1 << m; i++) {
        int x = 0;
        for(j = 0; j < m; j++) {
            if((i >> j) & 1 == 1) {
                x |= xx[j];
            }
        }
        if(x == (1 << n) - 1) {
            ans++;
        }
    }

    cout << ans << endl;
    return 0;
}