# 思考
说实话 这个题作为简单题 对我而言是崩溃的

因为我不知道怎么实现 。。。 如果它是一道困难题 我还能聊以慰藉 可是它是一道简单题

# 题解

看了一圈题解 发现 解答晦涩难懂 遂用题目标题Divide Two Integers google 找到了老外的 leetcode题解

[Divide Two Integers](https://leetcode.com/problems/divide-two-integers/solutions/1516367/complete-thinking-process-intuitive-explanation-all-rules-followed-c-code/)

于我而言这个题解是看起来是更科学的 解释可读性也更高了


Representing the quotient in binary form: (11)10 = (1011)2:

	58 = (2^3 + 2^1 + 2^0) * 5 + 3                // --- (I)
	58 = [(2^3 * 5) + (2^1 * 5) + (2^0 * 5)] + 3  // --- (II)
Since we dont know the quotient and remainder the equation we know is:
58 = (q) * 5 + rem

We get a hint at what we would like to do here. We will first multiply 5 with maximum power of 2 such that the resulting number is still smaller than the dividend (read further if you don't understand why). Since multiplication operator is not allowed, we would use bitwise left shift to achieve this multiplication: each time we shift 5 by 1, we multiply it by 2:

	5 << 0 = 5               // less than dividend
	5 << 1 = 5*2 = 10        // less than dividend
	5 << 2 = 5*2*2 = 20      // less than dividend
	5 << 3 = 5*2*2*2 = 40    // less than dividend
	5 << 4 = 5*2*2*2*2 = 80  // (stop and consider the previous value as the result is greater than dividend
We observe that:
58 = (2^3 * 5) + (something * 5) + rem // --- (III)
You can see we are getting close to the equation we initialy wanted (eqa II).

Since 5 is multiplied with 23, we add 23 to our answer.
Further operating on equation III:

	58 - (2^3 * 5)  =  (something * 5) + rem
	58 - (8 * 5) = something * 5 + rem
	58 - 40 = something * 5 + rem
	18 = something * 5 + rem
What we effectively have done is, subtracted the result we got from our first step from dividend (58 - 40).
We arived at the same question again but with a smaller dividend this time.
dividend = 18, divisor = 5

Therefore let us repeat the process:

	5 << 0 = 5           // less than dividend
	5 << 1 = 5*2 = 10    // less than dividend
	5 << 2 = 5*2*2 = 20  // (stop and consider the previous value as the result is greater than dividend
We add 21 to our answer.
Looking back:

	18  =  (2^1 * 5) + (something * 5) + rem
	58 - (2^3 * 5) = (2^1 * 5) + (something * 5) + rem
	58 =  (2^3 * 5) + (2^1 * 5) + (something * 5) + rem
You can notice we are gradually advancing towards equ II:
Our new dividend is now:

	18 - (2^1 * 5)  =  (something * 5) + rem
	18 - (2 * 5) = something * 5 + rem
	18 - 10 = something * 5 + rem
	8 = something * 5 + rem
dividend = 8, divisor = 5
Repeating the process:

	5 << 0 = 5           // less than dividend
	5 << 1 = 5*2 = 10    // (stop and consider the previous value as the result is greater than dividend
We add 20 to our answer.
New dividend:

	8 = (2^0 * 5) + (something * 5) + rem
	8 - 5 = something * 5 + rem
	3 = something * 5 + rem
dividend = 3, divisor = 5
At this step, we stop iterating as our dividend is less than the divisor (we have also found our remainder = 3, as 5 should be multiplied with 0 and what remains is the remainder).

Looking back again for the last time:

	3 = 0*5 + rem
	8 = (2^0 * 5) + 3
	18  =  (2^0 * 5) + (2^1 * 5) + 3
	58 = (2^3 * 5) + (2^1 * 5) + (2^0 * 5) + 3
In the process, we have finally reached the equation we wanted to, and have got the answer as:
quotient = (2^3 + 2^1 + 2^0)


我们将用二进制形式表示商：(11)10 = (1011)2：

    58 = (2^3 + 2^1 + 2^0) * 5 + 3                // --- (I)
    58 = [(2^3 * 5) + (2^1 * 5) + (2^0 * 5)] + 3  // --- (II)
由于我们不知道商和余数，我们知道的方程是：
58 = (商) * 5 + 余数

我们从中得到了一个提示，我们首先将5乘以最大的2的幂，使得结果仍然小于被除数（如果你不明白为什么，请继续阅读）。由于不允许使用乘法运算符，我们将使用位左移操作符来进行这个乘法运算：每次将5左移1位，相当于将它乘以2：

    5 << 0 = 5               // 小于被除数
    5 << 1 = 5*2 = 10        // 小于被除数
    5 << 2 = 5*2*2 = 20      // 小于被除数
    5 << 3 = 5*2*2*2 = 40    // 小于被除数
    5 << 4 = 5*2*2*2*2 = 80  // （停止，并将前一个值视为结果，因为它大于被除数）

我们观察到：

    58 = (2^3 * 5) + (某个数 * 5) + 余数 // --- (III)
你可以看到我们逐渐接近我们最初想要的方程（方程II）。

由于5乘以23，我们将23加到我们的答案中。
进一步操作方程III：

    58 - (2^3 * 5)  =  (某个数 * 5) + 余数
    58 - (8 * 5) = 某个数 * 5 + 余数
    58 - 40 = 某个数 * 5 + 余数
    18 = 某个数 * 5 + 余数
    我们实际上是将我们从第一步得到的结果从被除数中减去（58 - 40）。
    我们以一个较小的被除数再次得到了相同的问题。
    被除数 = 18，除数 = 5

因此，让我们重复这个过程：

    5 << 0 = 5           // 小于被除数
    5 << 1 = 5*2 = 10    // 小于被除数
    5 << 2 = 5*2*2 = 20  // （停止，并将前一个值视为结果，因为它大于被除数）
我们将21加到我们的答案中。
回顾一下：

    18  =  (2^1 * 5) + (某个数 * 5) + 余数
    58 - (2^3 * 5) = (2^1 * 5) + (某个数 * 5) + 余数
    58 =  (2^3 * 5) + (2^1 * 5) + (某个数 * 5) + 余数
你可以注意到我们逐渐接近方程II：
我们的新被除数现在是：

    18 - (2^1 * 5)  =  (某个数 * 5) + 余数
    18 - (2 * 5) = 某个数 * 5 + 余数
    18 - 10 = 某个数 * 5 + 余数
    8 = 某个数 * 5 + 余数
被除数 = 8，除数 = 5
重复这个过程：

    5 << 0 = 5           // 小于被除数
    5 << 1 = 5*2 = 10    // （停止，并将前一个值视为结果，因为它大于被除数）
我们将20加到我们的答案中。
我们的新被除数是：

    8 = (2^0 * 5) + (某个数 * 5) + 余数
    8 - 5 = 某个数 * 5 + 余数
    3 = 某个数 * 5 + 余数
被除数 = 3，除数 = 5
在这一步，我们停止迭代，因为被除数小于除数（我们也找到了余数=3，因为5应该乘以0，剩下的就是余数）。

再次回顾一下：

    3 = 0*5 + 余数
    8 = (2^0 * 5) + 3
    18  =  (2^0 * 5) + (2^1 * 5) + 3
    58 = (2^3 * 5) + (2^1 * 5) + (2^0 * 5) + 3
在整个过程中，我们最终达到了我们想要的方程，并得到了答案：
商 = (2^3 + 2^1 + 2^0)