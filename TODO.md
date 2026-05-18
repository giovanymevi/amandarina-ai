# TODO

- [x] Confirmar lista de IPs/CIDR a aplicar (74.220.48.0/24 y 74.220.56.0/24) y comportamiento: allowlist.
- [x] Implementar filtro por IP en `main.py` para endpoint `POST /chat` usando allowlist.
- [x] Considerar IP real detrás de proxy (usar `X-Forwarded-For` si existe, con fallback a `request.client.host`).
- [x] Actualizar respuesta cuando la IP no esté permitida (HTTP 403 + mensaje genérico).
- [x] Ejecutar prueba rápida: iniciar servidor y hacer request desde IP no permitida (si es posible) para verificar 403.
- [x] Actualizar `requirements.txt` con `fastapi[standard]` para evitar errores de CLI en Render.
- [ ] Realizar nuevo deploy en Render y verificar que el comando `uvicorn` inicie sin errores.
