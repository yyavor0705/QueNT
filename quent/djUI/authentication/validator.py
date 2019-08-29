def company_admin_required(view_function, *args):
    request = args[0]
    return view_function(*args)
