X = int(input())

num_count = 1
i = 1
while num_count < X:
    i += 1
    num_count += i

if i % 2 == 0:
    nume = i - num_count + X
    deno = num_count - X + 1
else:
    nume = 1 + num_count - X
    deno = i - num_count + X
print('{}/{}'.format(nume,deno))