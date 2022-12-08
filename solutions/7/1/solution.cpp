#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>
#include <numeric>
#include <functional>

const std::string RESET = "$ cd /";
const std::string LS = "$ ls";

struct File {
    int size;
    std::string name;
};

struct Folder {
    std::vector<Folder> folders;
    std::vector<File> files;
    std::string name;
    std::string parent;
    Folder * parentDir = nullptr;
};



int find_directory_sizes(Folder * start, std::vector<File> & results, std::string path) 
{
    std::cout << "searching folder " << path << "\n";
    int size = 0;
    size += std::accumulate(start->files.begin(), start->files.end(), 0, [](int val, auto f){return val + f.size;});
    size += std::accumulate(start->folders.begin(), start->folders.end(), 0, [&](int val, Folder & f){return val + find_directory_sizes(&f, results, path + f.name + "/");});
    results.push_back({size, path} );
    return size;
}

int main() 
{

    Folder root;
    root.name = "/";
    std::string cd = "/";
    Folder * cwd = &root;

    // std::ifstream infile("test.txt");
    std::ifstream infile("input.txt");

    std::string line;
    std::smatch matches;

    while (std::getline(infile, line))
    {
        // std::cout << "line =" << line << "\n";
        if (line == RESET) {
            std::cout << "reset\n";
            cd = "/";
        }
        else if (line == LS) {
    
        }
        else if (std::regex_search(line, matches, std::regex(R"(dir (.+))"))) {
            auto dir = matches[1];
            std::cout << "dir: " << dir << "\n";
            Folder f;
            f.name = dir;
            f.parentDir = cwd;
            cwd->folders.push_back(f);
        }
        else if (std::regex_search(line, matches, std::regex(R"(\$ cd (.+))"))) {
            auto dir = matches[1];
            std::cout << "cd: " << dir << "\n";
            if (dir == "..") {
                cwd = cwd->parentDir;
            }
            else {
                auto res = std::find_if(cwd->folders.begin(), cwd->folders.end(), [&](auto element) {return element.name == dir; });
                if (res != cwd->folders.end()) {
                    cwd = &(*res);
                }
            }
        }
        // extract numbers
        else if (std::regex_search(line, matches, std::regex(R"((\d+) (.+))"))) {
            File f;
            f.name = matches[2];
            f.size = stoi(matches[1]);
            cwd->files.push_back(f);

            std::cout << f.name << " = " << f.size << "\n";

        }
    }
    

    std::vector<File> results;
    const int size = find_directory_sizes(&root, results, "/");
    for (auto f : results) {
        std::cout << f.name << " = " << f.size << "\n";
    }
    
    // part 1
    int xx = std::accumulate(results.begin(), results.end(), 0, [](int val, auto f){return val + (f.size <= 100000 ? f.size : 0);});
    std::cout << "size = " << xx << "\n";

    // part 2
    const int unusedSpace = 70000000 - size;
    const int spaceToFree = 30000000 - unusedSpace;
    std::cout << "spaceToFree = " << spaceToFree << "\n";

    // sorted
    std::sort(results.begin(), results.end(), [](auto a, auto b) {return a.size < b.size;});
    for (auto f : results) {
        std::cout << f.name << " = " << f.size << "\n";
    }

    // if we were looking for an actual value we could binary search?
    for (int i = 1; i < results.size(); i++ ) {
        
        if (results[i].size > spaceToFree) {
            // const int beforeSize = spaceToFree - results[i-1].size;
            // const int afterSize = results[i].size - spaceToFree;
            std::cout << "results is : " << results[i].name << " ~ " << results[i].size << "\n";
            break;
        }
    }
}