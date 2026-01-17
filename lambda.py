ans = lambda a, b: a + b
lambda_square_of_the_max = lambda a, b, c: max([a, b, c]) ** 2
a, b, c = 11, 6, 20
print("lambda => %s" % (ans(a, b)))
print("lambda => %s" % (lambda_square_of_the_max(a, b, c)))
