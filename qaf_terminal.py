import os
import sys
import time
import base64
import platform
import random
import re

try:
    import psutil
except ImportError:
    print("ERROR: Faltan dependencias. Execute: pip install psutil")
    sys.exit()

# ARCHIVOS CLASIFICADOS (Base64)
_A1 = b'QW5vbWFsaWEgR3Jhdml0YWNpb25hbCBlbiBOYXRhbno6IExhcyBjZW50cmlmdWdhcyBkZWwgc2VjdG9yIDQgbm8gZXN0YW4gZ2lyYW5kbywgcGVybyBlbCBpc290b3BvIHNlIGVzdGEgZW5yaXF1ZWNpZW5kby4gRWwgdGllbXBvIGxvY2FsIHNlIGhhIHJlZGxhbnRpemFkbyB1biAzJXRyZXMu'
_A2 = b'UHJveWVjdG8gU0lNVVJHSCAoTnVjbGVhcik6IEhlbW9zIGRlc2N1YmllcnRvIHF1ZSBsYSBmcmVjdWVuY2lhIGRlIDE0aEh6IHB1ZWRlIGRldGVuZXIgZWwgZGVjYWltaWVudG8gcmFkaWFjdGl2by4gRXN0YW1vcyBjb25zdHJ1eWVuZG8gdW5hIGJvbWJhIHF1ZSBubyBleHBsb3RhLCBpbXBsb3Npb25hIGxhIHJlYWxpZGFkLg=='
_A3 = b'RW50aWRhZCBDZXJvOiBBbGd1aWVuIGhhIGVzdGFkbyBtb2RpZmljYW5kbyBsb3MgcmVnaXN0cm9zIGRlc2RlIFZlbmV6dWVsYS4gU2UgaGFjZSBsbGFtYXIgJ1NpZ25hbC1NdXJtYW5zaycuIEVsIG5vIHNhYmUgbG8gcXVlIGhhIGRlc3BlcnRhZG8u'
_A4 = b'QUNUQSBSRVVOSU9OIFRFSEVSQU4tTU9TQ1UgKDIwMTUpOiBBY29yZGFtb3MgaWdub3JhciBsYXMgZmx1Y3R1YWNpb25lcyBlbiBlbCBzZWN0b3IgTS0xNC4gTG9zIHJ1c29zIG1pbnRpZXJvbi4gRWwgRHIuIEFyYXNoIGFkdmlydGlvIHNvYnJlIGxhIHJlc29uYW5jaWEuIEFob3JhIE5hdGFueiBzZSBlbmZyaWEu'

# NUEVOS ARCHIVOS: PANDEMIAS Y TERROR CÓSMICO
_A9 = b'SU5GT1JNRSBPTVMtTkVHUk86IEVsIGNydWNlcm8gJ09jZWFuaWMgSG9yaXpvbicgbm8gc2UgaHVuZGlvLiBGdWUgcHVlc3RvIGVuIGN1YXJlbnRlbmEgZW4gYWd1YXMgaW50ZXJuYWNpb25hbGVzLiBFbCBicm90ZSBhIGJvcmRvIG5vIGVzIHVuYSBjZXBhIG5vcm1hbCBkZSBIYW50YXZpcnVzOyBlbCBwYXRvZ2VubyBhbHRlcmEgbGEgcGVyY2VwY2lvbiBkZWwgdGllbXBvIGVuIGxvcyBpbmZlY3RhZG9zIGFudGVzIGRlIGxhIG11ZXJ0ZS4='
_A10 = b'SU5URVJDRVBUQUNJT04gTVNTIChXdWhhbi1QNCk6IEZ1Z2EgZGUgY29udGVuY2lvbiBjb25maXJtYWRhIGVuIGVsIE5pdmVsIFN1YnRlcnJhbmVvIDMuIEVsIG1hdGVyaWFsIGJpb2xvZ2ljbyBubyBlcyBkZSBvcmlnZW4gdGVycmVzdHJlLiBMb3Mgc3VqZXRvcyBleHB1ZXN0b3MgZGVzYXJyb2xsYW4gZXN0cnVjdHVyYXMgY3Jpc3RhbGluYXMgZW4gZWwgbG9idWxvIGZyb250YWwuIFByb3RvY29sbyBkZSBpbmNpbmVyYWNpb24gYWN0aXZhZG8u'
_A11 = b'QVJDSElWTyBLLTEyIChTZW1pcGFsYXRpbnNrLCAxOTg5KTogTGEgcHJ1ZWJhIG51Y2xlYXIgc3VidGVycmFuZWEgbm8gZmFsbG8gcG9yIGVycm9yIGRlIGNhbGN1bG8uIExhIGV4cGxvc2lvbiBkZXNnYXJybyBlbCB0ZWppZG8gbWV0cmljby4gTGFzIGVudGlkYWRlcyBxdWUgY3J1emFyb24gbm8gdGllbmVuIGZvcm1hIGZpc2ljYSwgc29uIGNhbXBvcyBkZSByYWRpYWNpb24gY29uc2NpZW50ZXMuIE5vcyBlc3RhbiBvYnNlcnZhbmRvIGEgdHJhdmVzIGRlIGxhcyBwYW50YWxsYXMu'


def _z(s, d=0.02):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

