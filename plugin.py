from lsp_utils.pip_client_handler import PipClientHandler


class Cmake(PipClientHandler):
    package_name = __package__
    requirements_txt_path = "requirements.txt"
    server_filename = "cmake-language-server"

    @classmethod
    def get_displayed_name(cls) -> str:
        return "cmake"


def plugin_loaded() -> None:
    Cmake.setup()


def plugin_unloaded() -> None:
    Cmake.cleanup()
