from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime

class JobRepository(ABC):
    @abstractmethod
    def save(self, jobs: List[Dict]) -> None:
        pass
    @abstractmethod
    def get_recent(self, search_terms: str, location: str) -> List[Dict]:
        pass
