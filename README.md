# LSP-cmake

This is a helper package that automatically installs and updates a
[CMake Language Server](https://github.com/muffinmad/cmake-language-server) for you.

To use this package, you must have the [LSP](https://packagecontrol.io/packages/LSP) package installed as well.

## Applicable Selectors

This language server operates on views with the `source.cmake` base scope.

## Installation Location

The server is installed in the $DATA/Cache/LSP-cmake directory, where $DATA is the base data path of Sublime Text.
For instance, $DATA is `~/.config/sublime-text` on a Linux system. If you want to force a re-installation of the server,
you can delete the entire $DATA/Cache/LSP-cmake directory. The installation is done through a virtual environment,
using pip. Therefore, you must have at least the `python` executable installed and it must be present in your $PATH.

Like any helper package, installation starts when you open a view that is suitable for this language server. In this
case, that means that when you open a view with the `source.cmake` base scope, installation commences.

## Configuration

Configure the Python Language Server by accessing `Preferences > Package Settings > LSP > Servers > LSP-cmake`.

This language servers provides a few basic services like hover info and formatting.
