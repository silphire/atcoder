#include <bits/stdc++.h>

using namespace std;

int n, x, y;
map<int, vector<int>> g;
list<int> q;

void dfs(int v, int p) {
    if(v == y) {
        bool f = false;
        for(auto x : q) {
            if(f) {
                cout << " ";
            } else {
                f = true;
            }
            cout << x;
        }
        cout << endl;
        exit(0);
    }
    for(auto u : g[v]) {
        if(u == p) {
            continue;
        }
        q.push_back(u);
        dfs(u, v);
        q.pop_back();
    }
}

int main(void) {
    cin >> n >> x >> y;

    for(int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    q.push_back(x);
    dfs(x, -1);
    return 0;
}