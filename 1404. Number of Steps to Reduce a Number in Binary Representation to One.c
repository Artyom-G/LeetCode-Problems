//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Bit Operations

int numSteps(char* s) {
    int counter = 0;
    int i = strlen(s) - 1;
    bool increment = 0;
    while(strlen(s) > 1){
        i = strlen(s) - 1;
        if(increment == 1){
            increment = 0;
        }
        else if(s[i] == '0'){
            s[i] = '\0';
        }
        else{
            while(i > 0){
                increment = 1;
                if(s[i] == '0'){
                    s[i] = '1';
                    increment = 0;
                    break;
                }
                else{
                    s[i] = '0';
                }
                i--;
            }
        }
        counter++;
        printf("%s\n", s);
    }
    return counter;
}


//Alternative faster solution:
//The output is always a + b where
//a is the difference between the next power of 2 and the input number
//b is the exponent on the power of 2
