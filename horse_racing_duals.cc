/**
* Horse-racing Duals
* https://www.codingame.com/ide/puzzle/horse-racing-duals
**/

int merge(vector<int>& h,int p,int q,int r) {
    vector<int> lowerHalf(q + 1 - p);
    vector<int> upperHalf(r - q);
    
    int k = 0;
    int j = 0;
    for (int i = p; i <= r; i++) {
        if (i <= q) {
            lowerHalf[k] = h[i];
            k++;
        } else {
            upperHalf[j] = h[i];
            j++;
        }
    }
    
    k = 0;
    j = 0;
    for (int i = p; i <= r; i++) {
        if ((int)(k) < (int)(lowerHalf.size()) && (int)(j) < (int)(upperHalf.size())) {
            if (lowerHalf[k] < upperHalf[j]) {
                h[i] = lowerHalf[k];
                k++;
            } else {
                h[i] = upperHalf[j];
                j++;
            }
        } else {
            if (k >= lowerHalf.size()) {
                h[i] = upperHalf[j];
                j++;
            } else {
                h[i] = lowerHalf[k];
                k++;
            }
        }
    }
}   
 
int divide(vector<int>& h, int p,int r) {
    if (p < r) {
        int q = floor((p + r) / 2);
        divide(h,p,q);
        divide(h,q+1,r);
        merge(h,p,q,r);
    }
}

int main()
{
    int N;
    int lowest = 10000000;
    cin >> N; cin.ignore();
    vector<int> h(N); 
    
    for (int i = 0; i < N; i++) {
        int Pi;
        cin >> Pi; cin.ignore();
        h[i] = Pi;
    }
    
    divide(h,0,(int)h.size() - 1);
    
    for (int i = 0; i < h.size(); i++) { 
        int size = h.size() - 1;
        if ((int)(i + 1) > (int)(size)) {
            break;
        } else if (abs(h[i] - h[i + 1]) < lowest) {
            lowest = abs(h[i] - h[i + 1]);
        }
    }

    // // Write an action using cout. DON'T FORGET THE "<< endl"
    // // To debug: cerr << "Debug messages..." << endl;
    cout << lowest << endl;
}
