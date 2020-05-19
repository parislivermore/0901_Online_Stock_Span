題目地址：https://leetcode.com/problems/online-stock-span/description/

題目描述
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
題目大意
這個題要我們求，當一個新的股票價格來到的時候，在這個天數過去的多少天內，股票的價格是小於等於今天的。注意的是，從今天向前面數已經經過的天數，今天也包括在內。

解題方法
單調遞減棧
看了數值的範圍，可以肯定這個題的時間複雜度必須在O(n)以內，也就是說平均每次next()方法調用的時候，必須在將近O(1)的時間內找到前面多少天的價格是小於等於今天的。

這個題的重點在於连续二字上，我們只需要向前找到第一個比當前數字大的位置就停止。那麼我們只需要找到數字A其前面有多少個連續的並且比它小的數字個數a即可，這樣，當我們後面出現一個數字B，當B>=A時，在B前面小於等於B的連續數字共有a + 1個；當B < A時，在B前面小於等於B的連續數字只有1個，那就是B自己。

思路是使用一個單調遞減棧，這個棧裡保存的是當前的價格向前可以找連續的多少天。注意這個棧裡存放的內容是嚴格單調遞減的，如果新來的數值大於了棧頂元素，那麼就要把棧頂的元素給彈出去，直到當前元素小於棧頂才行。

這樣做的好處就是，我們沒必要保留較小的元素，只需要知道每個元素前面有幾個比它小的數字就行了。因為我們在遍歷的過程中，是在找比當前元素小的元素個數，棧頂保留的只有較大的元素和它前面出現的次數，那麼就知道了前面比它小的元素個數。

如果按照題目的示例，每次next()函數調用之後，棧中的內容如下：

[(100, 1)]
[(100, 1), (80, 1)]
[(100, 1), (80, 1), (60, 1)]
[(100, 1), (80, 1), (70, 2)]
[(100, 1), (80, 1), (70, 2), (60, 1)]
[(100, 1), (80, 1), (75, 4)]
[(100, 1), (85, 6)]

每步操作的平均時間複雜度是O(1)，最壞的時間複雜度是O(n)，空間複雜度是O(1).

代碼如下：
"""
Runtime: 672 ms, faster than 9.18% of Python3 online submissions for Online Stock Span.
Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Online Stock Span.
"""
class StockSpanner(object):
    def __init__(self):
        self.a = []
    def next(self, price):
        res = 1
        while self.a and self.a[-1][0] <= price:
            res += self.a.pop()[1]
        self.a.append((price, res))
        return res
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

參考資料：

https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O(1)

日期
2018年9月20日——趁年輕多讀書
2019年3月24日——再做一遍還是不會
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/82781059
