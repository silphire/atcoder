#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;
using mint = modint998244353;

int main(void)
{
    int n;
    cin >> n;

    vector<int> f(n);
    scc_graph g(n);
    for(int i = 0; i < n; i++) {
        int v;
        cin >> v;
        v--;
        f[i] = v;
        g.add_edge(i, v);
    }
    
    int na = 0;
    for(auto el : g.scc()) {
        auto start = el[0];
        auto x = start;
        bool flag = false;
        for(auto j = 0; j < el.size(); ++j) {
            x = f[x];
            if(x == start) {
                flag = true;
                break;
            }
        }
        if(flag) {
            na++;
        }
    }
    mint ans = mint(2).pow(na);
    ans--;
    cout << ans.val() << endl;

    return 0;
}