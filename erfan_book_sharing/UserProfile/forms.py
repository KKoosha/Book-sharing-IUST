class RegistrationForm():
    def __init__(self):
        self.fields = (
            forms.TextField(field_name='username',
                            length=30, maxlength=30,
                            is_required=True, validator_list=[validators.isAlphaNumeric,
                                                              self.isValidUsername]),
            forms.EmailField(field_name='email',
                             length=30,
                             maxlength=30,
                             is_required=True),
            forms.PasswordField(field_name='password1',
                                length=30,
                                maxlength=60,
                                is_required=True),
            forms.PasswordField(field_name='password2',
                                length=30, maxlength=60,
                                is_required=True,
                                validator_list=[validators.AlwaysMatchesOtherField('password1',
                                                                                   'Passwords must match.')]),
            )
    
    def isValidUsername(self, field_data, all_data):
        try:
            User.objects.get(username=field_data)
        except User.DoesNotExist:
            return
        raise validators.ValidationError('The username "%s" is already taken.' % field_data)
    
    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],
                                     new_data['email'],
                                     new_data['password1'])
        u.is_active = False
        u.save()
        return u
