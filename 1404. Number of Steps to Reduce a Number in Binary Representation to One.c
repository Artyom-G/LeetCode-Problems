//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Bit Operations

int numSteps(char* s) {
    int counter = 0;
    int i = strlen(s) - 1;
    bool increment = 0;
    while(strlen(s) > 1){
        i = strlen(s) - 1;
        //Incrementing is explained below, but essentially is an edge case
        if(increment == 1){
            increment = 0;
        }
        //If even then divide by 2 in bin
        else if(s[i] == '0'){
            s[i] = '\0';
        }
        //If odd then increment every bit from the end by 1 until you reach a 0 then stop incrementing
        else{
            while(i > 0){
                //This sets the increment to 1 in the case where the input string is '111' and needs to be expanded to '1000', this carries the extra carry-on bit
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
    }
    return counter;
}


//Alternative faster solution:
//The output is always a + b where
//a is the difference between the next power of 2 and the input number
//b is the exponent on the power of 2
