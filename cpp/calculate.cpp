#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int ret = add(1, 2);
    int ret_2 =  add(1, 2);
    int ret_3 = ret + ret_2;
    std::cout << ret << ret_2 << ret_3 << std::endl;
    for (int i = 0; i < 10; i++) {
        std::cout << i << std::endl;
    }

    int a = 0;
    for (int i = 0; i < 10; i++) {
        a += i;
    }
    std::cout << "result" << a << std::endl;

    return 0;
}
