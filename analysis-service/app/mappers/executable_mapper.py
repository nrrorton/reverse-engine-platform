from app.models.executable import Executable as DomainExecutable
from app.schemas.analysis import ExecutableInfo



class ExecutableMapper:

    def map_executable(self, executable: DomainExecutable) -> ExecutableInfo:

        return ExecutableInfo(
            name=executable.name,
            architecture=executable.architecture,
            entry_point_rva=(
                hex(executable.entry_point_rva)
                if executable.entry_point_rva is not None
                else None),
            sha256=executable.sha256
        )