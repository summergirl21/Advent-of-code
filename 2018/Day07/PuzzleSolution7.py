
"""
Part 1 Solution
Use a tree to map out the dependencies?
Each element will have
Name
List of non completed dependencies, will remove elements when completed to make it simple to see if this step is ready.
List of steps that depend on this step, so they can be updated when this step is completed
Create a dict of name to step, so that it's easy to find them, seems easier than creating links everywhere.

Part 2
Have a while loop that ticks through seconds
On each second, you need to update the status of each worker
If it has a task, reduce the time left for that task
If it doesn't have a task, check if there are any tasks available to start
When all the tasks are completed the time is up
"""
from dataclasses import dataclass

DEBUG = True


def log(s):
    if DEBUG:
        print(s)


@dataclass
class Step:
    Name: str
    Pre: list[str]
    Post: list[str]

@dataclass
class Task:
    Name: str
    Pre: list[str]
    Post: list[str]
    Time: int


def main():
    print("Hello")
    process_file("ExampleInput7.txt", 0, 2)
    print()
    process_file("PuzzleInput7.txt", 60, 5)


def process_file(file_name, time_offset, num_workers):
    with open(file_name) as file:
        lines = list(map(lambda x: x.strip().lower(), file.readlines()))
        print("Part 1")
        solve_part1(lines)

        print("\nPart 2")
        solve_part2(lines, time_offset, num_workers)


def parse_line(line: str) -> tuple[str, str]:
    line = line.split("step ")
    pre_step = line[1].split(" must be finished before ")[0]
    # log(f"Pre step {pre_step}")
    post_step = line[2].split(" can begin.")[0]
    # log(f"Post Step {post_step}")

    return pre_step, post_step


def parse_step_info(lines: list[str]) -> dict[str, Step]:
    steps: dict[str, Step] = dict()
    for line in lines:
        # log(line)
        pre_step_id, post_step_id = parse_line(line)

        pre_step = steps.get(pre_step_id, Step(pre_step_id, list(), list()))
        pre_step.Post.append(post_step_id)
        steps[pre_step_id] = pre_step

        post_step = steps.get(post_step_id, Step(post_step_id, list(), list()))
        post_step.Pre.append(pre_step_id)
        steps[post_step_id] = post_step
    return steps


def find_available_steps(steps: dict[str, Step]) -> list[str]:
    avail_steps = list(filter(lambda x: len(steps[x].Pre) == 0, steps.keys()))
    return avail_steps


def solve_part1(lines):
    steps = parse_step_info(lines)

    # log(f"Steps: {steps}")

    result = ""
    while len(steps.keys()) > 0:
        avail_steps = find_available_steps(steps)
        next_step_id = sorted(avail_steps)[0]
        cur_step = steps[next_step_id]

        # log(f"processing step {cur_step.Name}")
        result += cur_step.Name
        for step_id in cur_step.Post:
            step = steps[step_id]
            step.Pre.remove(cur_step.Name)
        del steps[cur_step.Name]

    print(f"Resulting step order {result.upper()}")


def create_tasks_from_steps(steps: dict[str, Step], time_offset: int) -> dict[str, Task]:
    tasks = dict()
    for step in steps.values():
        time = time_offset + ord(step.Name) - 96
        tasks[step.Name] = Task(step.Name, step.Pre, step.Post, time)

    return tasks


def find_avail_tasks(tasks: dict[str, Task], in_progress_tasks) -> list[str]:
    avail_tasks = list(filter(lambda x: len(tasks[x].Pre) == 0 and x not in in_progress_tasks, tasks.keys()))
    return avail_tasks


def log_task_info(workers: list[str], tasks: dict[str, Task], cur_time: int):
    info = "Current tasks: "
    for task_id in workers:
        if task_id:
            info += f"{task_id}: {tasks[task_id].Time}, "
    info += f"at time {cur_time}"
    log(info)


def solve_part2(lines, time_offset, num_workers):
    steps = parse_step_info(lines)
    tasks = create_tasks_from_steps(steps, time_offset)
    log(f"Tasks: {tasks}")

    workers = [""] * num_workers
    cur_time = -1
    while len(tasks.keys()) > 0:
        event = False
        # log(f"Workers {workers} at time {cur_time}")
        # log_task_info(workers, tasks)
        avail_tasks = sorted(find_avail_tasks(tasks, workers))
        # log(f"Available tasks: {avail_tasks}")
        for i in range(len(workers)):
            cur_task_id = workers[i]
            if cur_task_id:
                # worker has a current task, update the status of that task
                task = tasks[cur_task_id]
                if task.Time > 0:
                    task.Time -= 1
                else:
                    event = True
                    # task is finished after this round, update the task so at start of next round
                    # workers and tasks will be updated correctly
                    # log(f"Task is now finishing: {cur_task_id}")
                    task = tasks[cur_task_id]
                    for task_id in task.Post:
                        task = tasks[task_id]
                        task.Pre.remove(cur_task_id)
                    del tasks[cur_task_id]
                    workers[i] = ""
                    cur_task_id = workers[i]
                    avail_tasks = sorted(find_avail_tasks(tasks, workers))
                    # log(f"Available tasks: {avail_tasks}")

            # avail_tasks = sorted(find_avail_tasks(tasks, workers))
            # log(f"Available tasks: {avail_tasks}")
            if not cur_task_id and len(avail_tasks) > 0:
                event = True
                # log(f"Worker is not busy")
                cur_task_id = avail_tasks[0]
                workers[i] = cur_task_id
                avail_tasks = avail_tasks[1:]
                task = tasks[cur_task_id]
                task.Time -= 1
                # log(f"Workers {workers} added a task")

        cur_time += 1
        if (event):
            # log(f"Workers {workers} at time {cur_time}")
            log_task_info(workers, tasks, cur_time)
            # avail_tasks = sorted(find_avail_tasks(tasks, workers))
            # log(f"Available tasks: {avail_tasks}")

    # log(f"Workers {workers} at time {cur_time}")
    print(f"FINAL TIME: {cur_time}")


if __name__ == '__main__':
    main()
