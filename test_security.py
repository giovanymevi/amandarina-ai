import httpx
import asyncio

BASE_URL = "http://127.0.0.1:8000"

async def run_tests():
    async with httpx.AsyncClient() as client:
        print("--- Iniciando pruebas de seguridad de IP ---\n")
        
        # 1. Petición desde IP local (debería ser bloqueada)
        print("Prueba 1: Petición local (sin X-Forwarded-For)...")
        try:
            res1 = await client.post(f"{BASE_URL}/chat", json={"text": "Hola"})
            print(f"Status: {res1.status_code} - Detail: {res1.json().get('detail')}")
        except Exception as e:
            print(f"Error: ¿Está el servidor encendido en {BASE_URL}?")

        # 2. Simulando IP permitida (74.220.48.5 está dentro del rango CIDR)
        print("\nPrueba 2: Simulando IP permitida (74.220.48.5)...")
        try:
            res2 = await client.post(f"{BASE_URL}/chat", json={"text": "Hola"}, headers={"X-Forwarded-For": "74.220.48.5"})
            print(f"Status: {res2.status_code}")
            if res2.status_code == 200:
                print("Resultado: Acceso PERMITIDO (Correcto)")
        except Exception as e:
            print(f"Error: {e}")

        # 3. Simulando IP no permitida
        print("\nPrueba 3: Simulando IP externa NO permitida (1.1.1.1)...")
        try:
            res3 = await client.post(f"{BASE_URL}/chat", json={"text": "Hola"}, headers={"X-Forwarded-For": "1.1.1.1"})
            print(f"Status: {res3.status_code} - Detail: {res3.json().get('detail')}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(run_tests())