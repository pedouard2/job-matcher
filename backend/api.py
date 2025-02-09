from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class JobAPI(ABC):
    @abstractmethod
    def search_jobs(
        self, search_terms: Optional[str], location: Optional[str]
    ) -> List[Dict]:
        pass
