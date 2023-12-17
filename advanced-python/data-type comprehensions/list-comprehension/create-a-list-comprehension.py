# WAP to make a list containing first n- natural numbers
fn = []

# traditional way
for i in range(1, 100):
    # either you do this
    fn.append(i)

    # or you do this
    fn.extend([i,])

    # both will work the same

print(fn)

# list comprehension way ~

l = [i for i in range(1, 100)]
print(l)

# Note -> list comprehension can be combined with shorthand if. But shorthand else don't work.

m = [i*2 for i in range(1, 100) if i < 10]
print(m)

# but yeah, if the short hand if else is written first and the loop is written after it, it works!!

n = [i*2 if i < 10 else 0 for i in range(1, 100)]
print(n)
# the only drawback is that it doesn't work with pass. you can not pass a pass statement in it.