//Time Complexity: O(logn)
//Space Complexity: O(1)

#define HALF_OVERFLOW 1073741824

bool isPowerOfTwo(int n) {
    if(n == HALF_OVERFLOW){
        return true;
    }
    else if(n > HALF_OVERFLOW){
        return false;
    }

    int num = 1;
    while(num < n){
        num*=2;
    }
    if(num == n){
        return true;
    }
    else{
        return false;
    }
}
