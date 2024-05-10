
import sys

print("Original sys.path:")
print(sys.path)


new_path = '/path/to/new_directory'
sys.path.append(new_path)


print("\nModified sys.path:")
print(sys.path)


try:
    import test_module
    print("Module imported successfully.")
except ImportError:
    print("Failed to import module from the new directory.")


sys.path.remove(new_path)


print("\nRestored sys.path:")
print(sys.path)