class DeepScoutError(Exception):
    """Base exception for DeepScout."""
    pass


class ResearchError(DeepScoutError):
    """Raised when the research pipeline fails."""
    pass