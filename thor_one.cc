#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Power of Thor - Episode 1
 * https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
 **/
int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position
    cin >> lightX >> lightY >> initialTX >> initialTY; cin.ignore();

    // game loop
    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remainingTurns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        if (initialTX < lightX) {
            if (initialTY < lightY) {
                initialTY++;
                cout << "SE" << endl;
            } else if (initialTY > lightY) {
                initialTY--;
                cout << "NE" << endl;
            } else {
                initialTX++;
                cout << "E" << endl;
            }
        } else if (initialTX > lightX) {
            if (initialTY < lightY) {
                initialTY++;
                cout << "SW" << endl;
            } else if (initialTY > lightY) {
                initialTY--;
                cout << "NW" << endl;
            } else {
                initialTX--;
                cout << "W" << endl;
            }
        } else if (initialTY < lightY) {
            if (initialTX < lightX) {
                initialTX++;
                cout << "SE" << endl;
            } else if (initialTX > lightX) {
                initialTX--;
                cout << "SW" << endl;
            } else {
                initialTY++;
                cout << "S" << endl;
            }
        } else if (initialTY > lightY) {
            if (initialTX < lightX) {
                initialTX++;
                cout << "NE" << endl;
            } else if (initialTX > lightX) {
                initialTX--;
                cout << "NW" << endl;
            } else {
                initialTY--;
                cout << "N" << endl;
            }
        }
        // A single line providing the move to be made: N NE E SE S SW W or NW
    }
}