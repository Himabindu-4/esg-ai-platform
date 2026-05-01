from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# =========================
# IMPORT ROUTES
# =========================
from app.api.esg_routes import router as esg_router
from app.api.peer_compare import router as peer_router
from app.api.history_routes import router as history_router
from app.api.news_routes import router as news_router
from app.api.screener_routes import router as screener_router
from app.api.portfolio_routes import router as portfolio_router
from app.api.report_routes import router as report_router  # ✅ NEW


# =========================
# INIT APP
# =========================
app = FastAPI(title="ESG AI Platform")


# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# ROUTES
# =========================
app.include_router(esg_router, prefix="/api")
app.include_router(peer_router, prefix="/api")
app.include_router(history_router, prefix="/api")
app.include_router(news_router, prefix="/api")
app.include_router(screener_router, prefix="/api")
app.include_router(portfolio_router, prefix="/api")

# ✅ PDF REPORT ROUTE
app.include_router(report_router, prefix="/api")


# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {
        "message": "ESG AI Platform Running Successfully"
    }