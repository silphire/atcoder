#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

string cc[150];

int main(void) {
    int i, j;
    int n;
    cin >> n;

    for(i = 0; i < n; i++) {
        cin >> cc[i];
    }

    mf_graph<int> g(2 * n + 2);
    for(i = 0; i < n; i++) {
        g.add_edge(0, i + 1, 1);
        g.add_edge(n + 1 + i, 2 * n + 1, 1);
        for(j = 0; j < n; j++) {
            if(cc[j][i] == '#') {
                g.add_edge(i + 1, n + 1 + j + 1, 1);
            }
        }
    }

    cout << g.flow(0, 2 * n + 1) << endl;

    return 0;
}