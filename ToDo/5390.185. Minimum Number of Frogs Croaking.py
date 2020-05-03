'''
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 思想就是维护croak的个数，如果遇到当前字母，则肯定是由前面字母过来，前面字母数-1。
# 如遇到r，则必是c->r，所以c--
# k代表结尾，其实也是青蛙的起始（一次喊叫结束），所以遇到c的时候，先去消耗k，没有k了，需要新青蛙，答案+1

'''
public int minNumberOfFrogs(String croakOfFrogs) {
        c = 0; r = 0; o = 0; a = 0;k = 0;
        char []chars = croakOfFrogs.toCharArray();
        int res = 0;
        for(int i = 0;i < chars.length;i++){
            if(chars[i] == 'c'){
                if(k > 0){k--;}else{res++;}
                c++;
            }else if(chars[i] == 'r'){
                c--;r++;
            }else if(chars[i] == 'o'){
                r--;o++;
            }else if(chars[i] == 'a'){
                o--;a++;
            }else if(chars[i] == 'k'){
                a--;k++;
            }
            if(c < 0 || r < 0 || o < 0 || a < 0){
                break;
            }
        }
        if(c != 0 || r != 0 || o != 0 || a != 0){
            return -1;
        }
        return res;
    }
'''

# 作者：imcover
# 链接：https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking/solution/cai-ji-gong-xian-ge-chun-onzuo-fa-by-imcover/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。