import random
import datetime

# Define possible values for certain fields
actions = ["login", "logout", "failed_login"]
apps = ["web_app", "ssh", "vpn", "email"]
authentication_methods = ["password", "2fa", "certificate"]
destinations = ["server1", "server2", "server3"]
dest_bunits = ["IT", "HR", "Finance"]
dest_categories = ["server", "workstation", "network"]
# Add more possible values for other fields as needed

# Generate random authentication logs
num_logs = 10  # You can change this to the number of logs you want to generate

for _ in range(num_logs):
    log = {
        "action": random.choice(actions),
        "app": random.choice(apps),
        "authentication_method": random.choice(authentication_methods),
        "dest": random.choice(destinations),
        "dest_bunit": random.choice(dest_bunits),
        "dest_category": random.choice(dest_categories),
        "dest_nt_domain": f"nt_domain_{random.randint(1, 10)}",
        "dest_priority": random.randint(1, 5),
        "duration": random.randint(1, 60),
        "reason": "success" if random.random() < 0.8 else "failure",
        "response_time": random.uniform(0.1, 2.0),
        "signature": f"signature_{random.randint(1000, 9999)}",
        "signature_id": random.randint(100, 999),
        "src": f"src_{random.randint(1, 10)}",
        "src_bunit": random.choice(dest_bunits),
        "src_category": random.choice(dest_categories),
        "src_nt_domain": f"nt_domain_{random.randint(1, 10)}",
        "src_priority": random.randint(1, 5),
        "src_user": f"user_{random.randint(1, 100)}",
        "src_user_bunit": random.choice(dest_bunits),
        "src_user_category": random.choice(dest_categories),
        "src_user_id": random.randint(1000, 9999),
        "src_user_priority": random.randint(1, 5),
        "src_user_role": random.choice(["admin", "user"]),
        "src_user_type": random.choice(["employee", "contractor"]),
        "tag": f"tag_{random.randint(1, 5)}",
        "user": f"user_{random.randint(1, 100)}",
        "user_agent": f"user_agent_{random.randint(1, 10)}",
        "user_bunit": random.choice(dest_bunits),
        "user_category": random.choice(dest_categories),
        "user_id": random.randint(1000, 9999),
        "user_priority": random.randint(1, 5),
        "user_role": random.choice(["admin", "user"]),
        "user_type": random.choice(["employee", "contractor"]),
        "vendor_account": f"vendor_account_{random.randint(1, 10)}",
    }

    # Add timestamp field with current time
    log["timestamp"] = datetime.datetime.now().isoformat()

    # You can print or save the log in your desired format
    print(log)

