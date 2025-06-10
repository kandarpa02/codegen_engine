import cupy as cp
from deriv import array

def addt(a, b): return a + b
def mult(a, b): return a * b
def subt(a, b): return a - b
def div(a, b): return a / b
def powr(a, b): return a ** b
def matmul(a, b): return a @ b
def relu(a): return array(cp.maximum(a.data, 0))
def tanh(a): return array(cp.tanh(a.data))
def sigmoid(a): return array(1/(1+cp.exp(-a.data)))

OPERATIONS = {

    '+': addt,
    '*': mult,
    '-': subt,
    '/': div,
    '**': powr,
    '@': matmul,
    'relu': relu,
    'tanh': tanh,
    'sigmoid': sigmoid

}