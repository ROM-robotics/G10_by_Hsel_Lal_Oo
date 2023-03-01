### sympy

# e, pi, oo

```
>>> x = sp.Symbol('x')
>>> x
x
>>> x+1
x + 1
```

# equal sign x+1=4 ERROR
sympy.Eq(x+1, 4)

# simplify
a = (x+1)**2
b = x**2 + 2*x + 1
symby.simplify(a-b)

# rational 
sympy.Rational(1,2)

# numpy.sqrt(3) is 2.82842..
sympy.sqrt(3)

x,y = sympy.symbols('x y')
expression = x+2*y

x*expression

exp_expression = sympy.expand(x*expression)

factor_expression = sympy.expression(exp_expression)

# take the deriviative of sin(x) e^x
diff_x =sympy.diff(sin(x)*exp(x), x)

# compute integral of diff_x
sympy.integrate(diff_x)

sympy.integrate(sin(x**2), (x,-oo,oo))

# find limx-->0 , sin(x)/x
sympy.limit(sin(x)/x, x, 0)

# solve x**2 - 2 = 0
sympy.solve(x**2 - 2, x)

# solve the differential equation y**'' - y = e**t
y = Function('y')
sympy.dsolve( Eq( y(t).diff(t,t) - y(t), exp(t) ), y(t) ) 

# find eigen values of Matrix[1 2; 2 2]
sympy.Matrix([[1,2],[2,2]]).eigenvals()





 
