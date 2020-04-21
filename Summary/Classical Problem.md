### Number Theory
* __The prime numbers__:
    * Euler sieve: $T:O(n)$
        ```C++
        int countPrimes(n){
            int i,j,countnum=1;
            int prime[MAX]
            bool num[MAX];
            memset(num,true,sizeof(num));
            for(i=2;i<=n;i++){
                if(num[i]) prime[countnum++]=i;
                for(j=1,j<countnum;j++){
                    if (i*prime[j]>n) break;
                    num[i*prime[j]]=false; //rule out the multiples of i
                    if (i%prime[j]==0) break; // the key step
                }
            }
        }
        /*
        i=2
            j=1 prime[1]=2  i*prime[j]=4
        i=3
            j=1 prime[1]=2  i*prime[j]=3
            j=2 prime[2]=3  i*prime[j]=9
        i=4 (!!!)
            j=1 prime[1]=2  i*prime[j]=8 //4%2==0 so the multiples of 4 must be the multiple of 2, i.e. 12=4*3=6*2, because of 4=2*n(n=2)
        i=5
            ...
        */
        ```