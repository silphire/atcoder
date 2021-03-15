#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;
using mint = modint998244353;

int main(void)
{
    int n;
    cin >> n;

    dsu g(n);
    int i;
    for(i = 0; i < n; i++) {
        int f;
        cin >> f;
        g.merge(i, f - 1);
    }
    mint ans = mint(2).pow(g.groups().size()) - 1;
    cout << ans.val() << endl;

    return 0;
}