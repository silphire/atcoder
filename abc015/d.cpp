#include <bits/stdc++.h>

using namespace std;

int aa[50], bb[50];
int dp[51][10001][51];

int main(void)
{
    int i, j, kk;
    int w;
    cin >> w;
    int n, k;
    cin >> n >> k;
    for(i = 0; i < n; i++) {
        cin >> aa[i] >> bb[i];
    }

    for(i = 0; i < n; i++) {
        int a = aa[i];
        int b = bb[i];
        for(j = 0; j <= w; j++) {
            for(kk = 0; kk <= k; kk++) {
                dp[i + 1][j][kk] = max(
                    dp[i + 1][j][kk],
                    dp[i][j][kk]
                );
                if(j + a <= w) {
                    dp[i + 1][j + a][kk + 1] = max(
                        dp[i + 1][j + a][kk + 1],
                        dp[i][j][kk] + b
                    );
                }
            }
        }
    }

    cout << dp[n][w][k] << endl;
    return 0;
}