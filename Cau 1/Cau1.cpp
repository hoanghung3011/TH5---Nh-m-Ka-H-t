#include <iostream>

#include <cstring>

#include <fstream>

using namespace std;
int n, a[10][10], colorCount = 0, color[10];
void readFile() {
  int q, p;
  ifstream graph("graph.txt");
  if (graph.is_open()) {
    graph >> n;
    while (!graph.eof()) {
      graph >> q;
      graph >> p;
      a[q][p] = 1;
      a[p][q] = 1;
    }
    graph.close();
  } else
    cout << "Can not open the file";
}

void graphColoring() {
  int test;
  for (int i = 1; i <= n; i++)
    if (!color[i]) {
      colorCount++;
      color[i] = colorCount;
      for (int j = i + 1; j <= n; j++)
        if ((a[i][j] == 0) && (color[j] == 0)) {
          test = 1;
          for (int k = i + 1; k < j; k++)
            if ((a[k][j] == 1) && (color[i] == color[k])) {
              test = 0;
              break;
            }
          if (test == 1) color[j] = colorCount;
        }
    }
}
void print() {
  for (int i = 1; i <= colorCount; i++) {
    cout << "Color " << i << ": ";
    for (int j = 1; j <= n; j++)
      if (color[j] == i) cout << j << " ";
    cout << endl;
  }
}
int main() {
  readFile();
  cout << n << endl;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) cout << a[i][j] << "  ";
    cout << endl;
  }
  cout << endl;
  graphColoring();
  print();
  return 0;
}
