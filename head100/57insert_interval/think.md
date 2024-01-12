# given information

intervals 

    no overlapping

newInterval


solve steps

    1 first traverse the intervals if the interval[1] < newInterval[0] add to the res
    2 if interval[0] < newInterval[1]  overlapping then merge
         newInteravl[0] = min(interval[0],newInterval[0])
         newInterval[1] = max(interval[1],newInterval[1])
    3 when overlapping stop  add the newInterval to the result
    4 add the result list to the result


本题中的区间已经按照起始端点升序排列，因此我们直接遍历区间列表，寻找新区间的插入位置即可。具体步骤如下：

    1首先将新区间左边且相离的区间加入结果集（遍历时，如果当前区间的结束位置小于新区间的开始位置，说明当前区间在新区间的左边且相离）；
    
    2接着判断当前区间是否与新区间重叠，重叠的话就进行合并，直到遍历到当前区间在新区间的右边且相离，将最终合并后的新区间加入结果集；
    
    3最后将新区间右边且相离的区间加入结果集。

    


















    