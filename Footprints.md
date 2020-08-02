### <center>Footprints</center>

* <a href='https://github.com/apachecn/AiLearning/blob/master/docs/nlp/Word2Vec.md'>Word2Vec</a>【4/18 2020】
    * continuous bag-of-words model
    * skip-gram

* <a href='https://github.com/apachecn/nlp-pytorch-zh/blob/master/docs/1.md'>TF术语频率(TF)和术语频率反转文档频率(TF-idf)</a>【4/20 2020】 
    * TF-IDF反映了在文档集合中一个单词对一个文档的重要性，经常在文本数据挖据与信息提取中用来作为权重因子。在一份给定的文件里，词频(term frequency-TF)指的是某一个给定的词语在该文件中出现的频率。逆向文件频率（inverse document frequency，IDF）是一个词语普遍重要性的度量。某一特定词语的IDF，可以由总文件数目除以包含该词语之文件的数目，再将得到的商取对数得到
* __ML__: Decision Tree【4/25 2020】
* 【7/1 2020】
    * 机器学习中的求导法则
        * 分子布局、分母布局：__二者仅相差一个转置__
        * 列对列：Jacobian（分子布局）$\frac{\partial\bf{y}}{\partial\bf{x}^T }$ 矩阵 & 梯度矩阵（分母布局）$\frac{\partial\bf{y}^T}{\partial\bf{x} }$

    * 算法：
        * <a href='https://leetcode-cn.com/problems/add-digits/'>数根</a>
        * 出现一次的两个数

* 【7/2 2020】
    * 算法：
        * <input type='checkbox'><a href="https://leetcode-cn.com/problems/ugly-number-ii/">丑数II</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/h-index/'>H-index的计数排序</a>

* 【7/3 2020】
    * 算法：
        * Linked list cycle
        * 41.First Missing Positive

* 【7/5 2020】
    * alg:
        * <a href='https://leetcode-cn.com/problems/count-submatrices-with-all-ones/'>统计全为一的矩形的个数</a>
        * <a href='https://leetcode-cn.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/'>最多 K 次交换相邻数位后得到的最小整数</a>
        * 线段树
        * 树状数组
    * 支持向量机的重要性质：只与支持向量有关
        * 核函数：
            * 如果原始空间时有限维，那么一定存在一个高维特征空间是样本可分。
            * 计算：半正定核函数$\bf{K}$一定能找到一个$\phi$与之映射，任何一个核函数都隐式地定义了一个再生核希尔伯特空间？
        * 软间隔与正则化
            * 原因
            * 优化目标，损失函数 (hinge, 指数, 对数)

* 【7/6 2020】
    * alg：
        * 复习之前算法，并且记忆常见框架
        * <span style="color:red;">练习【线段树&树状数组】</span>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/'>1477.满足条件的子序列数目</a> 
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k/'>1488.检查数组对是否可以被 k 整除</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/max-value-of-equation/'>1499.满足不等式的最大值</a>
        * <span style='color:red'>单调队列&单调栈【经典的模板题，要反复做】</span>

    * 训练集，验证集，测试集：P28
        * 验证集：模型选择和调参
        * 测试集：模型的泛化能力

* 【7/7 2020】
    * alg:
        * 单调队列复习，1499 done
        * 树状数组1【单点修改，区间查询】
        * 树状数组2【区间修改，单点查询】
        * <input type='checkbox' checked></input><a href='https://leetcode-cn.com/problems/longest-increasing-subsequence/'>Longest Increasing Subsequence ($O(nlog(n))$)</a>
    * 
* 【7/9 2020】
    * alg:
    * ml:
        * 策略：期望风险，经验风险，结构风险

* 【7/11 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/parallel-courses-ii/'>并行课程 II</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/increasing-triplet-subsequence/'>334. Increasing Triplet Subsequence</a>
* 【7/12 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/path-with-maximum-probability/'>5211. Path with Maximum Probability</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/best-position-for-a-service-centre/'>5463. Best Position for a Service Centre</a>
        
* 【7/14 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/remove-invalid-parentheses/'>301. Remove Invalid Parentheses</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/generate-parentheses/'>22. Generate Parentheses</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/longest-valid-parentheses/' style='color:red'>32. Longest Valid Parentheses</a>
        * <input type='checkbox'><a href='https://ac.nowcoder.com/acm/problem/13230'>合并回文子串【区间DP】</a>
            * Note: the definition of states and the recursive formula
    * kaggle:
        * <a href='http://suo.im/5Jb9dM'>小白入门</a>
            1. <input type=checkbox checked>选择一门编程语言
            2. <input type='checkbox'>学习探索数据的基础 __<a href='http://seaborn.pydata.org/'>Seaborn</a>__ 库
            3. <input type='checkbox'>训练你的第一个机器学习模型 __<a href='http://www.scikitlearn.com.cn/'>Scikit-Learn</a>__ 库
            4. <input type="checkbox">解决入门级竞赛: Getting Started 竞赛非常适合初学者，因为它们给你提供了低风险的学习环境，并且还有很多社区创造的<a href='https://www.kaggle.com/c/titanic#tutorials'>社区创造的教程</a>
            5. 诀窍：
                * 设置循序渐进的目标
                * 查阅得票最多的 kernel
                * 在论坛中提问
                * 独立发展核心技能
                * 组队以拓展你的极限
                * 记住 Kaggle 可以成为你的垫脚石
                * 不要担心排名低

