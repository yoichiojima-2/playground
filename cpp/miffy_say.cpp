#include <iostream>
#include <string>


int miffy_say(std::string msg) {
    std::cout << " () () " << std::endl;
    std::cout << "( OvO ) < " << msg << std::endl;
    return 0;
};

int main() {
    miffy_say("Hello, World!");
    return 0;
};
