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

std::vector<Node *> nodes;
std::map<std::string, int> travelcostMap;
std::map<std::string, int64_t> flagForNode; //bits
std::map<uint64_t, uint32_t> cache;
std::vector<int32_t> results;

std::vector<Node *> removeUselessPaths(std::vector<Node *> nodes)
{

    for (Node * node : nodes)
    {
        
        if (node->flowRate == 0 and node->name != "AA")
        {
            continue;
        }
        
        std::vector<std::string> connetorsCopy = node->toConnect;
        // need to copy as we will delete from the original
        for (auto key : connetorsCopy ) {
            if (node->paths[key]->flowRate == 0 && key != "AA") {
                std::vector<std::string> visited;
                visited.push_back(node->name);
                std::cout << "Startig at: " << node->name <<  "\n";

                Node * temp = node->paths[key];
                visited.push_back(key);
                
                int travelCost = 1;
                if (temp->flowRate == 0) {
                    std::cout << "\tIterating on " << temp->name <<  "\n";
                }
                while (temp->flowRate == 0 && temp->name != "AA") {
                    travelCost += 1;
                    for (auto key : temp->toConnect ) {
                        if (auto res = std::find(visited.begin(), visited.end(), key); res == visited.end()) {
                            temp = temp->paths[key];
                            visited.push_back(key);
                            std::cout << "\tvisited: " << key << "\n";
                            break;
                        }
                        visited.push_back(key);
                    }
                }
                
                std::cout << node->name << " -> " << key << " skip to " << temp->name << "\n";
                // remove key from head
                node->toConnect.erase(std::remove(node->toConnect.begin(), node->toConnect.end(), key), node->toConnect.end());
                node->toConnect.push_back(temp->name);
                
                node->paths.erase(key);
                node->paths[temp->name] = temp;
                
                travelcostMap[node->name + temp->name] = travelCost;
                travelcostMap[temp->name + node->name] = travelCost;
                
            }
        }
    }
    
    std::vector<Node *> toKeep;
    
    for (Node * node : nodes)
    {
        if (node->flowRate == 0 and node->name != "AA") {
            delete node;
        }
        else {
            toKeep.push_back(node);
        }
    }
    
    for (Node * node : toKeep) {
        std::cout << node->name << "\n";
        for (auto p : node->toConnect) {
            std::cout << "\t" << p << "\n";
        }
    }
    return toKeep;
}

const int TIME = 26;

int getPressure(Node * node, int time, int pressure, int players)
{
    uint64_t valves = 0ULL;
    
    for (Node * n : nodes) {
        if (n->open) {
            valves |= flagForNode[n->name];
        }
    }
    
    if (time < 0) {
        return 0;
    }
    else if (time == 0) {
        results.push_back( (pressure << 16) + (int32_t) valves);
        return pressure;// + (players ? getPressure(nodes[0], TIME, 0, players-1) : 0);
    }
    

    
    //first 15 bits are open vales time is 5 bits, 2^5 , pressure = 12 bits  nodes = 15 bits
#if 1
    uint64_t p = (((uint64_t) pressure) << 16ULL); // 12 bits
    uint64_t t = (((uint64_t) time) << 28ULL); // 5 bits
    uint64_t u = (((uint64_t) flagForNode[node->name]) << 34ULL); //upper 16 bits
    uint64_t e = (((uint64_t) players) << 50ULL); //upper 5 bits
    assert(p > 65536 || p == 0);
    assert(t > 65536 || t == 0);
    assert(u > 65536 || u == 0);
    assert(valves < 65536);

    const uint64_t key = valves | p | t | u | e;
    if (cache.find(key) != cache.end()) {
        return cache[key];
    }
#else
//    uint64_t p = (((uint64_t) pressure) << 16ULL); // 12 bits
    uint64_t t = (((uint64_t) time) << 16ULL); // 5 bits
    uint64_t e = (((uint64_t) players) << 21ULL); //upper 5 bits
    
    int i = 0;
    for (Node * n : nodes) {
        if (n == node) {
            break;
        }
        i++;
    }
    uint64_t u = (((uint64_t) i) << 23ULL); //upper 4 bits
    
//    assert(p > 65536 || p == 0);
//    assert(t > 65536 || t == 0);
//    assert(u > 65536 || u == 0);
//    assert(valves < 65536);

    const uint64_t key = valves | u | t;// | e;
    if (cache.find(key) != cache.end()) {
        return cache[key];
    }
    
    
#endif
    
    
    int max = 0;
    
    // either we open a valve
    if (!node->open && node->flowRate > 0) {
        node->open = true;
        max = std::max(max, getPressure(node, time-1, pressure + (node->flowRate * (time-1) ), players));
        node->open = false;
    }
    
    // or move on
    for (auto name : node->toConnect) {
        Node * newNode = node->paths[name];
        const int tc = travelcostMap[node->name + newNode->name];
        assert(tc != 0);
        max = std::max(max, getPressure(newNode, time - tc, pressure, players));
    }
    
    cache[key] = max;

    return max;
}


