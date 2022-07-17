#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int pp[200001];

int main(void) {
    int i;
    int n, k;
    cin >> n >> k;
    for(i = 0; i < n; i++) {
        cin >> pp[i];
    }
    dsu uf(n + 1);
    map<int, int> ans;

    set<int> top;
    for(i = 0; i < n; i++) {
        int x = pp[i];
        auto it = top.upper_bound(x);
        if(it != top.end()) {
            uf.merge(*it, x);
            top.erase(it);
        }
        if(uf.size(x) >= k) {
            ans[uf.leader(x)] = i + 1;
        } else {
            top.insert(x);
        }
    }

    for(i = 1; i <= n; i++) {
        if(uf.size(i) >= k) {
            cout << ans[uf.leader(i)] << endl;
        } else {
            cout << -1 << endl;
        }
    }

    return 0;
}