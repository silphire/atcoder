#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int op(int x, int y) {
    return x ^ y;
}

int e(void) {
    return 0;
}

int main(void)
{
    int i;
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for(i = 0; i < n; i++) {
        cin >> a[i];
    }
    segtree<int, op, e> seg(a);

    for(i = 0; i < q; i++) {
        int t, x, y;
        cin >> t >> x >> y;
        x--;

        if(t == 1) {
            seg.set(x, seg.get(x) ^ y);
        } else {
            cout << seg.prod(x, y) << endl;
        }
    }

    return 0;
}