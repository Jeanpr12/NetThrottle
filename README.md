# NetThrottle


---

## Overview

The Meraki Bandwidth Changer is a Python script that allows you to update bandwidth limits for a Meraki network group policy using the Meraki Dashboard API. With this script, you can easily modify download and upload speed limits for specific network policies, providing granular control over bandwidth allocation in your Meraki network.

## Features

- Update bandwidth limits for a specified Meraki network group policy.
- Choose from predefined bandwidth limit options or set custom limits.
- Receive feedback on the success or failure of bandwidth limit updates.

## Requirements

- Python 3.x
- `meraki` Python library

## Usage

1. **Installation**:
   - Install the `meraki` library if you haven't already:

     ```
     pip install meraki
     ```

2. **Configuration**:
   - Open the script (`bandwidth_changer.py`) in a text editor.
   - Replace `"value"` placeholders in the script with your actual Meraki API key, network ID, and group policy ID.

3. **Run the Script**:
   - Execute the script using the following command:

     ```
     python bandwidth_changer.py
     ```

4. **Choose Bandwidth Limit**:
   - Follow the prompts to select a bandwidth limit option:
     - `1`: 30 Kbps Download & Upload
     - `2`: 100 Kbps Download, 30 Kbps Upload
     - `3`: No Limits
     - `4`: 100 Kbps Upload, 30 Kbps Download
     - `0`: Exit

5. **View Feedback**:
   - After selecting an option, the script will provide feedback on the success or failure of the bandwidth limit update.

## Notes

- Ensure that your Meraki API key has the necessary permissions to update network group policies.
- Verify that the provided network ID and group policy ID correspond to your Meraki dashboard configuration.

