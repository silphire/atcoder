#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int main(void)
{
    int i, x, y;

    int n, m;
    cin >> n >> m;
    int source = n * m;
    int sink = n * m + 1;

    vector<string> s(n);
    for(i = 0; i < n; i++) {
        cin >> s[i];
    }

    mf_graph<int> g(n * m + 2);
    for(y = 0; y < n; ++y) {
        for(x = 0; x < m; ++x) {
            if(s[y][x] == '#')
                continue;
            if((x + y) % 2 == 0) {
                g.add_edge(source, y * m + x, 1);

                for(i = 0; i < 4; ++i) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx < 0 || nx >= m || ny < 0 || ny >= n || s[ny][nx] == '#')
                        continue;
                    g.add_edge(y * m + x, ny * m + nx, 1);
                }
            } else {
                g.add_edge(y * m + x, sink, 1);
            }
        }
    }

    cout << g.flow(source, sink) << endl;
    for(const auto &e : g.edges()) {
        if(e.flow == 1 && e.from != source && e.to != sink) {
            int x1 = e.from % m;
            int y1 = e.from / m;
            int x2 = e.to % m;
            int y2 = e.to / m;

            if(x1 == x2) {
                s[min(y1, y2)][x1] = 'v';
                s[max(y1, y2)][x1] = '^';
            } else {
                s[y1][min(x1, x2)] = '>';
                s[y1][max(x1, x2)] = '<';
            }
        }
    }
    
    for(const auto &ss : s) {
        cout << ss << endl;
    }

    return 0;
}