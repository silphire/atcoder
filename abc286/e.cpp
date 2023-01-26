#include <bits/stdc++.h>
using namespace std;

long long d[301][301];
long long v[301][301];

const int INF = INT_MAX;

int main(void) {
    int i, j, k, n;
    cin >> n;
    
    vector<int> aa(n);
    vector<string> ss(n);

    for(i = 0; i < n; i++) {
        cin >> aa[i];
    }
    for(i = 0; i < n; i++) {
        cin >> ss[i];
    }

    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            if(ss[i][j] == 'Y') {
                d[i][j] = 1;
                v[i][j] = aa[j];
            } else {
                d[i][j] = INT_MAX;
            }
        }
    }
    
    for(k = 0; k < n; k++) {
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                if(d[i][j] > d[i][k] + d[k][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                    v[i][j] = v[i][k] + v[k][j];
                } else if(d[i][j] == d[i][k] + d[k][j]) {
                    v[i][j] = max(v[i][j], v[i][k] + v[k][j]);
                }
            }
        }
    }

    int q;
    cin >> q;
    for(i = 0; i < q; i++) {
        int u1, u2;
        cin >> u1 >> u2;
        u1--; u2--;

        if(d[u1][u2] == INF) {
            cout << "Impossible" << endl;
        } else {
            cout << d[u1][u2] << " " << (v[u1][u2] + aa[u1]) << endl;
        }
    }

    return 0;
}