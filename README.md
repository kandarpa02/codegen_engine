# codegen engine


![Alt text](levi_chibi.jpeg)

this is a helper repo for deriv library [text](https://github.com/kandarpa02/py-deriv.git)
**codegen engine** only works with `deriv.array` object, it fuses a python function which takes `deriv.array`, to run code with minimum python overhead

- minimal explanation
```python
from codegen.backend.CPU.egnine import XLR
from deriv import array

x = array(4)
y = array(5)
z = array(2)

def func(x, y, z):
    g = x + y
    h = (g) * z
    return h

f2, code = XLR(func(x, y, z), debug=True) # debug = True to return the generated function

print(code)

# output: 
# def fused(x_0, x_1, x_2):
#     return mult(addt(x_0, x_1), x_2)

print(f2(x, y, z))

# output:
# array(18, grad_fn=<mul_back>, need_grad=True)

```