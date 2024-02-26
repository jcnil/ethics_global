from app.core.process import CryptedProcess


class EncryptedHandler:
    @staticmethod
    def encrypted_text(request):
        obj = CryptedProcess()
        return obj.encrypt_data(request)

class DecryptedHandler:
    @staticmethod
    def decrypted_text(request, private_key):
        obj = CryptedProcess()
        return obj.decrypt_data(request, private_key)