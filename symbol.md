##### sympy
```
>>> import numpy as np
>>> import sympy as sp
```
sympy အသုံးပြုပြီး သင်ချာဆိုင်ရာဖေါ်ပြချက်တွေအတွက် symbolic ကို သုံးနိုင်တယ်။ 

```
>>> x = sp.Symbol('x')
>>> x
x
>>> x+1
x + 1
```
constant တွေဖြစ်တဲ့ e, pi, oo ( infinity ) တို့ကိုလည်းသုံးနိင်တယ်။
```
>>> sp.exp
exp
>>> sp.oo
oo
>>> sp.pi
pi
```
equal sign ကို သုံးဖို့ အတွက် >>> x+1=4 လို့သုံးရင် error ဖြစ်ပါတယ်။
```
>>> equation_1 = sp.Eq(x+1, 4)
>>> equation_1 
Eq(x + 1, 4)
```
အထက်ပါ x+1 = 4 ကိုဖြေရှင်းဖို့ကတော့ solve()
``` 
>>> sp.solve(equation_1)
[3]
```
x^2 - 2 = 0 ဆိုရင် x = ?
```
>>> sp.solve(x**2 -2, x)
[-sqrt(2), sqrt(2)]
```
solve မလုပ်ဘဲ simplify လည်းလုပ်နိုင်တယ်။
```
>>> a = (x+1)**2
>>> b = x**2 + 2*x + 1
>>> sp.simplify(a-b)
0
```
အချိုး( Rational ) ကိန်းများလဲ အသုံးပြုနိုင်တယ်။ 
```
>>> sp.Rational(1,2)
1/2
```
numpy မှာဆိုရင် square root of 8 သည် 2.82842.. ရပေမဲ့ sympy.sqrt() မှာတော့ အောက်ပါအတိုင်းသင်ချာပုံစံရနိုင်တယ်။
```
>>> np.sqrt(8)
2.8284271247461903
>>> sp.sqrt(8)
2*sqrt(2)
```
Symbols တွေသုံးပြီး equations တချို့ရှင်းကြည့်ရအောင်
```
>>> x,y = sp.symbols('x y')
>>> expression = x+2*y
>>> x * expression
x*(x + 2*y)
```
 expand() နဲ့ ဖြန့်ရေးမယ်။
```
>>> exp_express = sp.expand(x * expression)
>>> exp_express
x**2 + 2*x*y
```
factor() နဲ့ ဆခွဲကိန်းပြန်ခွဲမယ်။
```
>>> fac_express = sp.factor(exp_express)
>>> fac_express
x*(x + 2*y)
```
 sin(x) e^x ကို ရှိတ်ရအောင်။
```
diff_x =sympy.diff(sin(x)*exp(x), x)
```
ရှိတ်ထားတာကို ပြန်ရိတ်မယ်။
```
sympy.integrate(diff_x)
```
သီးခြားထပ် ရိတ်ကြည့်မယ်။
```
sympy.integrate(sin(x**2), (x,-oo,oo))
```
လစ်မစ် x ဟာ 0 ကိုချဥ်းကပ်သွားတဲ့အခါ ဖန်ရှင်ကဘာဖြစ်မလဲ?
```
# find limx-->0 , sin(x)/x
sympy.limit(sin(x)/x, x, 0)
```
y**'' - y = e**t , y နှစ်ခုရှိတ်တဲ့အထဲက y နှုတ်ရင် e^t ရတယ်ဆိုတဲ့ differential equation ကိုရှင်းဖို့ဆို dsolve()

```
>>> y = sp.Function('y')
>>> t = sp.Symbol('t')
>>> sp.dsolve( sp.Eq( y(t).diff(t,t) - y(t), sp.exp(t) ), y(t) )
Eq(y(t), C2*exp(-t) + (C1 + t/2)*exp(t))
```
ဒါကတော့ Matrix[ 1 2; 2 2] ရဲ့ အိုင်ဂန် values ရှာဖို့ပေါ့။
```
>>> M = sp.Matrix([[1,2],[2,2]])
>>> M.eigenvals()
{3/2 - sqrt(17)/2: 1, 3/2 + sqrt(17)/2: 1}
```
