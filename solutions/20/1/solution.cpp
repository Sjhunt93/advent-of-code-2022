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
#include <queue>

struct Node {
    Node * prev{nullptr};
    Node * next{nullptr};
    int64_t value{0};
    int position{-1};

    static void moveNode(Node * nodeStart, const int64_t size)
    {
        const bool isStart = nodeStart->position == 0;
        int64_t toMove = nodeStart->value % (size-1);
        if (toMove == 0) {
            return;
        }
        std::cout << "Moving by " << toMove << " places. " << nodeStart->value << "\n";

        Node * node = nodeStart;
        while(toMove != 0) {
            // std::cout << toMove << "\n";
            if (toMove < 0) {
                node = node->prev;
                toMove++;
            }
            else {
                node = node->next;
                toMove--;
            }
            
        }

        if (isStart) {
            nodeStart->position = -1;
            nodeStart->next->position = 0;
        }

        // [---]x [-pop-] x[---] 
        nodeStart->prev->next = nodeStart->next;
        nodeStart->next->prev = nodeStart->prev;


        // std::cout << nodeStart->prev->value << " ~~ " << nodeStart->next->value << "\n";
        // std::cout << node->value << "\n";
        // if (nodeStart->value < 0) 
        // std::cout << "Inserting after " << node->value << " with " << nodeStart->value << "\n"; 

        // std::cout << node->prev->value << " -- " << node->value << " -- " << node->next->value << "\n";

        if (nodeStart->value > 0) {

            node->next->prev = nodeStart; // link back
            nodeStart->next = node->next; //next is current next
            nodeStart->prev = node;
            node->next = nodeStart;
        }
        else {
            node->prev->next = nodeStart; // link back
            nodeStart->next = node; //next is current next
            nodeStart->prev = node->prev;
            node->prev = nodeStart;
        }

        // std::cout << nodeStart->prev->value << " -- " << nodeStart->value << " -- " << nodeStart->next->value << "\n";
        // nodeStart->prev = node;
        // node->next = nodeStart;
        // nodeStart->next->prev = 

            // node->prev->next = nodeStart;
            // nodeStart->next = node->next;
            // node->next->prev = nodeStart;
            // nodeStart->prev = node->prev;
        // }
        // else {
        // std::cout << nodeStart->prev->value << " -- " << nodeStart->value << " -- " << nodeStart->next->value << "\n";
        // }
    }
};






int main() 
{


    // std::ifstream infile("test.txt");
    std::ifstream infile("input.txt");

    // 
    // std::smatch matches;
    std::string line;
    std::vector<Node> nodes;
    std::vector<int64_t> original;
    std::queue<int64_t> toprocess;
    while (std::getline(infile, line))
    {
        std::cout << line << "\n";
        int64_t num = std::stoi(line);
        num *= 811589153;
        std::cout << num << "\n";
        original.push_back(num);
        toprocess.push(num);
    }
    
    std::vector<Node *> orders;
    
    Node * current = new Node();
    current->value = toprocess.front(); toprocess.pop();
    Node * start = current;
    start->position = 0;
    orders.push_back(current);

    while (!toprocess.empty())
    {
        std::cout << "Starting: " << toprocess.size() << "\n";
        int64_t a = toprocess.front(); toprocess.pop();

        // Node * old = current; // temp reference to old
        Node * newnode = new Node();

        newnode->prev = current;
        current->next = newnode;
        newnode->value = a;
        orders.push_back(newnode);
        current = newnode;

        std::cout << a << "\n";
    }
    // connect last dots

    current->next = start;
    start->prev = current;

    Node * debug = start;

    std::cout << "\n\n";
    for (int rounds = 0; rounds < 10; rounds++ ) {
    for (auto a : orders) {
        // std::cout << a->value << "\n";
        Node::moveNode(a, orders.size());
        
        while (debug->position != 0)
        {
            debug = debug->next;
        }
        // debug = debug->prev;

        int i = orders.size();
        int score = 0;
        while (i)
        {
            
            // std::cout << debug->value << ", ";
            debug = debug->next;
            i--;
            
        }
        // std::cout <<"\n";
    
    }
    }

    while (debug->value != 0)
    {
        debug = debug->next;
    }
    std::cout << debug->value << "\n";
    int64_t score = 0;

    for (int j = 0; j < 3; j++) {
        for (int i = 0; i < 1000; i++)
        {
            debug = debug->next;
        }
        std::cout << "value: " << debug->value << "\n";
        score += debug->value;
    }
    
    std::cout << "score is " << score << "\n";


    // current = start;
    // while (current != nullptr)
    // {
    //     Node::moveNode(current, orders.size());
    //     std::cout << " ~ " << current->value << "\n";
    //     current = current->next;
        
    // }

    
    
}