import sys
sys.path.append('..')
from main import calculate_project_hours

def test_calculate_project_hours():
    tasks = [
        {'name': 'Task 1', 'hours': 5},
        {'name': 'Task 2', 'hours': 3}
    ]
    assert calculate_project_hours(tasks) == 8
    print("Тест пройден!")

if __name__ == "__main__":
    test_calculate_project_hours()