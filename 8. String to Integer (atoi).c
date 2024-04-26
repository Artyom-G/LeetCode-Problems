//Time Complexity: O(n)
//Space Complexity: O(1)
int myAtoi(char* s) {
    if(strlen(s) == 0){
        return 0;
    }

    //partitioning string
    char *strX;
    int seenInt = -1;
    int len = 0;
    int sign = 1;
    for(int i = 0; i < strlen(s); i++){
        if(s[i] >= '0' && s[i] <= '9'){
            if(seenInt == -1 || s[seenInt] == '0'){
                strX = &s[i];
                seenInt = i;
            }
        }
        else if(seenInt != -1){
            len = i - seenInt;
            break;
        }
    }
    if(seenInt == -1){
        return 0;
    }
    if(seenInt != -1 && len == 0){
        len = strlen(s) - seenInt;
    }
    printf("%s\n", strX);

    //Checking Sign
    if(seenInt - 1 >= 0 && s[seenInt - 1] == '-'){
        sign = -1;
    }
    else if(seenInt - 1 >= 0 && s[seenInt - 1] == '+'){

    }else if(seenInt - 1 < 0 || s[seenInt - 1] == '0' || s[seenInt - 1] == ' '){

    }
    else{
        return 0;
    }

    //Checking everything before first digit is whitespace
    for(int i = 0; i < seenInt - 1; i++){
        if(s[i] != ' ' && s[i] != '0'){
            return 0;
        }
    }

    //Checking Bounds
    if(len > 10){
        if(sign == 1){
            return 2147483647;
        }
        else{
            return -2147483648;
        }
    }

    int overflowDigits[] = {'2', '1', '4', '7', '4', '8', '3', '6', '4', '7'};
    if(len == 10){
        for(int i = 0; i < len; i++){
            if(strX[i] > overflowDigits[i]){
                if(sign == 1){
                    return 2147483647;
                }
                else{
                    return -2147483648;
                }
            }
            else if(strX[len - 1 - i] < overflowDigits[i]){
                break;
            }
        }
    }

    //Outputting
    int output = 0;
    int iPow = 1;
    for(int i = len-1; i >= 1; i--){
        output += (strX[i] - '0') * iPow;
        iPow *= 10;
    }
    output += (strX[0] - '0') * iPow;

    return sign * output;
}
