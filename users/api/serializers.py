from rest_framework import serializers

from users.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', )
        extra_kwargs = {
            'first_name': {'required': True}
        }

    def save(self, **kwargs):
        data = self.validated_data
        password = data.pop("password")

        account = CustomUser(**data)
        account.set_password(password)
        account.save()
        self.instance = account

        return self.instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(instance.get_tokens())
        return data
