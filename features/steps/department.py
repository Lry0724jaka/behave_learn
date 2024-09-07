from collections import defaultdict

# Given - 初始化用户集合
@given('a set of specific users')
def step_impl(context):
    context.users = context.table.rows
    for user in context.users:
        print(f"User: {user['name']}, Department: {user['department']}")

# When - 计数每个部门的人数
@when('we count the number of people in each department')
def step_impl(context):
    department_count = defaultdict(int)
    for user in context.users:
        department_count[user['department']] += 1
    context.department_count = department_count
    print("Counting people in each department")

# Then - 验证部门人数
@then('we will find two people in "{department}"')
def step_impl(context, department):
    assert context.department_count[department] == 2, f"Expected 2 people in {department}, but found {context.department_count[department]}"

@then('we will find one person in "{department}"')
def step_impl(context, department):
    assert context.department_count[department] == 1, f"Expected 1 person in {department}, but found {context.department_count[department]}"