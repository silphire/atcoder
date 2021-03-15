#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(void) {
    int n, m;
    cin >> n >> m;
    
    scc_graph g(n);
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g.add_edge(a, b);
    }

    auto groups = g.scc();
    cout << groups.size() << endl;
    for(const auto& c : groups) {
        cout << c.size();
        for(auto v : c) {
            cout << " " << v;
        }
        cout << endl;
    }

    return 0;
}