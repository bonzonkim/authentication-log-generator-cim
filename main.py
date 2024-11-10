import random
import datetime

# Define possible values for certain fields
actions = ["success", "failure", "pending", "error"]
apps = ["web_app", "ssh", "vpn", "email"]
authentication_methods = ["password", "2fa", "certificate"]
destinations = ["server1", "server2", "server3"]
dest_bunits = ["IT", "HR", "Finance"]
dest_categories = ["server", "workstation", "network"]
# Add more possible values for other fields as needed

# Generate random authentication logs
num_logs = 200000  # You can change this to the number of logs you want to generate

def generate_log():
    random_generator = random.SystemRandom()
    log_entries = []

    for _ in range(num_logs):
        action = random_generator.choice(actions)
        app = random_generator.choice(apps)
        authentication_method = random_generator.choice(authentication_methods)
        dest = random_generator.choice(destinations)
        dest_bunit = random_generator.choice(dest_bunits)
        dest_category = random_generator.choice(dest_categories)
        dest_nt_domain = f"nt_domain_{random_generator.randint(1, 10)}"
        dest_priority = random_generator.randint(1, 5)
        duration = random_generator.randint(1, 60)
        reason = "success" if random_generator.random() < 0.8 else "failure"
        response_time = random_generator.uniform(0.1, 2.0)
        signature = f"signature_{random_generator.randint(1000, 9999)}"
        signature_id = random_generator.randint(100, 999)
        src = f"src_{random_generator.randint(1, 10)}"
        src_bunit = random_generator.choice(dest_bunits)
        src_category = random_generator.choice(dest_categories)
        src_nt_domain = f"nt_domain_{random_generator.randint(1, 10)}"
        src_priority = random_generator.randint(1, 5)
        src_user = f"user_{random_generator.randint(1, 100)}"
        src_user_bunit = random_generator.choice(dest_bunits)
        src_user_category = random_generator.choice(dest_categories)
        src_user_id = random_generator.randint(1000, 9999)
        src_user_priority = random_generator.randint(1, 5)
        src_user_role = random_generator.choice(["admin", "user"])
        src_user_type = random_generator.choice(["employee", "contractor"])
        tag = f"tag_{random_generator.randint(1, 5)}"
        user = f"user_{random_generator.randint(1, 100)}"
        user_agent = f"user_agent_{random_generator.randint(1, 10)}"
        user_bunit = random_generator.choice(dest_bunits)
        user_category = random_generator.choice(dest_categories)
        user_id = random_generator.randint(1000, 9999)
        user_priority = random_generator.randint(1, 5)
        user_role = random_generator.choice(["admin", "user"])
        user_type = random_generator.choice(["employee", "contractor"])
        vendor_account = f"vendor_account_{random_generator.randint(1, 10)}"
        timestamp = datetime.datetime.now().isoformat()

        log_entry = (
            f"{action} | {app} | {authentication_method} | {dest} | {dest_bunit} | {dest_category} | {dest_nt_domain} | {dest_priority} "
            f"{duration} | {reason} | {response_time} | {signature} | {signature_id} | {src} | {src_bunit} | {src_category} | {src_nt_domain} | {src_priority} "
            f"{src_user} | {src_user_bunit} | {src_user_category} | {src_user_id} | {src_user_priority} | {src_user_role} | {src_user_type} | {tag} | {user} | {user_agent} | {user_bunit} | {user_category} | {user_id} | {user_priority} | {user_role} | {user_type} | {vendor_account} | {timestamp}\n"
        )

        log_entries.append(log_entry)

    return log_entries

# change the first parameter of open() to change the name of the log file.
with open("generated_auth_logs.log", "w") as file:
    log_entries = generate_log()
    file.writelines(log_entries)

