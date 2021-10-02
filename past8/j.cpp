#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int op(int a, int b) {
    return a + b;
}
int e(void) {
    return 0;
}

int main(void)
{
    int n, q;
    cin >> n >> q;
    
    segtree<int, op, e> seg(n + 1);
    for(int i = 0; i < q; i++) {
        int t, k;
        cin >> t >> k;
        
        if(t == 1) {
            int r = k > n ? k - n : n - k + 1;
            auto x = seg.prod(r, n + 1);
            if(x % 2 == 0) {
                cout << k << endl;
            } else {
                cout << (2 * n - k + 1) << endl;
            }
        } else {
            seg.set(k, seg.get(k) + 1);
        }
    }

    return 0;
}