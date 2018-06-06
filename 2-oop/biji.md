lambda  函数式编程
map  系统高阶函数
reduce  归并、缩减
    把可迭代的对象最后后归并为一个结果
    reduce需要导入functools包
        from functools import reduce
    filter  过滤函数  符合条件的生成一组列表
        map是一对一的，而filter是数据合并
        返回值一定是一个布尔值
    高阶函数排序  
        key：
            sorted():
            sort():
    返回函数：
        可以返回具体值，也可以是函数
        
        
    闭包(closure)
        闭包的作用
    
装饰器
    在不改动代码的基础上无限制扩展函数功能的一种机制
    装饰器使用@语法
        @printTime
    一旦定义，则可以装饰任意函数
    
偏函数
    参数固定的函数，相当于一个由特定参数的函数体
    functools.partial包
    
zip:把两个可以迭代的内容生成一个可以迭代tuple的内容
    可以迭代的数据不可以用列表生成式
enumerate:跟zip很相似
    每一个元素配上一个索引，是tuple类型
collections模块:
    namedtuple
    deque
    defaultdict:
    Counter:统计字符的个数
    
    
    
    
