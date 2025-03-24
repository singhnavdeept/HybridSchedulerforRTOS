




def hybrid_scheduler(tasks, current_time, resource_manager):
    


    ready_tasks = [task for task in tasks if current_time >= task.arrival_time and task.remaining_time > 0]
    
    if not ready_tasks:
        return None 
    task_count = len(ready_tasks)
    urgency_weight = 0.5 + (0.1 * (task_count / 10))  # more tasks = higher urgency
    fairness_weight = 0.3 + (0.1 * (task_count / 15))  # more tasks = fairness matters more
    efficiency_weight = 1.0 - (urgency_weight + fairness_weight)  # remaining weight for short tasks

    
    longest_wait = max((current_time - task.arrival_time for task in ready_tasks), default=1)
    longest_burst = max((task.remaining_time for task in ready_tasks), default=1)

    best_task = None
    highest_priority = float('-inf')

    for task in ready_tasks:
      
        time_left = task.deadline - current_time
        urgency_score = 1.0 if time_left <= 0 else min(1.0 / (time_left + 1), 1.0)

       
        wait_time = current_time - task.arrival_time
        fairness_score = wait_time / longest_wait if longest_wait > 0 else 0

       
        efficiency_score = 1.0 - (task.remaining_time / longest_burst) if longest_burst > 0 else 0

      
        if wait_time > 20:
            fairness_score += 0.2  

       
        priority_score = (
            (urgency_weight * urgency_score) +
            (fairness_weight * fairness_score) +
            (efficiency_weight * efficiency_score)
        )

       
        if resource_manager.is_task_runnable(task):
            if priority_score > highest_priority:
                highest_priority = priority_score
                best_task = task 

    return best_task
#return the chosen task may return none if none are runnable , will adjust based on each task as  a batch of task is randomly genrated evry time 
