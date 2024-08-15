from .sprinkles import Sprinkles


def print_help() -> None:
    print(
        "\n\r"
        "Usage: vt <option>"
        "\n\r"
        "Example: vt pack transport development => Compile, transport and set the Vite environment to development"
        "\n\r\n\r"
        f" {Sprinkles.OKCYAN}list, ls{Sprinkles.END} => List all vite apps in pyproject.toml"
        "\n\r"
        f" {Sprinkles.OKCYAN}update{Sprinkles.END} => Attempt to npm update all vite apps"
        "\n\r"
        f" {Sprinkles.OKCYAN}pack{Sprinkles.END} => Attempt to compile all vite apps"
        "\n\r"
        f" {Sprinkles.OKCYAN}transport{Sprinkles.END} => Transport all vite apps to the serving app"
        "\n\r"
        f" {Sprinkles.OKCYAN}production{Sprinkles.END} => (DEFAULT) Set the Vite environment (env.MODE) to production"
        "\n\r"
        f" {Sprinkles.OKCYAN}staging{Sprinkles.END} => Set the Vite environment (env.MODE) to staging"
        "\n\r"
        f" {Sprinkles.OKCYAN}development{Sprinkles.END} => Set the Vite environment (env.MODE) to development"
        "\n\r"
        f" {Sprinkles.OKCYAN}-h, --help, help{Sprinkles.END} => Show the help message and exit"
        "\n\r"
        f" {Sprinkles.OKCYAN}-v, --version, version{Sprinkles.END} => Show the version and exit"
    )
    print("")