import os
import shutil
import subprocess
import re

import sublime
from LSP.plugin import AbstractPlugin
from LSP.plugin.core.typing import Any, Dict


class Cmake(AbstractPlugin):
    @classmethod
    def name(cls) -> str:
        return "cmake"

    @classmethod
    def basedir(cls) -> str:
        return os.path.join(cls.storage_path(), "LSP-cmake")

    @classmethod
    def bindir(cls) -> str:
        dirname = "Scripts" if sublime.platform() == "windows" else "bin"
        return os.path.join(cls.basedir(), dirname)

    @classmethod
    def server_exe(cls) -> str:
        return os.path.join(cls.bindir(), "cmake-language-server")

    @classmethod
    def pip_exe(cls) -> str:
        return os.path.join(cls.bindir(), "pip")

    @classmethod
    def version_str(cls) -> str:
        settings = sublime.load_settings("LSP-cmake.sublime-settings")
        return str(settings.get("version"))

    @classmethod
    def python_exe(cls) -> str:
        return "python" if sublime.platform() == "windows" else "python3"

    @classmethod
    def run(cls, *args: Any, **kwargs: Any) -> bytes:
        if sublime.platform() == "windows":
            startupinfo = subprocess.STARTUPINFO()  # type: ignore
            flag = subprocess.STARTF_USESHOWWINDOW  # type: ignore
            startupinfo.dwFlags |= flag
        else:
            startupinfo = None
        return subprocess.check_output(args=args, cwd=kwargs.get("cwd"), startupinfo=startupinfo)

    @classmethod
    def needs_update_or_installation(cls) -> bool:
        if os.path.exists(cls.server_exe()):
            first_line = cls.run(cls.server_exe(), "--version").decode("ascii").splitlines()[0]
            match = re.search(r"cmake-language-server (.+)", first_line)
            if match:
                current_version_str = match.group(1)
                return current_version_str != cls.version_str()
        return True

    @classmethod
    def install_or_update(cls) -> None:
        shutil.rmtree(cls.basedir(), ignore_errors=True)
        try:
            os.makedirs(cls.basedir(), exist_ok=True)
            cls.run(cls.python_exe(), "-m", "venv", "LSP-cmake", cwd=cls.storage_path())
            cmake = "cmake-language-server=={}".format(cls.version_str())
            cls.run(cls.pip_exe(), "install", "--disable-pip-version-check", cmake)
        except Exception:
            shutil.rmtree(cls.basedir(), ignore_errors=True)
            raise

    @classmethod
    def additional_variables(cls) -> Dict[str, str]:
        return {
            'server_binary': cls.server_exe()
        }
