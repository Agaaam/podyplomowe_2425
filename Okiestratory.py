from tarfile import data_filter
from typing import Dict
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    PENDING = "pending" #Zadanie oczekujące na przetworzenie
    PROCESSING = "processing" #Zadanie w trakcie przetwarzania
    COMPLETING = "completing" #Zadanie przetworzone poprawnie
    FAILED = "failed" #Zadanie zakończone błędem

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __int__(self, task_id: str, data:Dict, priority: TaskPriority = TaskPriority.MEDIUM):
        self.tasks_id = task_id
        self.data = data
        self.status = TaskStatus.PENDING
        self.priority = priority
        self.created_at = datetime.now()