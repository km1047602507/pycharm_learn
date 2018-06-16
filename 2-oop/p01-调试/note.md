调试
    调试流程：单元测试->集成测试->交测试部
    分类:
        静态调试：看
        动态调试：运行
pdb调试（在命令行进行调试）
    pdb:python调试库
pycharm调试
    run/debug模式
断点：程序中的某一行，程序在debug下遇到断点后停止
# 单元测试

    

        
        
        
# LOG日志
    级别：
        DEBUG
        INFO
        NOTICE
        WARNING
        ERROR
        CRITICAL
        ALERT
        EMERGENCU
    
    logging模块
        LOG的作用：
            调试
            了解软件的运行情况
            分析定位问题
        LOG信息：
            time
            location
            level
            内容
    成熟的第三方日志：
        log4j
        log4php
        logging
    logging模块；
    LOG的使用
        直接使用logging（封装了其他的模块）
            四大组件：
                日志器（Logger）:产生日志的接口
                    产生一个日志
                处理器（Handler）:把产生的日志发送到相应的目的地
                过滤器（Filter）:更精细的控制日志输出
                格式器（Formatter）:对输出的信息进行格式化
                
        logging.basicConfig(**kwargs)
            只在第一次调用的时候起作用
            不配置logger则使用默认值
                输出：sys.stderr
                级别：WARNING
                格式：level:log_name:content

#多线程
    程序
    进程
    线程
    全局解释器锁（GIL）
    _thread
    threading
    
    Lock
        lock = threading.Lock()
        lock.acquire()
        lock.release()
    线程不安全：list set dict
    线程安全：queue
#生产者消费者问题
    一个模型
        
    