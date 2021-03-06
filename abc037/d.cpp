#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;
using mint = modint1000000007;

int w, h;
int a[1000][1000];
int dp[1000][1000];

const int dx[] = { -1, 1, 0, 0 };
const int dy[] = { 0, 0, -1, 1 };

mint dfs(int x, int y, int prev)
{
    if(!(x >= 0 && x < w && y >= 0 && y < h)) {
        return 0;
    }
    if(a[y][x] <= prev) {
        return 0;
    }
    if(dp[y][x] > 0) {
        return dp[y][x];
    }

    mint ans = 1;
    int i;
    for(i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        ans += dfs(nx, ny, a[y][x]);
    }

    dp[y][x] = ans.val();
    return ans;
}

int main(void)
{
    int x, y;

    cin >> h >> w;
    for(y = 0; y < h; y++) {
        for(x = 0; x < w; x++) {
            cin >> a[y][x];
        }
    }

    mint ans = 0;
    for(y = 0; y < h; y++) {
        for(x = 0; x < w; x++) {
            ans += dfs(x, y, 0);
        }
    }
    cout << ans.val() << endl;
    return 0;
}
