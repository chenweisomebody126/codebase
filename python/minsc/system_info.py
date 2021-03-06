import sys
import pkg_resources
import importlib
import os

def get_python_version():
    """Get the system's python version.
    Returns:
        version (str): Python version.
    Examples:
        >>> get_python_version()
        '2.7.12 |Anaconda 4.0.0 (64-bit)| (default, Jun 29 2016, 11:07:13) [MSC v.1500 64 bit (AMD64)]'
        
    """
    return sys.version


def get_library_version(library_name):
    """Get the version of a library.
    Parameters:
        library_name (str): Name of the library.
    Returns:
        version (str): Version of the library.
    Examples:
        >>> get_library_version("pandas")
        '0.19.2'
       
    """
    try:
        version = pkg_resources.get_distribution(library_name).version
    except Exception:
        pass
    try:
        lib = importlib.import_module(library_name)
        version = lib.__version__
    except Exception as e:
        print(e)

    return version


def get_number_processors():
    """Get the number of processors in a CPU.
    Returns:
        num (int): Number of processors.
    Examples:
        >>> get_number_processors()
        4

    """
    try:
        num = os.cpu_count()
    except:
        import multiprocessing #force exception in case mutiprocessing is not installed
        num = multiprocessing.cpu_count()
    return num


def get_java_version():
    """Get java version, vendor, installation files and more information
    Examples:
        >>> get_java_version()

    """
    os.system('java -XshowSettings:properties -version')



