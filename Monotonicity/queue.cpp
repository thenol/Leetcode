/**
 * 给N个数求每连续k个最小的数
 * 暴力O(NK), 单调队列O(N)
 */
/* 
9 4
1 4 7 5 3 6 9 8 2
*/
// monotonous queue

// C:

# include<bits/stdc++.h>
using namespace std;
int N,K,d[10001],q[10001],idx[10001],le=1,ri;// two arrays: idx is index, and q is the value
int main(){
    cin>>N>>K;
    for(int i=1;i<=N;i++)cin>>d[i];
    for(int i=1;i<=N;i++){
        while(le<=ri&&d[i]<q[ri])ri--;// remove the elements in the queue greater than the i, monotonic reduction
        ri++;
        q[ri]=d[i];
        idx[ri]=i; //index of the digit in the queue, note N times of operation
        if(idx[le]+K<=i) le++;// remove each time, so once is enough
        // the value in the queue must is the maximum of the [:i+1]
        if(i>=K)cout<<q[le]<<" ";// output each time, note the question, 
    }
    cout<<endl;
    
}