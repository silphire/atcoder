#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int e(void) {
    return -1;
}

int op(int a, int b) {
    return max(a, b);
}

int vv;
bool f(int v) {
    return v < vv;
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

    segtree<int, op, e> st(a);

    for(i = 0; i < q; i++) {
        int t;
        cin >> t;
        switch(t) {
        case 1:
            {
                int x, v;
                cin >> x >> v;
                st.set(x - 1, v);
            }
            break;
        case 2:
            {
                int l, r;
                cin >> l >> r;
                cout << st.prod(l - 1, r) << endl;
            }
            break;
        case 3:
            {
                int x, v;
                cin >> x >> v;
                vv = v;
                cout << (st.max_right<f>(x - 1) + 1) << endl;
            }
            break;
        }
    }

    return 0;
}