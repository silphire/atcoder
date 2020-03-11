#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    cin >> n;

    int pmin = INT_MAX;
    int ans = 0;
    for(int i = 0; i < n; i++) {
        int p;
        cin >> p;
        if(p < pmin) {
            ans++;
        }
        pmin = min(pmin, p);
    }
    cout << ans << endl;
    return 0;
}