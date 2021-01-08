from cx_Freeze import setup, Executable

setup(
    name = "LBRY TOOLS",
    version = "0.1",
    description = "",
    executables = [Executable("install.py", base="Win32GUI")],
)
