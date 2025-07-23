
"""此文件用于定义通用的函数"""

import hashlib


def generate_token(session_key):
    """生成token令牌"""
    # 使用session_key进行哈希处理作为token
    token = hashlib.sha256(session_key.encode('utf-8')).hexdigest()
    return token

