# здесь у меня вся аналитика через NumPy
import numpy as np
from database import districts

# ---------------- AIR QUALITY ----------------
def get_air_stats():
    values = np.array([d["air_quality"] for d in districts])
    return np.mean(values), np.max(values), np.min(values)


# ---------------- TRAFFIC ----------------
def get_traffic_stats():
    values = np.array([d["traffic"] for d in districts])
    return np.mean(values), np.max(values), np.min(values)


# ---------------- INFRASTRUCTURE ----------------
def get_infra_stats():
    values = np.array([d["infrastructure"] for d in districts])
    return np.mean(values), np.max(values), np.min(values)


# ---------------- BEST DISTRICT ----------------
def best_air_district():
    values = np.array([d["air_quality"] for d in districts])
    idx = np.argmax(values)
    return districts[idx]