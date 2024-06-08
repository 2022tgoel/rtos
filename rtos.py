from dataclasses import dataclass
from typing import List, Callable

@dataclass
class Proc:
    code: Callable
    priority: int
    # pi_waiters: List[Proc]


proc_list: List[Proc] = []
running_proc: Proc = None

def sched(code: Callable, priority: int) -> None:
    global running_proc
    def min_proc() -> Proc:
        if len(proc_list) == 0:
            return None
        return max(proc_list, key=lambda x: x.priority)
    
    proc_list.append(Proc(code, priority))

    parent_priority = running_proc.priority if running_proc is not None else -10000
    next = min_proc()
    while next is not None and next.priority > parent_priority:
        # start the proc
        running_proc = next
        proc_list.remove(next)
        next.code()
        # proc complete, 
        next = min_proc()


# class RT_Mutex:

#     def __init__(self):
#         pass

#     def acquire(self):
#         pass

#     def release(self):
#         pass