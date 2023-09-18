# Python + WASI with Nix

This is an attempt at using Nix to create a local development environment for the WASI build of Python.

## Try it out

Assuming you already have Nix installed with flakes enabled.

1. Clone the repo
   ```
   $ git clone https://github.com/alcarney/python-wasi-nix
   $ cd python-wasi-nix
   ```

1. Activate the `devShell`
   ```
   $ nix develop
   ```

1. Run the script
   ```
   $ python main.py
   sys.platform='wasi'
   {'line': 1, 'character': 42}
   ```

## Resources

- [Setting up a Python WASI Environment with Nix](https://www.alcarney.me/blog/2023/python-wasi-nix/): The blog post outlining how the Nix parts of this repo work
- [Testing a Python project using the WASI build of CPython with pytest](https://snarky.ca/testing-a-project-using-the-wasi-build-of-cpython-with-pytest/): The blog post that covers the Python + WASI part of this repo
- [WebAssembly and its platform targets](https://snarky.ca/webassembly-and-its-platform-targets/): Overview of the different WebAssembly runtimes

## TODO

This is "good enough" for me to start hacking on the WASI runtime, but there's certainly plenty that could potnetially be improved.

- Building Python WASI from source
- Automatically choosing the right Python package set to use with ``mkPythonWASIShell``, like ``python.withPackages``
- Extending ``mkPythonWASIShell`` to allow the user to set the permissions for the Python process
- Overriding a base ``python`` derivation so that packages are built against this version of Python.
- Extending this to work with packages that contain native modules?
