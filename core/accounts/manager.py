from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def createUser(self, phoneNumber, password = None, **extraFields):
        if not phoneNumber:
            raise ValueError("Phone number field is required!")

        # normalize_email --> will remove the case senstivity of email
        # for ex: shiv@gmail.com === Shiv@gmail.com
        extraFields['email']  = self.normalize_email(extraFields['email'])
        user = self.model(phoneNumber = phoneNumber, **extraFields)
        # set_password is used to encrypt the password
        user.set_password(password)
        # saving in to DB
        user.save(using = self.db)

        return user

    # For admin purpose
    def createSuperUser(self, phoneNumber, password = None, **extraFields):
        # we set some fields as By default
        extraFields.setdefault("is_staff", True)
        extraFields.setdefault("is_superuser", True)
        extraFields.setdefault("is_active", True)

        # we are returning createUser method
        return self.createUser(phoneNumber, password, **extraFields)