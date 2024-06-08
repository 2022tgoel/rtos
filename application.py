from rtos import sched # the "syscalls"

def proc1():
    print("proc1")

def proc2():
    print("proc2")
    sched(proc3, 120)

def proc3():
    print("proc3")

def main():
    sched(proc1, 5)
    sched(proc2, 200)

if __name__ == "__main__":
    sched(main, 10)