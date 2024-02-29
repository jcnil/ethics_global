import time
import psutil
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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
        return get_random_bytes(16)

    @staticmethod
    def encrypted_text(text, key):
        cipher = AES.new(key, AES.MODE_EAX)
        text_encrypted, tag = cipher.encrypt_and_digest(text.encode())
        return text_encrypted

    @staticmethod
    def desencrypted_text(text_encrypted, key):
        cipher = AES.new(key, AES.MODE_EAX)
        text = cipher.decrypt(text_encrypted)
        return text.decode()

    def encrypt_data(self, text):
        key = self.generate_keys()

        encrypted_text = self.encrypted_text(text, key)

        result, total_time = self.measure_time_execution(self.encrypted_text, text, key)

        cpu_percent, memory_percent = self.measure_use_resource()

        request = {
            'text': text,
            'encrypted_text': str(encrypted_text),
            'total_time': str(total_time),
            'cpu_percent': str(cpu_percent),
            'memory_percent': str(memory_percent)
        }

        Queryset.create_row(request)

        return {
            'status': OK,
            'data': request,
            'message': 'Text Encrypted',
            'exception': NotFoundException
        }

    def decrypt_data(self, encrypted_text):
        #key = self.generate_keys()
        #decrypted_text = self.desencrypted_text(encrypted_text, key)
        #result, total_time = self.measure_time_execution(self.desencrypted_text, encrypted_text, key)
        #cpu_percent, memory_percent = self.measure_use_resource()

        qu = Queryset.get_encrypt_data(encrypted_text)

        request = {
            'decrypt_text': qu.text,
            'encrypted_text': str(encrypted_text),
            'total_time': qu.total_time,
            'cpu_percent': qu.cpu_percent,
            'memory_percent': qu.memory_percent
        }

        return {
            'status': OK,
            'data': request,
            "message": "Text Decrypted",
            'exception': NotFoundException
        }
