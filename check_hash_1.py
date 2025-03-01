import subprocess
import sys

def check_sha256(filename, expected_hash):
    try:
        # Run the sha256sum command
        result = subprocess.run(
            ["sha256sum", filename],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Extract the actual hash value
        actual_hash = result.stdout.split()[0]

        # Check if actual hash matches the expected hash
        if actual_hash == expected_hash:
            print("Match: true")
            return True
        else:
            print("Match: false")
            return False

    except subprocess.CalledProcessError as e:
        print(f"Error executing sha256sum: {e}")
        return False
    except FileNotFoundError:
        print("Error: sha256sum command not found.")
        return False
    except IndexError:
        print("Error: Could not parse hash output.")
        return False

if __name__ == "__main__":
    # Get filename as argument or input
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter filename: ").strip()

    # Get expected hash from argument or prompt for input
    if len(sys.argv) > 2:
        expected_hash = sys.argv[2]
    else:
        expected_hash = input("Enter expected SHA-256 hash: ").strip()

    if not filename or not expected_hash:
        print("Error: Filename and hash value are required.")
        sys.exit(1)

    if check_sha256(filename, expected_hash):
        sys.exit(0)  # Exit with success status
    else:
        sys.exit(1)  # Exit with failure status
