def validate_hook(hook: str) -> bool:
    if len(hook.split()) < 5:
        return True
    if "this chapter" in hook.lower():
        return True
    if len(hook.split()) > 35:
        return True
    return False