int main()
{


    // std::ifstream infile("test.txt");
    std::ifstream infile("/Users/hackerman/Documents/code/advent-of-code-2022/solutions/16/1/input.txt");
//    std::ifstream infile("/Users/hackerman/Documents/code/advent-of-code-2022/solutions/16/1/test.txt");

    std::string line;
    std::smatch matches;

    while (std::getline(infile, line))
    {
        std::cout << line << "\n";
        if (std::regex_search(line, matches, std::regex(R"(Valve (\w\w) has flow rate=(\d*); tunnel?s? leads? to valves? (.*))"))) {
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
            
            std::string path = node->name + k;
            travelcostMap[path] = 1;
        }
    }

    // this actually takes the remaining pointers also
    nodes = removeUselessPaths(nodes);
    
    int flag = 0;
    int c = 0;
    for (auto * n : nodes) {
//        std::cout << n->travelCost << "\n";
        flagForNode[n->name] = 1 << c;
        c++; //hehe
        
    }
    
    // deletes null nodes
    for (auto * node : nodes) {
        std::vector<std::string> newConnectors;
        for (int i = 0; i < node->toConnect.size(); i++) {

            if (flagForNode.find(node->toConnect[i]) != flagForNode.end()) { //not found
                newConnectors.push_back(node->toConnect[i]);
            }
        }
        node->toConnect = newConnectors;
        for (auto k : node->toConnect ) {
            std::cout << node->name << " ~ " << k << "\n";
        }
        std::cout << "\n";
    }
//    for (int i = 5; i <= 30; i++)
    {
    
        int i = TIME;
        for (auto * n : nodes) {
            n->open = false;
        }
        int pressure = getPressure(nodes[10], i, 0, 0);
        std::cout << i << " ~ " << pressure << "\n";
    }
    
    struct Res {
        int32_t valves;
        int32_t result;
    };
    
    std::vector<Res> fitlerd;
    
    for (auto i : results) {
        fitlerd.push_back({ i & 0xFFFF , i >> 16});
//        std::cout << i << "\n";
    }
    
    std::sort(fitlerd.begin(), fitlerd.end(), [](const Res& lhs, const Res& rhs) {
       return lhs.result < rhs.result;
    });
    
    for (auto r : fitlerd) {
//        std::cout << r.result << " ~ " << r.valves << "\n";
    }
    std::reverse(fitlerd.begin(), fitlerd.end());
    
    uint32_t a = fitlerd[0].valves;
    std::cout << fitlerd[0].result << "\n";
    
    
    for (int i = 1; i < fitlerd.size(); i++) {
        if ((a ^ fitlerd[i].valves) == (a | fitlerd[i].valves) ) {
//            std::cout << " ~ " << fitlerd[i].result << "\n";
            break;
        }
    }
    
    int max = 0;
    for (int i = 0; i < fitlerd.size(); i++) {
        
        for (int j = i; j < fitlerd.size(); j++) {
            if (i != j) {
                
                if ((fitlerd[j].valves ^ fitlerd[i].valves) == (fitlerd[j].valves | fitlerd[i].valves) )
                {
                    int b = max;
                    max = std::max(max, fitlerd[i].result + fitlerd[j].result);
                    if (max != b) {
                        std::cout << max << "\n";
                    }
                }

            }
            
        }
        
    }
    std::cout << "max is " << max << "\n";
    return 0;
}

/*
 
 Get the results and sort them
 extract the valve pattern
 
 */


