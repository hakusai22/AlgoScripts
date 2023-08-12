```bash
    当主函数main执行完成后，子goroutine执行了一次整个程序就执行结束了，
    main函数并不会等待子goroutine执行结束。一个goroutine的执行速度是非常快的，
    并且是主goroutine和子goroutine进行资源竞争，谁抢到资源多，谁就先执行。main函数是不会让着子goroutine的。
    我们可以在主goroutine中加上时间休眠，可以看每一个goroutine执行过程。
```