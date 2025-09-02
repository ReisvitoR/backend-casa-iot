#!/usr/bin/env python3
"""
TESTE COMPLETO DE CRUD - TODAS AS CLASSES
Testa CRUD completo para todas as entidades do sistema
"""

import requests
import json
from datetime import datetime

BASE_URL = "https://backend-casa-iot.onrender.com/api"
HEADERS = {'Content-Type': 'application/json'}

class TestCRUD:
    def __init__(self):
        self.created_ids = {}
        self.results = {}
    
    def log(self, message, status="info"):
        emoji = {"info": "ℹ️", "success": "✅", "error": "❌", "warning": "⚠️"}
        print(f"{emoji.get(status, 'ℹ️')} {message}")
    
    def test_endpoint(self, endpoint, create_data, update_data=None, skip_delete=False):
        """Testa CRUD completo em um endpoint"""
        self.log(f"TESTANDO: {endpoint.upper()}", "info")
        print("-" * 60)
        
        success_count = 0
        total_tests = 5 if not skip_delete else 4  # CREATE, READ_LIST, READ_DETAIL, UPDATE, [DELETE]
        
        # 1. CREATE (POST)
        self.log("CREATE (POST)...")
        try:
            response = requests.post(f"{BASE_URL}/{endpoint}/", 
                                   json=create_data, 
                                   headers=HEADERS,
                                   timeout=15)
            
            if response.status_code in [200, 201]:
                created_item = response.json()
                item_id = created_item.get('id')
                self.created_ids[endpoint] = item_id
                self.log(f"Criado com ID: {item_id}", "success")
                success_count += 1
            else:
                self.log(f"Falha CREATE - Status: {response.status_code} - {response.text[:100]}", "error")
                self.results[endpoint] = f"❌ CREATE falhou ({response.status_code})"
                return False
                
        except Exception as e:
            self.log(f"Exceção CREATE: {e}", "error")
            self.results[endpoint] = "❌ CREATE exceção"
            return False
        
        item_id = self.created_ids[endpoint]
        
        # 2. READ LIST (GET)
        self.log("READ LIST (GET)...")
        try:
            response = requests.get(f"{BASE_URL}/{endpoint}/", timeout=10)
            if response.status_code == 200:
                self.log("Lista OK", "success")
                success_count += 1
            else:
                self.log(f"Falha READ LIST - Status: {response.status_code}", "error")
        except Exception as e:
            self.log(f"Exceção READ LIST: {e}", "error")
        
        # 3. READ DETAIL (GET)
        self.log("READ DETAIL (GET)...")
        try:
            response = requests.get(f"{BASE_URL}/{endpoint}/{item_id}/", timeout=10)
            if response.status_code == 200:
                self.log("Detalhe OK", "success")
                success_count += 1
            else:
                self.log(f"Falha READ DETAIL - Status: {response.status_code}", "error")
        except Exception as e:
            self.log(f"Exceção READ DETAIL: {e}", "error")
        
        # 4. UPDATE (PATCH)
        self.log("UPDATE (PATCH)...")
        patch_data = update_data or {"nome": f"Editado_{datetime.now().strftime('%H%M%S')}"}
        try:
            response = requests.patch(f"{BASE_URL}/{endpoint}/{item_id}/", 
                                    json=patch_data, 
                                    headers=HEADERS,
                                    timeout=10)
            if response.status_code == 200:
                self.log("Update OK", "success")
                success_count += 1
            else:
                self.log(f"Falha UPDATE - Status: {response.status_code} - {response.text[:100]}", "error")
        except Exception as e:
            self.log(f"Exceção UPDATE: {e}", "error")
        
        # 5. DELETE (somente se não for dependência)
        if not skip_delete:
            self.log("DELETE...")
            try:
                response = requests.delete(f"{BASE_URL}/{endpoint}/{item_id}/", timeout=10)
                if response.status_code in [204, 200]:
                    self.log("Delete OK", "success")
                    success_count += 1
                else:
                    self.log(f"Falha DELETE - Status: {response.status_code}", "error")
            except Exception as e:
                self.log(f"Exceção DELETE: {e}", "error")
        else:
            self.log("DELETE pulado (dependência)", "warning")
        
        # Resultado final para este endpoint
        if success_count == total_tests:
            self.results[endpoint] = "✅ CRUD COMPLETO"
            result = True
        elif success_count >= 3:
            self.results[endpoint] = f"⚠️ CRUD PARCIAL ({success_count}/{total_tests})"
            result = True
        else:
            self.results[endpoint] = f"❌ CRUD FALHOU ({success_count}/{total_tests})"
            result = False
        
        print()
        return result
    
    def run_all_tests(self):
        """Executa todos os testes na ordem correta das dependências"""
        self.log("🧪 TESTE COMPLETO DE CRUD - TODAS AS CLASSES", "info")
        print("=" * 80)
        self.log(f"Base URL: {BASE_URL}", "info")
        self.log(f"Iniciado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", "info")
        print()
        
        # 1. USUÁRIO (sem dependências) - NÃO DELETAR
        usuario_data = {
            "username": f"teste_{datetime.now().strftime('%H%M%S')}",
            "email": f"teste_{datetime.now().strftime('%H%M%S')}@crud.com",
            "first_name": "Teste",
            "last_name": "CRUD",
            "password": "teste123"
        }
        self.test_endpoint("usuarios", usuario_data, skip_delete=True)
        
        # 2. TIPO DISPOSITIVO (sem dependências) - NÃO DELETAR
        tipo_data = {
            "nome": f"Tipo_Teste_{datetime.now().strftime('%H%M%S')}",
            "categoria": "iluminacao",
            "icone": "lightbulb"
        }
        self.test_endpoint("tipos-dispositivo", tipo_data, skip_delete=True)
        
        # 3. CASA (depende de usuário) - NÃO DELETAR
        if 'usuarios' in self.created_ids:
            casa_data = {
                "nome": f"Casa_Teste_{datetime.now().strftime('%H%M%S')}",
                "endereco": "Rua do Teste CRUD, 123",
                "usuario": self.created_ids['usuarios']
            }
            self.test_endpoint("casas", casa_data, skip_delete=True)
        else:
            self.log("CASA: Pulado - usuário não criado", "warning")
            self.results["casas"] = "⚠️ Pulado - dependência"
        
        # 4. CÔMODO (depende de casa) - NÃO DELETAR
        if 'casas' in self.created_ids:
            comodo_data = {
                "nome": f"Comodo_Teste_{datetime.now().strftime('%H%M%S')}",
                "casa": self.created_ids['casas'],
                "descricao": "Cômodo de teste"
            }
            self.test_endpoint("comodos", comodo_data, skip_delete=True)
        else:
            self.log("CÔMODO: Pulado - casa não criada", "warning")
            self.results["comodos"] = "⚠️ Pulado - dependência"
        
        # 5. DISPOSITIVO (depende de cômodo e tipo) - NÃO DELETAR
        if 'comodos' in self.created_ids and 'tipos-dispositivo' in self.created_ids:
            dispositivo_data = {
                "nome": f"Dispositivo_Teste_{datetime.now().strftime('%H%M%S')}",
                "comodo": self.created_ids['comodos'],
                "tipo": self.created_ids['tipos-dispositivo'],
                "estado": False,
                "ativo": True
            }
            self.test_endpoint("dispositivos", dispositivo_data, skip_delete=True)
        else:
            self.log("DISPOSITIVO: Pulado - dependências não criadas", "warning")
            self.results["dispositivos"] = "⚠️ Pulado - dependência"
        
        # 6. CENA (depende de casa) - NÃO DELETAR
        if 'casas' in self.created_ids:
            cena_data = {
                "nome": f"Cena_Teste_{datetime.now().strftime('%H%M%S')}",
                "casa": self.created_ids['casas'],
                "descricao": "Cena de teste",
                "ativa": True,
                "favorita": False
            }
            self.test_endpoint("cenas", cena_data, skip_delete=True)
        else:
            self.log("CENA: Pulado - casa não criada", "warning")
            self.results["cenas"] = "⚠️ Pulado - dependência"
        
        # 7. AÇÃO CENA (depende de cena e dispositivo) - PODE DELETAR
        if 'cenas' in self.created_ids and 'dispositivos' in self.created_ids:
            acao_data = {
                "cena": self.created_ids['cenas'],
                "dispositivo": self.created_ids['dispositivos'],
                "estado_desejado": True,  # Campo correto!
                "ordem": 1
            }
            self.test_endpoint("acoes-cena", acao_data, skip_delete=False)
        else:
            self.log("AÇÃO CENA: Pulado - dependências não criadas", "warning")
            self.results["acoes-cena"] = "⚠️ Pulado - dependência"
        
        # LIMPEZA FINAL - Deletar na ordem inversa das dependências
        self.cleanup_test_data()
        
        # RESULTADO FINAL
        self.print_final_results()
    
    def cleanup_test_data(self):
        """Limpa os dados de teste na ordem correta (inversa das dependências)"""
        self.log("🧹 LIMPEZA DOS DADOS DE TESTE", "info")
        print("-" * 60)
        
        # Ordem de limpeza: do mais dependente para o menos dependente
        cleanup_order = ['dispositivos', 'cenas', 'comodos', 'casas', 'tipos-dispositivo', 'usuarios']
        
        for endpoint in cleanup_order:
            if endpoint in self.created_ids:
                item_id = self.created_ids[endpoint]
                self.log(f"Deletando {endpoint} ID {item_id}...")
                try:
                    response = requests.delete(f"{BASE_URL}/{endpoint}/{item_id}/", timeout=10)
                    if response.status_code in [204, 200]:
                        self.log(f"✅ {endpoint} deletado", "success")
                    else:
                        self.log(f"⚠️ Falha ao deletar {endpoint}: {response.status_code}", "warning")
                except Exception as e:
                    self.log(f"❌ Erro ao deletar {endpoint}: {e}", "error")
        
        print()
    
    def print_final_results(self):
        """Imprime o resultado final de todos os testes"""
        print("=" * 80)
        self.log("📊 RESULTADO FINAL DOS TESTES:", "info")
        print("-" * 80)
        
        total_endpoints = len(self.results)
        success_count = sum(1 for result in self.results.values() if result.startswith("✅"))
        partial_count = sum(1 for result in self.results.values() if result.startswith("⚠️"))
        
        for endpoint, result in self.results.items():
            print(f"   {result} {endpoint}")
        
        print("-" * 80)
        self.log(f"RESUMO: {success_count} completos, {partial_count} parciais, de {total_endpoints} endpoints", "info")
        
        if success_count == total_endpoints:
            self.log("🎉 SUCESSO TOTAL: Todos os endpoints têm CRUD completo!", "success")
        elif success_count + partial_count == total_endpoints:
            self.log("✨ SUCESSO: Todos os endpoints funcionais!", "success")
        else:
            self.log("⚠️ ATENÇÃO: Alguns endpoints falharam", "warning")
        
        self.log(f"Finalizado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", "info")

if __name__ == "__main__":
    tester = TestCRUD()
    tester.run_all_tests()
