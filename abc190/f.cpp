#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(void)
{
    long long n;
    cin >> n;
    vector<long long> a(n, 0);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    fenwick_tree<long long> fw(n);
    long long ans = 0;
    for(int i = 0; i < n; i++) {
        ans += i - fw.sum(0, a[i]);
        fw.add(a[i], 1);
    }
    for(int i = 0; i < n; i++) {
        cout << ans << endl;
        ans += n - 1 - a[i] * 2;
    }

    return 0;
}