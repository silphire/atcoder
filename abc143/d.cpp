#include <bits/stdc++.h>

using namespace std;

int n;
int a[2000];

int main(void) {
    cin >> n;
    int i, j, k;
    for(i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);

    int ans = 0;
    for(i = 0; i < n; i++) {
        for(j = i + 1; j < n; j++) {
            for(k = j + 1; k < n; k++) {
                if(a[i] + a[j] > a[k]) {
                    ans++;
                }
            }
        }
    }
    cout << ans << endl;

    return 0;
}