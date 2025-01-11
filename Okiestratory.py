from typing import Dict
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    PENDING = "pending"         # Zadanie oczekujące na przetworzenie
    PROCESSING = "processing"   # Zadanie w trakcie przetwarzania
    COMPLETING = "completing"   # Zadanie przetworzone poprawnie
    FAILED = "failed"           # Zadanie zakończone błędem

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self, task_id: str, data: Dict, priority: TaskPriority = TaskPriority.MEDIUM):
        self.task_id = task_id #Unikalny identyfikator zadania
        self.data = data #Dane wejściowe
        self.status = TaskStatus.PENDING #Początkowy status
        self.priority = priority #Priorytet zadania
        self.createt_at = datetime.now() #Odcisk czasu utworzenia zadania
        self.error = None #Miejsce na przechowywanie ewentualnych błędów


# task = Task("test", {"pole1": 3, "pole2": "alamakota"})
# print(task.priority)
