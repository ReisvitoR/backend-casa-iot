#!/usr/bin/env python3
"""
Script COMPLETO para testar TODAS as rotas da API Casa IoT
Inclui: GET, POST, PUT, PATCH, DELETE
"""
import urllib.request
import urllib.parse
import json
import time

BASE_URL = "https://backend-casa-iot.onrender.com/api"

def make_request(method, endpoint, data=None, expected_status=200):
    """Faz requisição HTTP"""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if data:
            data_bytes = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=data_bytes)
            req.add_header('Content-Type', 'application/json')
        else:
            req = urllib.request.Request(url)
        
        req.get_method = lambda: method
        
        with urllib.request.urlopen(req, timeout=30) as response:
            status = response.getcode()
            result = json.loads(response.read().decode('utf-8'))
            
            status_icon = "✅" if status == expected_status else "❌"
            print(f"{status_icon} {method} {endpoint} - Status: {status}")
            
            if status != expected_status:
                print(f"   Expected: {expected_status}, Got: {status}")
            
            return status == expected_status, result
            
    except urllib.error.HTTPError as e:
        status = e.code
        status_icon = "✅" if status == expected_status else "❌"
        print(f"{status_icon} {method} {endpoint} - Status: {status}")
        
        if status != expected_status:
            print(f"   Expected: {expected_status}, Got: {status}")
            
        return status == expected_status, None
        
    except Exception as e:
        print(f"❌ {method} {endpoint} - ERROR: {str(e)}")
        return False, None

