#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>
#include <numeric>
#include <functional>
#include <set>
#include <map>
#include <queue>

struct Node {
    std::string name;
    std::vector<std::string> toConnect;
    std::map<std::string, Node *> paths;
    int flowRate{0};
    bool open{false};
    int travelCost{1};
};



int getFlowRate(std::vector<Node> &nodes)
{
    int sum = 0;
    for (auto n : nodes) {
        if (n.open) {
            sum += n.flowRate;
        }
    }
    return sum;

}




void removeUselessPaths(std::vector<Node *> nodes)
{
    // std::vector<std::string> visited;

    // visited.push_back(nodes[0]->name);
    // std::list<Node *> nodes;

    for (Node * node : nodes)
    {
        
        if (node->flowRate == 0)
        {
            continue;
        }
        
        
        for (auto key : node->toConnect ) {
            if (node->paths[key]->flowRate == 0) {
                std::vector<std::string> visited;
                visited.push_back(node->name);
                std::cout << node->name <<  " get\n";

                // std::string startedAt = node->name;
                Node * temp = node->paths[key];
                while (temp->flowRate == 0) {
                    for (auto key : temp->toConnect ) {
                        if (auto res = std::find(visited.begin(), visited.end(), key); res == visited.end()) {
                            temp = temp->paths[key];
                            std::cout << key <<  " Found\n";
                        }
                    }
                }
            }
        }

    }
    

}


// returns the next node to go to and how deep it is
std::tuple<Node *, int> getNext(Node * starts, std::vector<Node> & nodes, int depth=1) 
{
    for (auto key : starts->toConnect) {
        Node * next = nullptr;
        int max = 0;
        std::vector<Node *> layerBellow;
        for (int i = 0; i < nodes.size(); i++) //iterate over list to find
        {
            if (nodes[i].name == key)
            {
                if (nodes[i].flowRate > max) {
                    next = &nodes[i];
                    max = nodes[i].flowRate;
                }
                layerBellow.push_back(&nodes[i]);
            }
            
        }
        // if (next == nullptr) {
        //     int max = 0
        // }
        return {next, depth};
    }
}

int main() 
{


    // std::ifstream infile("test.txt");
    std::ifstream infile("test.txt");

    std::string line;
    std::smatch matches;

    std::vector<Node *> nodes;
    while (std::getline(infile, line))
    {
        std::cout << line << "\n";
        if (std::regex_search(line, matches, std::regex(R"(Valve (\w\w) has flow rate=(\d*); tunnels lead to valves (.*))"))) {
            auto valveName = matches[1];
            auto flowRate = matches[2];
            std::string rm = matches[3];

            std::smatch match2;
            std::regex r(R"(\w\w)");
            Node * node = new Node();
            node->flowRate = std::stoi(flowRate);
            node->name = valveName;

            while (std::regex_search(rm, match2, r)) {
                node->toConnect.push_back(match2.str(0));
                std::cout << "Matched string is " << match2.str(0) << std::endl;
                rm = match2.suffix().str();
            }
            nodes.push_back(node);
        }  
    }
    
    for (auto * node : nodes)
    {
        // create connections
        for (auto k : node->toConnect ) {
            // ughhhh c++ deference the iterator to get the reference and then get the addres
            auto res = * std::find_if(nodes.begin(), nodes.end(), [&](Node * a) {return a->name == k;});
            node->paths[k] = res;

            // auto ptr = &(*res);
        }
        
        
    }

    removeUselessPaths(nodes);
    
   

       
}