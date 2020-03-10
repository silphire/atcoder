#include <bits/stdc++.h>

using namespace std;

const int INF = 100000000;
int dp[20000];

int main(void) {
    dp[0] = 0;
    for(int i = 1; i < 20000; i++) {
        dp[i] = INF;
    }

    int h, n;
    cin >> h >> n;

    int amax = 0;
    for(int j = 0; j < n; ++j) {
        int a, b;
        cin >> a >> b;
        amax = max(amax, a);

        for(int i = 0; i <= h; i++) {
            dp[i + a] = min(dp[i + a], dp[i] + b);
        }
    }

    int ans = INF;
    for(int i = h; i <= h + amax; i++) {
        ans = min(ans, dp[i]);
    }
    cout << ans << endl;
}