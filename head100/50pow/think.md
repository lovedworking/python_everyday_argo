这种题 
一般递归可以实现 考虑不同情况 

递归转迭代

## 快速幂？

    观察奇数情况下 2^5 = 2*2*2*2*2
    5 // 2 = 2   5 % 2 = 1 也就是奇数
    所以相当于 2*2^2 * 2 = 2^(n//2)*2
    偶数情况下就简单了
    2^4 = 2^2*2^2 
    以上只需要把2换成对应的x就行了

以上是针对正数的规律
如果是负数呢？
    1/x**n
    2

    
考虑 0 return -1
奇数
偶数 
## 递归

        if n == 0:
            return 1.0
        if n < 0:
            return 1/self.myPow(x, -n)
        else:
            if n % 2 == 0:
                return self.myPow(x*x, n // 2)
            else:
                return x * self.myPow(x*x, n // 2)

## 迭代

要做的是乘数翻倍

        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result = result * x
            x = x * x
            n = n // 2
        return result

如何把递归转化为迭代


