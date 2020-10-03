#include <atcoder/dsu.hpp>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n, q;
    cin >> n >> q;

    atcoder::dsu d(n);

    for(int i = 0; i < q; i++) {
        int t, u, v;
        cin >> t >> u >> v;
        if(t == 0) {
            d.merge(u, v);
        } else {
            if(d.same(u, v)) {
                cout << 1 << endl;
            } else {
                cout << 0 << endl;
            }
        }
    }
    return 0;
}