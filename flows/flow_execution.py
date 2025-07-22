from prefect import task, flow

@task
def say_task1():
    print("Hi! I am task 1!")


@task
def say_task2():
    print("hi!I am task 2")


@task
def say_task3():
    print("hi! i am task 3")

@flow
def my_second_flow():
    say_task1()
    say_task2()
    say_task3()

if __name__=="__main__":
    my_second_flow()