def test_crud_complete():
    print("🧪 TESTE COMPLETO - TODOS OS MÉTODOS HTTP")
    print("=" * 60)
    
    results = []
    created_ids = {}
    
    # === 1. USUÁRIOS ===
    print("\n👤 TESTANDO USUÁRIOS (CRUD COMPLETO):")
    
    # GET - Listar usuários
    success, data = make_request("GET", "/usuarios/")
    results.append(success)
    
    # POST - Criar usuário
    user_data = {
        "username": "teste_user_2025",
        "nome": "Usuário Teste",
        "email": "teste@email.com",
        "telefone": "(11) 99999-9999"
    }
    success, data = make_request("POST", "/usuarios/", user_data, 201)
    results.append(success)
    if success and data:
        created_ids['usuario'] = data.get('id')
        print(f"   📝 Usuário criado com ID: {created_ids['usuario']}")
    
    # GET - Usuário específico
    if 'usuario' in created_ids:
        success, data = make_request("GET", f"/usuarios/{created_ids['usuario']}/")
        results.append(success)
    
    # PUT - Atualizar usuário completo
    if 'usuario' in created_ids:
        updated_user = {
            "username": "teste_user_updated",
            "nome": "Usuário Atualizado",
            "email": "atualizado@email.com",
            "telefone": "(11) 88888-8888"
        }
        success, data = make_request("PUT", f"/usuarios/{created_ids['usuario']}/", updated_user)
        results.append(success)
    
    # PATCH - Atualização parcial
    if 'usuario' in created_ids:
        patch_data = {"telefone": "(11) 77777-7777"}
        success, data = make_request("PATCH", f"/usuarios/{created_ids['usuario']}/", patch_data)
        results.append(success)
    
    # GET - Endpoint especial
    success, data = make_request("GET", "/usuarios/me/")
    results.append(success)
    
    # === 2. CASAS ===
    print("\n🏠 TESTANDO CASAS (CRUD COMPLETO):")
    
    # GET - Listar casas
    success, data = make_request("GET", "/casas/")
    results.append(success)
    
    # POST - Criar casa
    casa_data = {
        "nome": "Casa Teste API",
        "endereco": "Rua Teste, 123",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01234-567"
    }
    success, data = make_request("POST", "/casas/", casa_data, 201)
    results.append(success)
    if success and data:
        created_ids['casa'] = data.get('id')
        print(f"   📝 Casa criada com ID: {created_ids['casa']}")
    
    # GET - Casa específica
    if 'casa' in created_ids:
        success, data = make_request("GET", f"/casas/{created_ids['casa']}/")
        results.append(success)
    
    # GET - Status da casa
    if 'casa' in created_ids:
        success, data = make_request("GET", f"/casas/{created_ids['casa']}/status/")
        results.append(success)
    
    # PUT - Atualizar casa
    if 'casa' in created_ids:
        updated_casa = {
            "nome": "Casa Teste Atualizada",
            "endereco": "Rua Nova, 456",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "20000-000"
        }
        success, data = make_request("PUT", f"/casas/{created_ids['casa']}/", updated_casa)
        results.append(success)
    
    # === 3. CÔMODOS ===
    print("\n🚪 TESTANDO CÔMODOS (CRUD COMPLETO):")
    
    # GET - Listar cômodos
    success, data = make_request("GET", "/comodos/")
    results.append(success)
    
    # POST - Criar cômodo
    if 'casa' in created_ids:
        comodo_data = {
            "nome": "Sala Teste",
            "casa": created_ids['casa'],
            "descricao": "Sala de teste da API"
        }
        success, data = make_request("POST", "/comodos/", comodo_data, 201)
        results.append(success)
        if success and data:
            created_ids['comodo'] = data.get('id')
            print(f"   📝 Cômodo criado com ID: {created_ids['comodo']}")
    
    # GET - Cômodo específico
    if 'comodo' in created_ids:
        success, data = make_request("GET", f"/comodos/{created_ids['comodo']}/")
        results.append(success)
    
    # === 4. TIPOS DE DISPOSITIVO ===
    print("\n🔧 TESTANDO TIPOS DE DISPOSITIVO (CRUD COMPLETO):")
    
    # GET - Listar tipos
    success, data = make_request("GET", "/tipos-dispositivo/")
    results.append(success)
    
    # POST - Criar tipo
    tipo_data = {
        "nome": "Dispositivo Teste API",
        "categoria": "teste",
        "descricao": "Dispositivo para teste da API"
    }
    success, data = make_request("POST", "/tipos-dispositivo/", tipo_data, 201)
    results.append(success)
    if success and data:
        created_ids['tipo'] = data.get('id')
        print(f"   📝 Tipo criado com ID: {created_ids['tipo']}")
    
    # === 5. DISPOSITIVOS ===
    print("\n🔌 TESTANDO DISPOSITIVOS (CRUD COMPLETO + ENDPOINTS ESPECIAIS):")
    
    # GET - Listar dispositivos
    success, data = make_request("GET", "/dispositivos/")
    results.append(success)
    
    # POST - Criar dispositivo
    if 'comodo' in created_ids and 'tipo' in created_ids:
        dispositivo_data = {
            "nome": "Dispositivo Teste",
            "comodo": created_ids['comodo'],
            "tipo": created_ids['tipo'],
            "estado": False,
            "ativo": True
        }
        success, data = make_request("POST", "/dispositivos/", dispositivo_data, 201)
        results.append(success)
        if success and data:
            created_ids['dispositivo'] = data.get('id')
            print(f"   📝 Dispositivo criado com ID: {created_ids['dispositivo']}")
    
    # GET - Endpoints especiais (CORRIGIDOS)
    success, data = make_request("GET", "/dispositivos/ativos/")
    results.append(success)
    
    success, data = make_request("GET", "/dispositivos/inativos/")
    results.append(success)
    
    success, data = make_request("GET", "/dispositivos/status_geral/")
    results.append(success)
    
    # POST - Toggle dispositivo
    if 'dispositivo' in created_ids:
        success, data = make_request("POST", f"/dispositivos/{created_ids['dispositivo']}/toggle/")
        results.append(success)
    
    # === 6. CENAS ===
    print("\n🎬 TESTANDO CENAS (CRUD COMPLETO + ENDPOINTS ESPECIAIS):")
    
    # GET - Listar cenas
    success, data = make_request("GET", "/cenas/")
    results.append(success)
    
    # POST - Criar cena
    if 'casa' in created_ids:
        cena_data = {
            "nome": "Cena Teste API",
            "casa": created_ids['casa'],
            "descricao": "Cena para teste da API",
            "ativa": True,
            "favorita": False
        }
        success, data = make_request("POST", "/cenas/", cena_data, 201)
        results.append(success)
        if success and data:
            created_ids['cena'] = data.get('id')
            print(f"   📝 Cena criada com ID: {created_ids['cena']}")
    
    # GET - Endpoints especiais (CORRIGIDOS)
    success, data = make_request("GET", "/cenas/ativas/")
    results.append(success)
    
    success, data = make_request("GET", "/cenas/favoritas/")
    results.append(success)
    
    success, data = make_request("GET", "/cenas/disponiveis/")
    results.append(success)
    
    success, data = make_request("GET", "/cenas/status_geral/")
    results.append(success)
    
    # POST - Executar cena
    if 'cena' in created_ids:
        success, data = make_request("POST", f"/cenas/{created_ids['cena']}/executar/")
        results.append(success)
    
    # === 7. AÇÕES DE CENA ===
    print("\n⚙️ TESTANDO AÇÕES DE CENA (CRUD COMPLETO):")
    
    # GET - Listar ações
    success, data = make_request("GET", "/acoes-cena/")
    results.append(success)
    
    # POST - Criar ação
    if 'cena' in created_ids and 'dispositivo' in created_ids:
        acao_data = {
            "cena": created_ids['cena'],
            "dispositivo": created_ids['dispositivo'],
            "acao": "ligar",
            "valor": "100",
            "ordem": 1
        }
        success, data = make_request("POST", "/acoes-cena/", acao_data, 201)
        results.append(success)
        if success and data:
            created_ids['acao'] = data.get('id')
            print(f"   📝 Ação criada com ID: {created_ids['acao']}")
    
    # === 8. LOGS ===
    print("\n📊 TESTANDO LOGS (READ-ONLY):")
    
    # GET - Listar logs
    success, data = make_request("GET", "/logs/")
    results.append(success)
    
    # === LIMPEZA ===
    print("\n🧹 LIMPANDO DADOS DE TESTE:")
    
    # DELETE - Limpar dados criados (ordem inversa)
    if 'acao' in created_ids:
        success, data = make_request("DELETE", f"/acoes-cena/{created_ids['acao']}/", None, 204)
        results.append(success)
    
    if 'cena' in created_ids:
        success, data = make_request("DELETE", f"/cenas/{created_ids['cena']}/", None, 204)
        results.append(success)
    
    if 'dispositivo' in created_ids:
        success, data = make_request("DELETE", f"/dispositivos/{created_ids['dispositivo']}/", None, 204)
        results.append(success)
    
    if 'tipo' in created_ids:
        success, data = make_request("DELETE", f"/tipos-dispositivo/{created_ids['tipo']}/", None, 204)
        results.append(success)
    
    if 'comodo' in created_ids:
        success, data = make_request("DELETE", f"/comodos/{created_ids['comodo']}/", None, 204)
        results.append(success)
    
    if 'casa' in created_ids:
        success, data = make_request("DELETE", f"/casas/{created_ids['casa']}/", None, 204)
        results.append(success)
    
    if 'usuario' in created_ids:
        success, data = make_request("DELETE", f"/usuarios/{created_ids['usuario']}/", None, 204)
        results.append(success)
    
    # === RESUMO FINAL ===
    print("\n" + "=" * 60)
    print("📊 RESUMO FINAL DOS TESTES:")
    
    successful = sum(1 for result in results if result)
    total = len(results)
    
    print(f"✅ Sucessos: {successful}/{total}")
    print(f"❌ Falhas: {total - successful}/{total}")
    print(f"📈 Taxa de sucesso: {(successful/total)*100:.1f}%")
    
    print(f"\n📋 MÉTODOS TESTADOS:")
    print(f"  • GET (leitura)")
    print(f"  • POST (criação)")
    print(f"  • PUT (atualização completa)")
    print(f"  • PATCH (atualização parcial)")
    print(f"  • DELETE (remoção)")
    print(f"  • Actions customizadas (toggle, status, etc.)")
    
    if successful == total:
        print("\n🎉 TODOS OS ENDPOINTS E MÉTODOS FUNCIONANDO PERFEITAMENTE!")
        print("🚀 API 100% OPERACIONAL!")
    else:
        print(f"\n⚠️ {total - successful} ENDPOINT(S) COM PROBLEMA")
        print("🔧 Verificar logs acima para detalhes")

if __name__ == "__main__":
    test_crud_complete()
