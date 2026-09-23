SENSITIVE_ACTIONS = {"delete_file", "send_email", "purchase", "install_software"}

def requires_confirmation(action: str) -> bool:
    return action in SENSITIVE_ACTIONS
