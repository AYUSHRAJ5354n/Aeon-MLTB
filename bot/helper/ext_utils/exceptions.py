class DirectDownloadLinkException(Exception):
    """No method found for extracting direct download link from the HTTP link."""


class NotSupportedExtractionArchive(Exception):
    """The archive format the user is trying to extract is not supported."""


class RssShutdownException(Exception):
    """This exception should be raised when shutdown is called to stop the monitor."""


class TgLinkException(Exception):
    """Access denied for this chat."""
