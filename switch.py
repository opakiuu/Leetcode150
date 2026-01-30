# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404 | 403: # Multiple values in one case
#             return "Client error"
#         case _: # The wildcard '_' acts as the default case
#             return "Unknown status"

# print(http_status(404))
# # Output: Client error
# print(http_status(200))
# # Output: OK

# def one():
#     return "One"

# def two():
#     return "Two"

# def default_case():
#     return "Unknown"

# options = {
#     1: one,
#     2: two,
# }

# def switch_by_dict(value):
#     # .get() provides a default function if the key is not found
#     return options.get(value, default_case)()

# print(switch_by_dict(1))
# # Output: One
# print(switch_by_dict(3))
# # Output: Unknown
