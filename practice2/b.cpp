#include <bits/stdc++.h>
#include <atcoder/fenwicktree.hpp>

using namespace std;

int main(void)
{
    int n, q;
    cin >> n >> q;

    atcoder::fenwick_tree<long long> fw(n);
    for(int i = 0; i < n; i++) {
        int a;
        cin >> a;
        fw.add(i, a);
    }

    for(int i = 0; i < q; i++) {
        int qq, x, y;
        cin >> qq >> x >> y;
        if(qq == 0) {
            fw.add(x, y);
        } else {
            cout << fw.sum(x, y) << endl;
        }
    }

    return 0;
}