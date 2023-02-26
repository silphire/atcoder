#include <bits/stdc++.h>

using namespace std;

const int N = 200001;
const int MOD = 998244353;
int dp[N][2];    // 枚目、表裏

int main(void) {
    int i, n;
    cin >> n;
    vector<int> aa(n), bb(n);
    for(i = 0; i < n; i++) {
        cin >> aa[i] >> bb[i];
    }

    dp[0][0] = 1;
    dp[0][1] = 1;
    for(i = 1; i < n; i++) {
        if(aa[i - 1] != aa[i]) {
            dp[i][0] += dp[i - 1][0];
            dp[i][0] %= MOD;
        }
        if(bb[i - 1] != aa[i]) {
            dp[i][0] += dp[i - 1][1];
            dp[i][0] %= MOD;
        }
        if(aa[i - 1] != bb[i]) {
            dp[i][1] += dp[i - 1][0];
            dp[i][1] %= MOD;
        }
        if(bb[i - 1] != bb[i]) {
            dp[i][1] += dp[i - 1][1];
            dp[i][1] %= MOD;
        }
    }

    int ans = dp[n - 1][0] + dp[n - 1][1];
    cout << (ans % MOD) << endl;
    return 0;
}