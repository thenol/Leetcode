/*
链接：https://ac.nowcoder.com/acm/problem/21302
来源：牛客网

题目描述 
给你一个长度为50的数字串,问你有多少个子序列构成的数字可以被3整除
答案对1e9+7取模
输入描述:
输入一个字符串，由数字构成，长度小于等于50
输出描述:
输出一个整数
示例1
输入
复制
132
输出
复制
3
示例2
输入
复制
9
输出
复制
1
示例3
输入
复制
333
输出
复制
7
示例4
输入
复制
123456
输出
复制
23
示例5
输入
复制
00
输出
复制
3
备注:
n为长度
子任务1: n <= 5
子任务2: n <= 20
子任务3: 无限制
*/

# include <iostream>
# include <cstring>
using namespace std;
int main(){
    char s[50];
    cin>>s;
    int N=strlen(s);
    long long M=1e9+7;
    int d[N][3];
    for(int i=0;i<3;i++){
        d[0][i]=0;
    }
    d[0][s[0]%3]=1;
    for(int i=1;i<N;i++){
        int mod=int(s[i])%3;
        switch(mod){
            case 0:
                d[i][0]=(2*d[i-1][0]+1)%M;
                d[i][2]=(2*d[i-1][2])%M;
                d[i][1]=(2*d[i-1][1])%M;
                    break;
            case 1:
                d[i][0]=(d[i-1][0]+d[i-1][2])%M;
                d[i][1]=(d[i-1][0]+d[i-1][1]+1)%M;
                d[i][2]=(d[i-1][1]+d[i-1][2])%M;
                break;
            case 2:
                d[i][0]=(d[i-1][0]+d[i-1][1])%M;
                d[i][2]=(d[i-1][0]+d[i-1][2]+1)%M;
                d[i][1]=(d[i-1][2]+d[i-1][1])%M;
                break;
        }
        // cout<<d[i-1][0]<<d[i-1][1]<<d[i-1][2]<<endl;
    }
    cout<<d[N-1][0];
}