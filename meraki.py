import meraki

API_KEY = "value"
NETWORK_ID = "value"
GROUP_POLICY_ID = "value"

dashboard = meraki.DashboardAPI(API_KEY)

def update_bandwidth_limits(limit_up, limit_down):
    try:
        if limit_up is None and limit_down is None:
            bandwidth_settings = "unlimited"
        else:
            bandwidth_settings = "custom"
        response = dashboard.networks.updateNetworkGroupPolicy(
            NETWORK_ID,
            GROUP_POLICY_ID,
            bandwidth={
                "settings": bandwidth_settings,
                "bandwidthLimits": {"limitUp": limit_up, "limitDown": limit_down},
            },
        )
        print("Bandwidth limits updated successfully.")
    except meraki.APIError as e:
        print(f"Failed to update bandwidth limits: {e}")

def choose_bandwidth_limit():
    print("Select a bandwidth limit option:")
    print("1. 30 Kbps Download & Upload")
    print("2. 100 Kbps Download, 30 Kbps Upload")
    print("3. No Limits")
    print("4. 100 Kbps Upload, 30 Kbps Download")
    print("0. Exit")
    
    while True:
        choice = input("Enter the number of your choice (0-4): ")
        
        if choice == "1":
            update_bandwidth_limits(20, 20)
        elif choice == "2":
            update_bandwidth_limits(20, 900000)
        elif choice == "3":
            update_bandwidth_limits(900000, 900000)
        elif choice == "4":
            update_bandwidth_limits(100000, 20)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option (0-4).")

if __name__ == "__main__":
    choose_bandwidth_limit()