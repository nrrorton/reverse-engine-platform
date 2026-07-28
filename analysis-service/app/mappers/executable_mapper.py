from app.models.executable import Executable as DomainExecutable
from app.schemas.analysis import ExecutableInfo



class ExecutableMapper:

    def map_executable(self, executable: DomainExecutable) -> ExecutableInfo:

        return ExecutableInfo(
            name=executable.name,
            architecture=executable.architecture,
            entry_point_rva=executable.entry_point_rva,
            sha256=executable.sha256
        )