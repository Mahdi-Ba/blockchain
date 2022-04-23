from rest_framework import serializers


class AddressInfoSerializer(serializers.Serializer):
    blockchain_type = serializers.CharField(max_length=60)

    def validate_blockchain_type(self, blockchain_type):
        if blockchain_type.lower() not in ['bitcoin', 'ethereum']:
            raise serializers.ValidationError("Blockchain not valid")
        return blockchain_type