## HybridSchedulerforRTOS
 Dynamically adjusts weights based on system load.  Prevents starvation by boosting tasks that have waited too long.  Normalizes wait time and burst time based on active tasks instead of fixed values.  Integrates resource management by checking available resources before scheduling.
Combines the strenght of all the other schedulers , does a prior analysis on the tasks and return the best one
