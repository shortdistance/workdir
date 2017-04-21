# coding=utf-8
'''''
加密的一方和解密的一方必须提前确定好key值
'''
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class MyCrypto():
    def __init__(self, key, iv):
        self.key_len = len(key)
        self.iv_len = len(iv)
        if not self.key_len == 16 and not self.key_len == 24 and not self.key_len == 32:
            raise Exception("length of key is wrong")
        if not self.iv_len == 16:
            raise Exception("length of iv is wrong")

        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC  # 这种模式更加安全

    def encrypt(self, text):
        '''''
            被加密的明文长度必须是key长度的整数倍,如果不够,则用\0进行填充
            转成16进制字符串,是因为避免不可见的ascii在显示的时候捣乱
        '''
        cryptor = AES.new(self.key, self.mode, self.iv)
        count = len(text)
        add = self.key_len - (count % self.key_len)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        '''''
            解密后需注意,加密时有可能填充\0,因此要去掉右侧的\0
        '''
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    mc = MyCrypto("kwsy_zds20160822")
    e = mc.encrypt("张东升")
    d = mc.decrypt(e)
    print e, d