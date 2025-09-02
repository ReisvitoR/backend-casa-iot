#!/usr/bin/env python3
"""
TESTE DE CRUD COM DADOS CORRETOS
"""

import requests
import json

BASE_URL = "https://backend-casa-iot.onrender.com/api"
HEADERS = {'Content-Type': 'application/json'}

def create_usuario():
    """Cria um usuário para usar nos testes"""
    data = {
        "email": "teste@crud.com",
        "first_name": "Teste",
        "last_name": "CRUD",
        "username": "teste_crud",
        "password": "teste123"
    }
    
    response = requests.post(f"{BASE_URL}/usuarios/", json=data, headers=HEADERS)
    print(f"Criando usuário: {response.status_code}")
    if response.status_code in [200, 201]:
        return response.json()['id']
    return None

def test_crud():
    print("🧪 TESTE DE CRUD COM DADOS CORRETOS")
    print("=" * 50)
    
    # 1. Criar usuário primeiro
    print("1️⃣ Criando usuário...")
    usuario_id = create_usuario()
    
    if not usuario_id:
        print("❌ Falha ao criar usuário")
        return
    
    print(f"✅ Usuário criado: ID {usuario_id}")
    
    # 2. Teste TipoDispositivo com categoria válida
    print("\n2️⃣ Testando TipoDispositivo...")
    tipo_data = {
        "nome": "Lâmpada Teste",
        "categoria": "iluminacao",  # Categoria válida
        "icone": "lightbulb"
    }
    
    response = requests.post(f"{BASE_URL}/tipos-dispositivo/", json=tipo_data, headers=HEADERS)
    print(f"POST TipoDispositivo: {response.status_code}")
    
    if response.status_code in [200, 201]:
        tipo_id = response.json()['id']
        print(f"✅ Tipo criado: ID {tipo_id}")
        
        # Teste PATCH
        patch_response = requests.patch(f"{BASE_URL}/tipos-dispositivo/{tipo_id}/",
                                      json={"nome": "Lâmpada Editada"}, headers=HEADERS)
        print(f"PATCH TipoDispositivo: {patch_response.status_code}")
        
        # Teste DELETE
        delete_response = requests.delete(f"{BASE_URL}/tipos-dispositivo/{tipo_id}/")
        print(f"DELETE TipoDispositivo: {delete_response.status_code}")
        
    else:
        print(f"❌ Erro: {response.text}")
    
    # 3. Teste Casa com usuário
    print("\n3️⃣ Testando Casa...")
    casa_data = {
        "nome": "Casa Teste CRUD",
        "endereco": "Rua do Teste, 123",
        "usuario": usuario_id  # Usuário obrigatório
    }
    
    response = requests.post(f"{BASE_URL}/casas/", json=casa_data, headers=HEADERS)
    print(f"POST Casa: {response.status_code}")
    
    if response.status_code in [200, 201]:
        casa_id = response.json()['id']
        print(f"✅ Casa criada: ID {casa_id}")
        
        # Teste PATCH
        patch_response = requests.patch(f"{BASE_URL}/casas/{casa_id}/",
                                      json={"nome": "Casa Editada"}, headers=HEADERS)
        print(f"PATCH Casa: {patch_response.status_code}")
        
        # Teste DELETE
        delete_response = requests.delete(f"{BASE_URL}/casas/{casa_id}/")
        print(f"DELETE Casa: {delete_response.status_code}")
        
    else:
        print(f"❌ Erro: {response.text}")
    
    # 4. Limpar usuário de teste
    print("\n4️⃣ Limpando usuário de teste...")
    delete_user = requests.delete(f"{BASE_URL}/usuarios/{usuario_id}/")
    print(f"DELETE Usuario: {delete_user.status_code}")
    
    print("\n🎯 Teste concluído!")

if __name__ == "__main__":
    test_crud()
