#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Node {
public:
  Node(char l, map<Node, int> con) : letter{l}, connections(con) {}
  void setLetter(char l) {letter = l;}
  void setConnections(map<Node, int> con) {connections = con;}
  char getLetter() {return letter;}
  map<Node, int> getConnections() {return connections;}
private:
  char letter;
  map<Node, int> connections;
};

int main () {
    map<Node, Node[]> graph;
    vector<Node> nodes;
    char letters[10] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    return 0;
}