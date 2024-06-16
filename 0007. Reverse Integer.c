//Time Complexity: O(logx)
//Space Complexity: O(1)

#define MAX 10
#define INT_OVERFLOW 2147483647
#define INT_OVERFLOW_WITHOUT_FIRST_DIGIT 147483647

int reverse(int x){
    if(x == -INT_OVERFLOW - 1){
        return 0;
    }
    //Checking Sign
    int sign = 1;
    if(x < 0){
        sign = -1;
        x *= -1;
    }

    //Converting to String
    char strX[MAX + 1];
    sprintf(strX, "%d", x);
    int len = strlen(strX);

    //Checking Bounds
    int overflowDigits[] = {'2', '1', '4', '7', '4', '8', '3', '6', '4', '7'};
    if(len >= MAX){
        for(int i = 0; i < len; i++){
            if(strX[len - 1 - i] > overflowDigits[i]){
                return 0;
            }
            else if(strX[len - 1 - i] < overflowDigits[i]){
                break;
            }
        }
    }

    //Reversing
    int xReversed = 0;
    int iPow = 1;
    for(int i = 0; i < len-1; i++){
        xReversed += (strX[i] - '0') * iPow;
        iPow *= 10;
    }
    xReversed += (strX[len-1] - '0') * iPow;

    if(sign == -1){
        return -xReversed;
    }
    else{
        return xReversed;
    }
}
