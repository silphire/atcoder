#include <bits/stdc++.h>
using namespace std;

int n;
vector<string> s;
string ans;

bool dfs(int a, int b, int c, int i) {
    if(i == n) {
        return true;
    }
    if(s[i] == "AB") {
        if(a > 0) {
            if(dfs(a - 1, b + 1, c, i + 1)) {
                ans = "B" + ans;
                return true;
            }
        }
        if(b > 0) {
            if(dfs(a + 1, b - 1, c, i + 1)) {
                ans = "A" + ans;
                return true;
            }
        }
    } else if(s[i] == "BC") {
        if(b > 0) {
            if(dfs(a, b - 1, c + 1, i + 1)) {
                ans = "C" + ans;
                return true;
            }
        }
        if(c > 0) {
            if(dfs(a, b + 1, c - 1, i + 1)) {
                ans = "B" + ans;
                return true;
            }
        }
    } else {
        if(a > 0) {
            if(dfs(a - 1, b, c + 1, i + 1)) {
                ans = "C" + ans;
                return true;
            }
        }
        if(c > 0) {
            if(dfs(a + 1, b, c - 1, i + 1)) {
                ans = "A" + ans;
                return true;
            }
        }
    }

    return false;
}

int main(void) {
    int a, b, c;
    cin >> n;
    cin >> a;
    cin >> b;
    cin >> c;

    s = vector<string>(n);
    for(int i = 0; i < n; i++) {
        cin >> s[i];
    }

    bool f = dfs(a, b, c, 0);
    if(f) {
        cout << "Yes" << endl;
        for(int i = 0; i < ans.length(); i++) {
            cout << ans[i] << endl;
        }
    } else {
        cout << "No" << endl;
    }

    return 0;
}