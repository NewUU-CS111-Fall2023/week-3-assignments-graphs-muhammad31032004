#include <iostream>
#include <string>
using namespace std;
int a[100][100];
int m[100], k;

int get(int i, bool b){
    int ans = 0;
    for (int j = 0; j < m[i]; j ++) {
        ans = max(ans, get(a[i][j], b || k == i));
    }
    
    return ans + 1 + b;
}

int main()
{
  int n, x, y;
  cin >> n >> k;
  for (int i = 0; i < n - 1; i ++) {
      cin >> x >> y;
      a[x][m[x]] = y;
      m[x] ++;
  }
  cout << get(1, false);
}