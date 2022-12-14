class Base:
    def __init__(self, name: str, git: str, time_update: str, command_run: str,) -> None:
        self.name = name
        self.git = git
        self.time_update = time_update
        self.com_run = command_run
    
    def generate_dict(self):
        return {
            self.name: {
                "git": self.git,
                "time_update": self.time_update,
                "command_run": self.com_run,
            }
        }
    
    def __str__(self) -> str:
        return f"{self.name}"
