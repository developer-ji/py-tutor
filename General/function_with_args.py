def virat(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
data = {
    "kl":2,
    "a":3,
    "b":4,
}
print(virat(data))
# {
#     "kl":2,
#     "a":3,
#     "b":4,
# }
# positional_arg:
# named_argument:
# default_argument: