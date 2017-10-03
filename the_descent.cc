#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * The Descent
 * https://www.codingame.com/ide/puzzle/the-descent
 **/
int main()
{
    int prevHeight = 0;
    int index = 0;
    // game loop
    while (1) {
        for (int i = 0; i < 8; i++) {
            int mountainH; // represents the height of one mountain.
            cin >> mountainH; cin.ignore();
            if (prevHeight < mountainH) {
                index = i;
                prevHeight = mountainH;
            }
            
        }

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        prevHeight = 0;
        cout << index << endl; // The index of the mountain to fire on.
    }
}