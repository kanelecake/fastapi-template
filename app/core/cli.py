import argparse


class CLIArgs:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Configuration arguments for the app")
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument("--config", type=str, required=True, help="Path to the YAML config file")
        # Добавьте другие аргументы, которые хотите обрабатывать

    def parse(self):
        return self.parser.parse_args()


_cli_args = CLIArgs()
cli_args = _cli_args.parse()