def _env_scan():
    _z("\n[!] 正在扫描主机环境... (Escaneando entorno anfitrión...)")
    time.sleep(1)
    
    if 'google.colab' in sys.modules:
        _z(">>> هشدار! (¡ADVERTENCIA!) <<<")
        _z("ИСПОЛЬЗОВАНИЕ ОБЛАКА GOOGLE ОБНАРУЖЕНО.")
        _z("You are running this in Google Colab. Do you think Mountain View servers can hide you?")
        _z("Tus máquinas virtuales no te protegerán del desgarro dimensional.")
        _z("Identidad en la nube registrada. Informando a Teherán...")
    else:
        _z(f"SISTEMA DETECTADO: {platform.system()} {platform.release()}")
        _z(f"NODO (КОМПЬЮТЕР): {platform.node()}")
        cores = psutil.cpu_count()
        _z(f"Consumiendo {cores} núcleos lógicos para aislamiento de contención...")

def _verify_clearance(input_key):
    if not re.match(r'^[A-Z]+$', input_key):
        _z("\n[!!!] 警告：DETECTADA ANOMALÍA SINTÁCTICA.")
        _z("[!!!] INTENTO DE INYECCIÓN DE CÓDIGO BLOQUEADO.")
        return False
        
    _cipher_matrix = [15, 20, 7, 20, 1, 29, 0, 6, 1, 7, 20]
    
    if len(input_key) != len(_cipher_matrix): 
        return False
        
    for i, char in enumerate(input_key):
        if (ord(char) ^ 85) != _cipher_matrix[i]:
            return False
    return True

def _encrypt_qaf(text):
    return ' '.join(format((ord(char) + 14) ^ 89, '08b') for char in text)

def _decrypt_qaf(binary_str):
    try:
        chars = binary_str.split()
        return ''.join(chr((int(b, 2) ^ 89) - 14) for b in chars)
    except:
        return "خطا: کد نامعتبر است (ERROR: Cadena binaria incompatible)"

def _void_whisper():
    _z("\n" + "="*50)
    _z("NO SON EXTRATERRESTRES. NO SON DEMONIOS.")
    time.sleep(1)
    _z("La fisura de Semipalatinsk fue solo la puerta.")
    _z("El virus del crucero es su método de adaptación biológica.")
    _z("Son campos de radiación conscientes. Y ahora mismo...")
    time.sleep(2)
    _z(f"...están mirando a través de la pantalla de {platform.node()}.")
    _z("="*50 + "\n")

def _library():
    _z("\n=======================================================")
    _z(" کتابخانه ناهنجاری ها (BIBLIOTECA DE ANOMALÍAS - NIVEL 7)")
    _z("=======================================================")
    _z("[01] Документ 88-A: Colapso Gravitacional (Natanz)")
    _z("[02] Документ 88-B: Detención de Decaimiento Nuclear")
    _z("[03] Документ 88-C: Reporte de Entidad Extranjera")
    _z("[04] MINUTAS: Reunión Teherán-Moscú 2015 (Clasificado)")
    _z("[09] INFORME OMS: Cuarentena 'Oceanic Horizon' (Hantavirus)")
    _z("[10] 拦截 MSS: Incidente Nivel 3 (Wuhan-P4)")
    _z("[11] ДОКУМЕНТ К-12: Incidente Semipalatinsk (1989)")
    
    c = input("\nانتخاب کنید (Seleccione Índice): ")
    
    if c in ['01', '1']: _z("\n[DECRYPTING...]\n" + base64.b64decode(_A1).decode())
    elif c in ['02', '2']: _z("\n[DECRYPTING...]\n" + base64.b64decode(_A2).decode())
    elif c in ['03', '3']: _z("\n[DECRYPTING...]\n" + base64.b64decode(_A3).decode())
    elif c in ['04', '4']: _z("\n[DECRYPTING...]\n" + base64.b64decode(_A4).decode())
    elif c in ['09', '9']: _z("\n[DECRYPTING...]\n" + base64.b64decode(_A9).decode())
    elif c == '10': _z("\n[DECRYPTING...]\n" + base64.b64decode(_A10).decode())
    elif c == '11': _z("\n[DECRYPTING...]\n" + base64.b64decode(_A11).decode())
    else: 
        _z("دسترسی غیرمجاز (Índice Inválido o Acceso Denegado)")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    _z("سیمرغ در حال بیدار شدن است...")
    _z("SIMURGH KERNEL v2.0.4 || AEOI PROPERTY")
    
    _env_scan()
    
    _z("\n>>> INGRESE CONTRASEÑA DE RESONANCIA (Clave Persa):")
    pw = input("-> ").upper()
    
    if not _verify_clearance(pw):
        _z("\n[X] CONTRASEÑA INCORRECTA O ACCESO RESTRINGIDO.")
        _z("[X] БЛОКИРОВКА СИСТЕМЫ (BLOQUEO DEL SISTEMA).")
        sys.exit()

    _z("\n[+] دسترسی تایید شد (Acceso Concedido). Bienvenido, supervisor.")
    
    while True:
        _z("\n[A] CIFRADOR QAF (Binario Mutado)")
        _z("[B] DESCIFRADOR QAF")
        _z("[C] ACCEDER A BIBLIOTECA CLASIFICADA")
        _z("[X] CORTAR ENLACE")
        
        op = input("\nОПЕРАЦИЯ (Operación): ").upper()
        
        # El comando oculto 'OMEGA' desencadena el mensaje de los seres dimensionales
        if op == 'OMEGA':
            _void_whisper()
        elif op == 'A':
            msg = input("Ingrese texto a codificar: ")
            _z("\n[BINARIO QAF]:\n" + _encrypt_qaf(msg))
        elif op == 'B':
            b_str = input("Ingrese binario QAF (separado por espacios): ")
            _z("\n[TRADUCCIÓN]:\n" + _decrypt_qaf(b_str))
        elif op == 'C':
            _library()
        elif op == 'X':
            _z("ارتباط قطع شد (Desconectando...).")
            break
