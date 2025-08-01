class AdminText:
    ADMIN_REMOVED = """
Admin removed
"""
    ADMIN_NOT_EXISTS = """
Admin not exists
"""
    ADMIN_LIST_EMPTY = """
Admin list is empty
"""
    ADMIN_ALREADY_EXISTS = """
Admin already exists
"""
    START = """
Welcome to admin panel

Base Commands:
/admin - Admin panel
/user_stat - User statistics 

Admin Manager Commands (Only for base admins):
/add_admin {telegram_id} - Add admin
/admin_list - List of admins
/remove_admin {telegram_id} - Remove admin
"""
