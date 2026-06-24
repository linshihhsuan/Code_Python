# Smart Task Command Interpreter
# 使用 match-case 實作任務管理系統

tasks = {}


def show_task(task_id, task):
    print(
        f"{task_id} | "
        f"Priority: {task['priority']} | "
        f"Status: {task['status']} | "
        f"{task['description']}"
    )


def list_tasks(task_items):
    if not task_items:
        print("No tasks found.")
        return

    for task_id, task in task_items:
        show_task(task_id, task)


def show_help():
    print("""
Available commands:

add <task_id> <priority> <description>
done <task_id>
remove <task_id>
list all
list pending
list done
list priority <priority>
search <keyword>
update <task_id> priority <new_priority>
help
exit
""")


while True:
    command = input("Enter command: ").strip()
    parts = command.split()

    match parts:

        # add T001 3 finish Python homework
        case ["add", task_id, priority_str, *description_words] \
            if priority_str.isdigit() and 1 <= int(priority_str) <= 5 and description_words:

            if task_id in tasks:
                print(f"Error: Task {task_id} already exists.")
            else:
                tasks[task_id] = {
                    "priority": int(priority_str),
                    "description": " ".join(description_words),
                    "status": "pending"
                }
                print(f"Task {task_id} added.")

        # add 指令格式錯誤或 priority 不合法
        case ["add", *_]:
            print("Invalid add command.")
            print("Format: add <task_id> <priority 1-5> <description>")

        # done T001
        case ["done", task_id]:
            if task_id in tasks:
                tasks[task_id]["status"] = "done"
                print(f"Task {task_id} marked as done.")
            else:
                print(f"Error: Task {task_id} does not exist.")

        # remove T001
        case ["remove", task_id]:
            if task_id in tasks:
                del tasks[task_id]
                print(f"Task {task_id} removed.")
            else:
                print(f"Error: Task {task_id} does not exist.")

        # list all
        case ["list", "all"]:
            list_tasks(tasks.items())

        # list pending
        case ["list", "pending"]:
            pending_tasks = [
                (task_id, task)
                for task_id, task in tasks.items()
                if task["status"] == "pending"
            ]
            list_tasks(pending_tasks)

        # list done
        case ["list", "done"]:
            done_tasks = [
                (task_id, task)
                for task_id, task in tasks.items()
                if task["status"] == "done"
            ]
            list_tasks(done_tasks)

        # list priority 5
        case ["list", "priority", priority_str] \
            if priority_str.isdigit() and 1 <= int(priority_str) <= 5:

            priority = int(priority_str)
            priority_tasks = [
                (task_id, task)
                for task_id, task in tasks.items()
                if task["priority"] == priority
            ]
            list_tasks(priority_tasks)

        # list priority 指令錯誤
        case ["list", "priority", *_]:
            print("Invalid priority. Priority must be an integer from 1 to 5.")

        # search final
        case ["search", keyword]:
            keyword = keyword.lower()

            matched_tasks = [
                (task_id, task)
                for task_id, task in tasks.items()
                if keyword in task["description"].lower()
            ]

            list_tasks(matched_tasks)

        # update T002 priority 2
        case ["update", task_id, "priority", new_priority_str] \
            if new_priority_str.isdigit() and 1 <= int(new_priority_str) <= 5:

            if task_id in tasks:
                tasks[task_id]["priority"] = int(new_priority_str)
                print(f"Task {task_id} priority updated to {new_priority_str}.")
            else:
                print(f"Error: Task {task_id} does not exist.")

        # update 指令格式或 priority 錯誤
        case ["update", *_]:
            print("Invalid update command.")
            print("Format: update <task_id> priority <new_priority 1-5>")

        # help
        case ["help"]:
            show_help()

        # exit
        case ["exit"]:
            print("Goodbye!")
            break

        # 空輸入
        case []:
            print("Please enter a command.")

        # 其他無效指令
        case _:
            print("Invalid command. Type 'help' to see available commands.")