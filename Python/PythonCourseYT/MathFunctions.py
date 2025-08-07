import math

x=5.0
y=7.8
z=-3.2

print(round(x))  # Rounds to the nearest integer
print(math.ceil(y))   # Rounds up to the nearest integer
print(math.floor(z))  # Rounds down to the nearest integer
print(math.trunc(z))  # Truncates the decimal part
print(math.sqrt(x))  # Square root of x
print(math.pow(x, 2))  # x raised to the power of 2
print(math.exp(x))  # e raised to the power of x
print(math.log(x))  # Natural logarithm of x
print(math.log10(x))  # Base-10 logarithm of x
print(math.sin(x))  # Sine of x (in radians)
print(math.cos(x))  # Cosine of x (in radians)
print(math.tan(x))  # Tangent of x (in radians)
print(math.degrees(x))  # Convert radians to degrees
print(math.radians(x))  # Convert degrees to radians
print(math.factorial(5))  # Factorial of 5
print(math.gcd(12, 15))  # Greatest common divisor of 12 and 15
print(math.lcm(12, 15))  # Least common multiple of 12 and 15
print(math.pi)  # Value of pi
print(math.e)  # Value of e (Euler's number)
print(math.inf)  # Positive infinity
print(math.nan)  # Not a number (NaN)
print(math.isfinite(x))  # Check if x is finite
print(math.isinf(math.inf))  # Check if positive infinity is infinite
print(math.isnan(math.nan))  # Check if NaN is not a number
print(math.isclose(x, y, rel_tol=1e-9))  # Check if x and y are close within a tolerance
