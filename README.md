# Network Connectivity Test Script

This script is designed to test network connectivity and troubleshoot any issues that may arise. It allows end-users to run the script and communicate the test results to the system administrator. The script performs connectivity tests to the gateway, a remote IP address, and a URL to validate DNS resolution.

## Prerequisites

- CentOS 8
- Python 3

## Usage

1. Ensure that you have Python 3 installed on your CentOS 8.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:

   ```shell
   python3 network_connectivity_test.py
   ```

4. The script will display a menu with the following options:

   - Test connectivity to the gateway (Option 1)
   - Test remote connectivity (Option 2)
   - Test DNS resolution (Option 3)
   - Display gateway IP address (Option 4)

5. Enter the corresponding number for the test you want to perform.
6. The script will execute the selected test and provide the test result.

   - If the test is successful, it will display a success message.
   - If the test fails, it will display an error message.

7. After viewing the test result, you can choose another test or exit the script by entering 'Q' or 'q'.

## Script Details

The script utilizes the following Python modules:

- `subprocess`: Used to run shell commands.
- `socket`: Used to communicate with network connections.
- `os`: Used to perform system-related operations.

The script consists of the following functions:

- `gateway_connection()`: Tests connectivity to the gateway using the specified gateway address and port. It establishes a TCP connection and checks the connection result.
- `remote_connection()`: Tests remote connectivity by attempting to connect to a remote IP address (8.8.8.8) and port (443) using a socket. It checks if the connection was successful or not.
- `dns_resolution()`: Tests DNS resolution by resolving a hostname ("www.google.com") to an IP address using the `gethostbyname()` function. It verifies if the resolution was successful.
- `print_gateway()`: Retrieves and prints the default gateway IP address of the system by executing the "ip r" command and parsing the output.

The `run_code()` function is responsible for executing the appropriate test based on the user's input.

**Note:** The script clears the terminal screen upon execution for a better user experience.


## License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the script according to the terms of the license.

By utilizing this script, organizations can proactively identify potential security threats, analyze failed login attempts, and enhance their overall security infrastructure.
