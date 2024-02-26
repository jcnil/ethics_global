import time
import psutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from app.core.exceptions import NotFoundException
from app.core.querysets import Queryset
from app.core.constants import OK


class Performance:
    @staticmethod
    def measure_time_execution(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        total_time = end - start
        return result, total_time

    @staticmethod
    def measure_use_resource():
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        return cpu_percent, memory_percent


class CryptedProcess(Performance):
    @staticmethod
    def generate_keys():
        key = RSA.generate(2048)
        return key

    @staticmethod
    def encrypted_text(text, public_key):
        cipher = PKCS1_OAEP.new(public_key)
        text_encrypted = cipher.encrypt(text.encode())
        return text_encrypted

    @staticmethod
    def desencrypted_text(text_encrypted, private_key):
        cipher = PKCS1_OAEP.new(private_key)
        text = cipher.decrypt(text_encrypted).decode()
        return text

    def encrypt_data(self, text):
        public_key = self.generate_keys().publickey()

        encrypted_text = self.encrypted_text(text, public_key)

        result, total_time = self.measure_time_execution(self.encrypted_text, text, public_key)

        cpu_percent, memory_percent = self.measure_use_resource()

        request = {
            'text': text,
            'encrypted_text': str(encrypted_text),
            'total_time': str(total_time),
            'cpu_percent': str(cpu_percent),
            'memory_percent': str(memory_percent)
        }

        Queryset.create_row(request)

        request['private_key'] = str(self.generate_keys())

        return {
            'status': OK,
            'data': request,
            'message': 'Text Encrypted',
            'exception': NotFoundException
        }

    def decrypt_data(self, encrypted_text, private_key):

        decrypted_text = self.desencrypted_text(encrypted_text, private_key)

        result, total_time = self.measure_time_execution(self.desencrypted_text, encrypted_text, private_key)

        cpu_percent, memory_percent = self.measure_use_resource()

        request = {
            'text': decrypted_text,
            'encrypted_text': str(encrypted_text),
            'total_time': str(total_time),
            'cpu_percent': str(cpu_percent),
            'memory_percent': str(memory_percent)
        }

        Queryset.create_row(request)

        return {
            'status': OK,
            'data': request,
            "message": "Text Decrypted",
            'exception': NotFoundException
        }
