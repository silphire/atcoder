#include <bits/stdc++.h>

using namespace std;

int aa[200001];

int main(void) {
    int i, d, q;
    cin >> d;

    cin >> aa[0];
    for(i = 1; i < d; i++) {
        int a;
        cin >> a;
        aa[i] = aa[i - 1] + a;
    }
    cin >> q;
    for(i = 0; i < q; i++) {
        int s, t;
        cin >> s >> t;
        if(aa[s - 1] > aa[t - 1]) {
            cout << s << endl;
        } else if(aa[s - 1] < aa[t - 1]) {
            cout << t << endl;
        } else {
            cout << "Same" << endl;
        }
    }

    return 0;
}