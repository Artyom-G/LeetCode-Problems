int tribonacci(int n){
    if(n == 0){
        return 0;
    }
    int t0 = 1;
    int t1 = 1;
    int t2 = 1; 
    int t3 = 0;
    for(int i = 2; i < n; i++){
        t0 = t1 + t2 + t3; 
        t3 = t2;
        t2 = t1;
        t1 = t0;
    }
    return t0;
}

//
