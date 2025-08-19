from flytekit import task, workflow

@task
def sum_task(x: int, y: int) -> int:
    return x + y

@workflow
def my_workflow(x: int, y: int) -> int:
    return sum_task(x=x, y=y)
