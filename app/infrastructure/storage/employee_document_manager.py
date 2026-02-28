from pathlib import Path

class EmployeeDocumentManager:

    folders = [
        "medicals",
        "mutuelle",
        "prevoyance",
        "contracts",
        "legal",
        "disciplinary",
        "it_charts",
        "images_rights",
        "identity"
        
    ]
    
    def __init__(self, base_path: str ):
        self.base_path = Path(base_path)

    def create_workspace(self, token: str) -> str:
        employee_root = self.base_path / token
        employee_root.mkdir(parents=True, exist_ok=True)

        for folder in self.folders:
            (employee_root/folder).mkdir(parents=True, exist_ok=True)

        return employee_root