#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int i;
    int h, w;
    cin >> h >> w;

    vector<string> ss(h), tt(h);

    for(i = 0; i < h; i++) {
        string s;
        cin >> s;
        ss[i] = s + s;
    }
    for(i = 0; i < h; i++) {
        cin >> tt[i];
    }
    
    size_t p = 0;
    while(true) {
        p = ss[0].find(tt[0], p);
        if(p == string::npos) {
            cout << "No" << endl;
            return 0;
        }

        bool f = true;
        for(i = 1; i < h; i++) {
            if(ss[i].find(tt[i], p) != p) {
                f = false;
                break;
            }
        }
        if(f) {
            cout << "Yes" << endl;
            return 0;
        }

        p++;
    }

    cout << "???" << endl;
    return 0;
}