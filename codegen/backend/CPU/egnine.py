from codegen.backend.CPU.numerics import OPERATIONS

def is_unary(op):
    func = OPERATIONS[op]
    try:
        return func.__code__.co_argcount == 1
    except AttributeError:
        return False

def fuse(vars, ops):
    def get_func_name(op): 
        func = OPERATIONS[op]
        return func.__name__ if callable(func) else str(func)

    vars = vars[:] 
    i = 0 
    j = 1

    expr = f"{vars[0]}"
    while i < len(ops):
        op = ops[i]
        func = get_func_name(op)
        if is_unary(op):
            expr = f"{func}({expr})"
        else:
            expr = f"{func}({expr}, {vars[j]})"
            j += 1
        i += 1

    return expr

def XLR(fn_out, debug=False):
    graph = fn_out.topo()
    exprs = {} 
    varnames = {}  
    input_count = 0

    for node in graph:
        if node.op == '':
            name = f"x_{input_count}"
            varnames[node] = name
            exprs[node] = name
            input_count += 1
        else:
            func = OPERATIONS[node.op]
            args = [exprs[inp] for inp in node.parents]
            expr = f"{func.__name__}({', '.join(args)})"
            exprs[node] = expr

    final_expr = exprs[graph[-1]]
    args = ', '.join(varnames[n] for n in graph if n in varnames)

    code = f"def fused({args}):\n"
    code += f"    return {final_expr}\n"

    scope = {func.__name__: func for func in OPERATIONS.values()}
    exec(code, scope)

    if debug:
        return scope['fused'], code
    else:
        return scope['fused']
