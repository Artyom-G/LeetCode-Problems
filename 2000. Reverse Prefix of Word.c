//Time Complextity: O(n)
//Space Complexity: O(1)
char* reversePrefix(char* word, char ch) {
    int index;
    for(index = 0; index < strlen(word) + 1; index++){
        if(word[index] == ch){
            break;
        }
    }
    if(index >= strlen(word)){
        return word;
    }

    char temp;
    for(int i = 0; i <= index/2; i++){
        temp = word[i];
        word[i] = word[index - i];
        word[index - i] = temp;
    }
    return word;
}
