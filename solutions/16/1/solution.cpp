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

struct Node {
    std::string name;
    std::vector<std::string> toConnect;
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

    std::vector<Node> nodes;
    while (std::getline(infile, line))
    {
        std::cout << line << "\n";
        if (std::regex_search(line, matches, std::regex(R"(Valve (\w\w) has flow rate=(\d*); tunnels lead to valves (.*))"))) {
            auto valveName = matches[1];
            auto flowRate = matches[2];
            std::string rm = matches[3];

            std::smatch match2;
            std::regex r(R"(\w\w)");
            Node node;
            node.flowRate = std::stoi(flowRate);
            node.name = valveName;

            while (std::regex_search(rm, match2, r)) {
                node.toConnect.push_back(match2.str(0));
                std::cout << "Matched string is " << match2.str(0) << std::endl;
                rm = match2.suffix().str();
            }
            nodes.push_back(node);
        }  
    }
    

    
    Node * current = &nodes[0];

    std::set<std::string> visited;
    int pressureReading = 0;
    for (int time = 30; time > 0; time--)
    {
        /* code */
        pressureReading += getFlowRate(nodes);

        if (! current->open && current->flowRate > 0)
        {
            current->open = true;
            std::cout << "Opening valve " << current->name << "\n";
        }
        else {
            int max = 0;
            Node * next = nullptr;
            for (auto key : current->toConnect) {
                for (int i = 0; i < nodes.size(); i++)
                {
                    if (nodes[i].name == key)
                    {
                        if (next == nullptr) { //fallback
                            next = &nodes[i];
                        }
                        if (nodes[i].flowRate > max) {
                            next = &nodes[i];
                            max = nodes[i].flowRate;
                        }
                    }
                    
                }
            }
            std::cout << "Moving from " << current->name << " <- " << next->name << "\n";
            current = next;
        }

        
        // std::string t = "AA";
        // if (visited.find(t) != visited.end()) {

        // }
        // visited.insert(t);

    }
    std::cout << "pressure: " << pressureReading << "\n";
    
    
}