import logging
import os

# Create logs directory in the project root
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/genomictwinops.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("GenomicTwinOps")