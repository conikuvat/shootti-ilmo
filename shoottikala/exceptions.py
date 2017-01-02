from safespace.excs import Problem


class AccessDenied(Problem):
    code = 403
    title = 'Access denied'
