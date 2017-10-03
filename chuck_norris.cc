#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

/**
 * Chuck Norris
 * https://www.codingame.com/ide/puzzle/chuck-norris
 **/
int main()
{
    string MESSAGE;
    getline(cin, MESSAGE);
    bitset<7> letters [ MESSAGE.length() ];
    string encode;
    string characters;
    
    for (int i = 0; i < MESSAGE.length();i++) {
        bitset<7> bits(MESSAGE[i]);
        characters += bits.to_string(); 
    }
    
    for (int j = 0; j < characters.length(); j++) {
        if (characters[j] == '1') {
            if (j == 0) {
                encode += "0 0";
            } else {
                if (characters[j - 1] == '1') {
                    encode += "0";
                } else {
                    encode += " 0 0";
                }
            }
        } else {
            if (j == 0) {
                encode += "00 0";
            } else {
                if (characters[j - 1] == '0') {
                  encode += "0"; 
                } else {
                    encode += " 00 0";
                }
            }
        }
    }
    
    // Write an action using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    cout << encode << endl;
}