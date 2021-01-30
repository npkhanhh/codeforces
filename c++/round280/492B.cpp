#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int n, l;
  cin >> n >> l;
  vector<int> a(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  sort(a.begin(), a.end());
  a.insert(a.begin(), 0);
  a.push_back(l);
  double result = 0;
  for (int i = 1; i< n+2; ++i) {
    if ((i == 1 || i == n+1) && a[i] - a[i-1] > result){
      result = a[i] - a[i-1];
    }
    else if (float(a[i] - a[i-1]) / 2.0 > result) {
      result = float(a[i] - a[i-1]) / 2.0;
    }
  }
  cout.precision(17);
  cout << fixed << result;
  return 0;
}

