from typing import Protocol, runtime_checkable
from entities import Student, Course, Department

@runtime_checkable
class ReportGenerator(Protocol):
    def generate(self, data: list, title: str) -> None:
        pass

class ConsoleReport:
    def generate(self, data: list, title: str) -> None:
        print(f"\n=== {title} ===")
        if not data:
            print("No data available.")
            return
        for item in data:
            print(item)

class CSVReport:
    def generate(self, data: list, title: str) -> None:
        import csv
        filename = f"{title.lower().replace(' ', '_')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = writer(f)
            writer.writerow(['ID', 'Name'])
            for item in data:
                if isinstance(item, Student):
                    writer.writerow([item.student_id, item.name])
                elif isinstance(item, Course):
                    writer.writerow([item.course_id, item.title])
                elif isinstance(item, Department):
                    writer.writerow([item.dept_id, item.name])
        print(f"Report saved to {filename}")