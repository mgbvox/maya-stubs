import site
import sysconfig
from pathlib import Path


def ensure_maya() -> None:
    maya_stdlib = Path(sysconfig.get_path("stdlib"))
    site.addsitedir(str(maya_stdlib / "site-packages"))

    try:
        import maya  # type: ignore[reportUnusedImport,unused-ignore]
    except ModuleNotFoundError as e:
        raise RuntimeError(
            "could not import maya module; ensure you're using mayapy as "
            "the base interpreter for your virtual environment"
        ) from e


def main() -> None:
    ensure_maya()
    from .cli import cli

    cli()


if __name__ == "__main__":
    main()
