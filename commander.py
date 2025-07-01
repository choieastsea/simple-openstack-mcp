import subprocess


class OpenStackCommander:
    @staticmethod
    def execute(command: str, timeout: int = 60) -> str:
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True, timeout=timeout
            )
            return result.stdout.strip()
        except Exception as e:
            return str(e)