* 【7/15 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/range-sum-query-2d-immutable/submissions/'>304. Range Sum Query 2D - Immutable</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/additive-number/'>306. Additive Number</a>
    * ml:
        * PCA(方差): 样本方差 vs 样本信息量，方差越大，所含信息越大
        * SVD(奇异值)
        * <a href='https://www.jianshu.com/p/7919ef304b19'>概念定义：</a>
        * 啥叫 __精确度__：就是你预测的正例（预测对了的即$TP$，预测错了的$FP$）当中真正的正例$P=\frac{TP}{TP+FP}$
        * 召回了多少即 __召回率__：$R=\frac{TP}{TP+FN}$
        * __特异度__：就是你预测是反例（预测对了$TN$，预测错的$FN$）$Specificity=\frac{TN}{TN+FN}$
        * __假正率__: FPR(false positive rate)=1-$S$ 评价判断错误的能力
        * <span style='color:red;font-weight:bold'>ROC</span>: 横坐标是FPR, 纵坐标是RECALL, 比较理想的是，发现的正例越多，也就是RECALL越高，而犯错的比率越低，也就是而假正率越低，是比较理想的分类器。【正例召回率vs反例召回率】
        * ACC：classification accuracy，描述分类器的分类准确率
        计算公式为：ACC=(TP+TN)/(TP+FP+FN+TN)
        * BER：balanced error rate
        计算公式为：BER=1/2*(FPR+FN/(FN+TP))
        * __召回率__ TPR：true positive rate，描述识别出的所有正例占所有正例的比例
        计算公式为：TPR=TP/ (TP+ FN)
        * __假正率__ FPR：false positive rate，描述将负例识别为正例的情况占所有负例的比例
        计算公式为：FPR= FP / (FP + TN)
        * TNR：true negative rate，描述识别出的负例占所有负例的比例
        计算公式为：TNR= TN / (FP + TN)
        其中TPR即为敏感度（sensitivity），TNR即为特异度（specificity）。
* 【7/16 2020】
    * alg:
        * <input type='checkbox' checked>$\#191$ <a href='https://leetcode-cn.com/contest/weekly-contest-191/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/'>【dfs】1466. 重新规划路线</a>
        * __图的模板(BFS, DFS, TOP SORT)__
    * ml:
        * <a href='https://zhuanlan.zhihu.com/p/24709748' style="color:red;font-weight:bold">矩阵求导上</a><a href='https://zhuanlan.zhihu.com/p/24863977'>下(知乎)</a>
        * sci-kit learn 里面只要是描述损失的都是负数，例如均方根误差是neg_mse __#p62__
        * 贝叶斯的了解：
        * $R^2$值的定义 __#P63__, $R^2=1-\frac{RSS}{\sum_{i=0}^{m}{(y_i-\bar{y})^2}}$, 代表1-损失掉的信息所占的比率，因此越接近于1越好
        * __bootstrap（穿脱靴子）有放回抽样，注意集成学习算法中的bagging和boosting建树的区别__
        * numpy轴向 __设axis=i，则numpy沿着第i个下标变化的方向进行操作__, 例如所以axis=0时，沿着第0个下标变化的方向进行操作，也就是a**0**0->a**1**0, a**0**1->a**1**1，也就是纵坐标的方向，__正好对应着列向量__，axis=1时也类似
        * numpy.cov的计算方式, 注意参数rowvar=False意为：行为sample,列为feature, 默认值为True, <a href='https://njuferret.github.io/2019/07/26/2019-07-26-covariance/' style='color:red;font-weight:bold;'>协方差</a>, <a href='https://blog.csdn.net/iloveyousunna/article/details/77948219'>系数求法</a>

