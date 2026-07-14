import logging
import uuid
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

# Filter out /server-id polling and WebSocket connection attempts/warnings from console logs
class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        if any(ignored in message for ignored in ("/server-id", "/docs/ws", "ws-reload", "connection rejected")):
            return False
        return True

for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
    logging.getLogger(logger_name).addFilter(EndpointFilter())


def setup_swagger_reload(app: FastAPI):
    """
    Enables quiet auto-hot-reloading for the Swagger UI (/docs).
    Disables console log spam of polling requests.
    """
    SERVER_ID = str(uuid.uuid4())

    @app.get("/server-id", include_in_schema=False)
    async def get_server_id():
        return {"server_id": SERVER_ID}

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html() -> HTMLResponse:
        # Get the standard Swagger UI HTML with cache-busted openapi_url
        response = get_swagger_ui_html(
            openapi_url=f"{app.openapi_url}?t={SERVER_ID}" if app.openapi_url else None,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        )
        
        # Auto-reconnect script: checks every 500ms if the server ID has changed.
        # Uses cache-busting query parameter to avoid cached responses.
        reload_script = f"""
        <script>
            const currentServerId = "{SERVER_ID}";
            function checkServer() {{
                fetch('/server-id?t=' + Date.now())
                    .then(response => response.json())
                    .then(data => {{
                        if (data.server_id !== currentServerId) {{
                            window.location.reload();
                        }} else {{
                            setTimeout(checkServer, 500);
                        }}
                    }})
                    .catch(error => {{
                        // Server is likely restarting, try again soon
                        setTimeout(checkServer, 500);
                    }});
            }}
            setTimeout(checkServer, 500);
        </script>
        """
        
        # Decode the response body and inject our script right before </body>
        html_content = response.body.decode("utf-8")
        modified_html = html_content.replace("</body>", f"{reload_script}</body>")
        
        return HTMLResponse(content=modified_html, status_code=response.status_code)
