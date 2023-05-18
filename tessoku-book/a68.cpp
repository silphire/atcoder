#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(void) {
    int i;

    int n, m;
    cin >> n >> m;

    mf_graph<int> g(n + 1);
    for(i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        g.add_edge(a, b, c);
    }

    cout << g.flow(1, n) << endl;
    return 0;
}