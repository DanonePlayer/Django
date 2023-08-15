# def strong_password(password):
#     regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*{8,}$")

#     if not regex.match(password):
#         raise ValidationError((
#             "password must have at least one uppercase letter,"
#             "one lowercase letter and one number. The length shoud be at least 8 characters."
#         ),
#             code="Invalid"
#         )
