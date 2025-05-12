import logging

# Configure logging when the package is imported
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("audio_stream_server package initialized")

# Expose core functions from submodules (optional, for convenience)
from .server import run_server
from .audio_input import get_audio_stream

__all__ = ["run_server", "get_audio_stream"]
