import math as m

sol = m.sqrt(2**101 / (m.pi**53+11**7))

# // I HATE DYNAMIC TYPING
sol = str(sol)
sol = sol.replace('.', '')

print(sol[:10])
