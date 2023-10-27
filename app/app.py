import threading

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mouse import MouseCircler

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


mouse_circler = MouseCircler()


@app.get("/")
async def on_heath():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Aplicação rodando"})


@app.get("/health")
async def on_heath():
    return status.HTTP_200_OK


@app.get("/mouse_circle")
async def toggle_mouse_circle():
    mouse_circler.on_move(0, 0)
    threading.Thread(target=mouse_circler.move_mouse_in_circles).start()

    return "Mouse circles started!"


@app.middleware('http')
async def get_error(request: Request, call_next):
    response = await call_next(request)
    response.headers["referrer-policy"] = "strict-origin-when-cross-origin"

    return response

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
