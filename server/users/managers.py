from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login, email, password=None):
        if not login:
            raise ValueError('Необходимо указать логин!')
        user = self.model(login=login, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, login, email, password=None):
        user = self.create_user(login, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
