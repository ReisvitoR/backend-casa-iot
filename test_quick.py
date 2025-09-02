#!/usr/bin/env python3
"""
Teste rápido para verificar se os endpoints corrigidos estão funcionando
"""
import urllib.request
import json

BASE_URL = "https://backend-casa-iot.onrender.com/api"

def quick_test():
    endpoints_to_test = [
        # Endpoints que estavam com problema (404)
        "/dispositivos/ativos/",
        "/dispositivos/inativos/", 
        "/cenas/ativas/",
        "/cenas/favoritas/",
        "/cenas/disponiveis/",
        
        # Endpoints principais para garantir que funcionam
        "/usuarios/",
        "/casas/",
        "/comodos/",
        "/tipos-dispositivo/",
        "/dispositivos/",
        "/cenas/",
        "/acoes-cena/",
        "/logs/"
    ]
    
    print("🧪 TESTE RÁPIDO - ENDPOINTS CORRIGIDOS")
    print("=" * 50)
    
    success_count = 0
    total_count = len(endpoints_to_test)
    
    for endpoint in endpoints_to_test:
        try:
            url = f"{BASE_URL}{endpoint}"
            with urllib.request.urlopen(url, timeout=15) as response:
                status = response.getcode()
                if status == 200:
                    print(f"✅ {endpoint}")
                    success_count += 1
                else:
                    print(f"❌ {endpoint} - Status: {status}")
        except Exception as e:
            print(f"❌ {endpoint} - Error: {str(e)[:50]}...")
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTADO:")
    print(f"✅ Sucessos: {success_count}/{total_count}")
    print(f"❌ Falhas: {total_count - success_count}/{total_count}")
    print(f"📈 Taxa de sucesso: {(success_count/total_count)*100:.1f}%")
    
    if success_count == total_count:
        print("\n🎉 TODOS OS ENDPOINTS FUNCIONANDO!")
        print("🚀 Correções aplicadas com sucesso!")
    else:
        print(f"\n⚠️ {total_count - success_count} endpoint(s) ainda com problema")

if __name__ == "__main__":
    quick_test()
