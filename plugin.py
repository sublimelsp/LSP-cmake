from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import UvVenvManager
from sublime_lib import ResourcePath
from typing_extensions import override


class Cmake(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        UvVenvManager.on_pre_start_async(
            context, cls.plugin_storage_path, ResourcePath('Packages', package_name, 'server'), 'cmake-language-server')


def plugin_loaded() -> None:
    Cmake.register()


def plugin_unloaded() -> None:
    Cmake.unregister()
