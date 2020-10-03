#include <bits/stdc++.h>
#include <atcoder/math.hpp>

using namespace std;
using namespace atcoder;

int main(void)
{
    int tt;
    cin >> tt;
    for(int t = 0; t < tt; t++) {
        int n, m, a, b;
        cin >> n >> m >> a >> b;

        long long ans = floor_sum(n, m, a, b);
        cout << ans << endl;
    }
    return 0;
}