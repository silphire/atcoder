#include <bits/stdc++.h>

using namespace std;

struct obj {
    int w, h, kind;
    obj() {}
    obj(int w_, int h_, int kind_) {
        w = w_;
        h = h_;
        kind = kind_;
    }
    bool operator<(const obj& t) const {
        if(h == t.h) return kind > t.kind;
        return h > t.h;
    }
    bool operator==(const obj& t) const {
        return h == t.h && w == t.w && kind == t.kind;
    }
};

int main(void) {
    int i;
    
    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(n), c(m), d(m);
    for(i = 0; i < n; i++) cin >> a[i];
    for(i = 0; i < n; i++) cin >> b[i];
    for(i = 0; i < m; i++) cin >> c[i];
    for(i = 0; i < m; i++) cin >> d[i];

    vector<obj> objs(m + n);
    for(i = 0; i < n; i++) objs[i] = obj(b[i], a[i], 0);
    for(i = 0; i < m; i++) objs[n + i] = obj(d[i], c[i], 1);
    sort(objs.begin(), objs.end());

    multiset<int> s;
    for(auto it : objs) {
        if(it.kind == 1) {
            s.insert(it.w);
        } else {
            auto jt = s.lower_bound(it.w);
            if(jt == s.end()) {
                cout << "No" << endl;
                return 0;
            }
            s.erase(jt);
        }
    }

    cout << "Yes" << endl;
    return 0;
}