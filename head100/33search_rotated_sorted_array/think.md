# think
## my
this is a such hard question ,at first sight ,i even can't understand what this question intent to express 

after a long time,combine with the given examples i start to understand that.Previous the array is sorted,and at a assigned point it rotated,but even it's rotated we can know that at the left the array is increase and in the right it's also increase

but left > right and the given num either in the left or in the right  so we can search in binary search 

## chatgpt suggestion
    "a such hard question" 应改为 "such a hard question"，在 "such" 和 "a" 之间需要有一个空格。
    
    "at first sight" 应改为 "at first glance"，表示 "一开始看"。
    
    "i even can't understand" 应改为 "I couldn't even understand"，使用过去时态表达过去的情况。
    
    "Previous the array" 应改为 "Previously, the array"，表示 "先前，数组"。
    
    "at a assigned point" 应改为 "at an assigned point"，在 "a" 前要使用 "an"。
    
    "but even it's rotated" 应改为 "but even though it's rotated"，在 "even" 后要使用 "though" 连接从句。
    
    "at the left" 应改为 "on the left"，用 "on" 表示位置。
    
    "it's also increase" 应改为 "it also increases"，使用第三人称单数形式。
    
    "left > right" 应改为 "left is greater than right"，使用 "is greater than" 表示大于的关系。
    
    "the given num" 应改为 "the given number"，使用 "number" 表示数值。



"This is such a difficult question that, at first glance, I couldn't even understand the intended meaning. After spending a considerable amount of time and combining it with the given examples, I started to comprehend it. It appears that the array was previously sorted, but at a certain point, it underwent rotation. However, even after rotation, we can observe that the values on the left side of the rotation point are in increasing order, as are the values on the right side.

Since we know that the left side is greater than the right side and the given number can be either on the left or right side, we can perform a binary search to locate the target number."


# solution

Since we use binary search to locate the target,we must solve the very import question on our face that the close left and right.  In other words,we use < or use <=  and > and >= compare with the left and right and under what environment we should return -1

"Since we are using binary search to locate the target, we must address the crucial question right in front of us: should we use the open interval '<' or the closed interval '<='? And under what circumstances should we return -1?"

