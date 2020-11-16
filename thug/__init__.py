__version__            = "1.16"
__jsengine__           = ""
__jsengine_version__   = ""
__configuration_path__ = "/etc/thug"


try:
    import STPyV8

    __jsengine__         = "STPyV8"
    __jsengine_version__ = getattr(STPyV8, "__version__", "")
except ImportError: # pragma: no cover
    pass