* 【7/17 2020】
    * alg:
        * <a href='https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/'>股票类型</a>
    * ml:
        * <a href='https://www.cnblogs.com/pinard/p/10791506.html'>矩阵求导(博客园)</a>：
            * __<span style='color:red'>核心：</span>__ **全微分**到**迹**之间的一个转换
            $df=\sum_{i=1}^m\sum_{j=1}^n{\frac{\partial{f}}{\partial{X_{i,j}}}}dX_{i,j}=tr((\frac{\partial{f}}{\partial{X}})_{m\times{n}}^TdX_{_{m\times{n}}})$ 注意 $(\frac{\partial{f}}{\partial{X}})^T$是**矩阵**
            * __重点__ : $tr(A^TB)=\sum_{i,j}{A_{i,j}B_{i,j}}=
            \begin{bmatrix}
            a_{11} & a_{21}
            \\a_{12}  & a_{22}
            \end{bmatrix}\cdot
            \begin{bmatrix}
            b_{11} & b_{12}
            \\b_{21}  & b_{22}
            \end{bmatrix}=a_{11}b_{11}+a_{21}b_{21}+a_{12}b_{12}+a_{22}b_{22}=A\bigodot{B}
            $ 
            即：两个矩阵的内积(对应位置乘积也就是两个矩阵的<a href='https://blog.csdn.net/yao1131/article/details/78332037'>哈达马乘积</a>之和) $A\bigodot{B}=tr{(A^TB)}$
            * 基本重要运算法则及其证明：
                * 微分：$dtr(X)=tr(dX)$
                * 迹：$tr(AB)=tr(BA)$
                * 常见公式：
                    * $\frac{\partial{tr(AB)}}{\partial{A}}=B^T$ or $\frac{\partial{tr(AB)}}{\partial{B}}=A^T$ 定义法可证
                    * $\frac{\partial{tr(W^TAW)}}{\partial{W}}=(A+A^T)W$
* 【7/18 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/minimum-height-trees/'>310. Minimum Height Trees</a>
        * <input type='checkbox' checked><a href='https://leetcode-cn.com/problems/interleaving-string/'>97. Interleaving String【滚动数组优化】</a>
    * ml:
        * 
* [7/19 2020]  
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/burst-balloons/'>312. Burst Balloons</a>
        * <input type='checkbox' checked><a href='https://leetcode-cn.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/'>5465. Number of Nodes in the Sub-Tree With the Same Label</a>  [-optimization]
        * 

* 【7/20 2020】
    * ml:
        * <a href='https://github.com/Sakura-gh/ML-notes'>笔记</a>，<a href='https://github.com/Iallen520/lhy_DL_Hw'>作业</a>
        * adagrad 控制梯度下降方式：造成反差的结果
        * 朴树贝叶斯公式，好好理解一下: 预测$P(C_k|x)=\frac{P(x|C_k)P(C_k)}{\sum_iP(x)P(x|C_i)}$因此 $\mathcal{Y}=\argmax_{c_k}{P(x|C_k)P(C_k)}$ 即各种分类中是x的情况下，分类$C_1$是x的概率，注意所谓先验概率，后验概率也是从这看出
        * 贝叶斯公式$P(C|x)=\frac{P(x,C)}{P(x)}=\frac{P(x,C)}{\sum_iP(x,C_i)}$(即所有x中分类概率最大的分类)$=\frac{P(x|C)P(C)}{\sum_iP(x,C_i)}=\frac{P(x|C)P(C)}{\sum_iP(x|C_i)P(C_i)}$

* 【7/20 2020】
    * ml:
        * <input type='checkbox' checked><a href='https://leetcode-cn.com/problems/unique-binary-search-trees-ii/'>95. Unique Binary Search Trees II</a>
        * <input type='checkbox'><a href=''>357. Count Numbers with Unique Digits【math-combination, dp,】</a>
        * Sigmoid函数的特点：
            * $S(x)=\frac{1}{1+e^x}$
            * $S'=\frac{e^x}{1+e^x}=S(1-S)$
        * 逻辑斯蒂回归模型：
            * 搞懂什么是模型!!!，弄清**模型、策略（损失函数）、算法（优化器）** 之间的关系
            * <span style='color:red;font-weight:bold'>1.模型; 
            2.求模型的参数->损失函数(参数的函数)->优化器（损失函数最小值时的参数）</span>
* 【7/22 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/'>315. Count of Smaller Numbers After Self</a><a href='https://www.bilibili.com/video/BV1BW411C7TM?from=search&seid=8177914316991403908'> 讲解</a>
* 【7/25 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/split-array-largest-sum/'>410. Split Array Largest Sum</a>
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/remove-duplicate-letters/'>316. Remove Duplicate Letters</a> 注意与LIS问题的联系

* 【7/26 2020】
    * alg:
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/'>329. Longest Increasing Path in a Matrix</a>
        * <input type='checkbox'><a href=''>5462. String Compression II</a>
    * 
* 【7/28 2020】
    * alg:didi面试（out）
    * ml:
        * z-score: 数据标准化$\frac{x-μ}{\sigma}$，就是将不同量级的数据统一转化为同一个量级，统一用计算出的Z-Score值衡量，以保证数据之间的可比性
* 【7/30 2020】
    * alg: 
        * <input type='checkbox'><a href='https://leetcode-cn.com/problems/integer-break/'>343. Integer Break</a>
        * 